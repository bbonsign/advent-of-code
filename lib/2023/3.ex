import AOC

aoc 2023, 3 do
  @moduledoc """
  https://adventofcode.com/2023/day/3
  """
  @symbol_regex ~r/[^1-9^\.]/
  @line_length 140

  @doc """
      iex> p1(AOC.IEx.example_string(year: 2023, day: 3))
  """
  def p1(input) do
    input
    |> parse()
    |> get_part_numbers()
    |> Enum.sum()
  end

  @doc """
      iex> p2(AOC.IEx.example_string(year: 2023, day: 3))
  """
  def p2(input) do
    input
    |> parse()
    |> get_gear_ratios()
    |> Enum.sum()
  end

  def parse(input) do
    input
    |> String.split("\n", trim: true)
    |> Enum.filter(fn s -> String.trim(s) != "" end)
  end

  def get_part_numbers(lines) do
    lines
    |> Enum.with_index()
    |> Enum.flat_map(fn {line, line_no} -> get_part_numbers(line, line_no, lines) end)
  end

  def get_part_numbers(line, line_no, lines) do
    Regex.scan(~r(\d+), line, return: :index)
    |> Enum.filter(fn [{index, offset}] ->
      neighboring_symbol?({index, offset}, line, line_no, lines)
    end)
    |> Enum.map(fn [{index, offset}] ->
      {number, _} = String.slice(line, index, offset) |> Integer.parse()
      number
    end)
  end

  defp neighboring_symbol?({index, offset}, line, line_number, lines) do
    at_top? = line_number == 0
    at_bottom? = line_number == length(lines) - 1
    at_left? = index == 0
    at_right? = index + offset == @line_length
    slice_left = if at_left?, do: index, else: index - 1
    slice_offset = if at_right? or at_left?, do: offset + 1, else: offset + 2

    [
      if(at_left?, do: "", else: String.slice(line, slice_left, 1)),
      if(at_right?, do: "", else: String.slice(line, index + offset, 1)),
      if(at_top?,
        do: "",
        else: String.slice(Enum.at(lines, line_number - 1), slice_left, slice_offset)
      ),
      if(at_bottom?,
        do: "",
        else: String.slice(Enum.at(lines, line_number + 1), slice_left, slice_offset)
      )
    ]
    |> Enum.map(fn string -> Regex.match?(@symbol_regex, string) end)
    |> Enum.any?()
  end

  def get_gear_ratios(lines) do
    number_spans = Enum.map(lines, fn line -> Regex.scan(~r(\d+), line, return: :index) end)
    possible_gears = Enum.map(lines, fn line -> Regex.scan(~r(\*), line, return: :index) end)

    gear_ratios_spans =
      possible_gears
      |> Enum.with_index()
      |> Enum.filter(fn {match_list, _line_no} -> match_list != [] end)
      |> Enum.flat_map(fn {match_list, line_no} ->
        match_list |> Enum.map(fn match -> {match, line_no} end)
      end)
      |> Enum.map(fn {[{gear_index, _}], line_number} ->
        at_top? = line_number == 0
        at_bottom? = line_number == length(lines) - 1
        at_left? = gear_index == 0
        at_right? = gear_index == @line_length - 1

        %{
          number_left:
            if at_left? do
              []
            else
              Enum.map(Enum.at(number_spans, line_number), fn [{no_index, offset}] ->
                if no_index + offset == gear_index do
                  {no_index, offset, line_number}
                else
                  nil
                end
              end)
            end,
          number_right:
            if at_right? do
              []
            else
              Enum.map(Enum.at(number_spans, line_number), fn [{no_index, offset}] ->
                if no_index - 1 == gear_index do
                  {no_index, offset, line_number}
                else
                  nil
                end
              end)
            end,
          numbers_above:
            if(at_top?,
              do: [],
              else:
                Enum.map(Enum.at(number_spans, line_number - 1), fn [{no_index, offset}] ->
                  if no_index - 1 <= gear_index and gear_index <= no_index + offset do
                    {no_index, offset, line_number - 1}
                  else
                    nil
                  end
                end)
            ),
          numbers_below:
            if at_bottom? do
              []
            else
              Enum.map(Enum.at(number_spans, line_number + 1), fn [{no_index, offset}] ->
                if no_index - 1 <= gear_index and gear_index <= no_index + offset do
                  {no_index, offset, line_number + 1}
                else
                  nil
                end
              end)
            end
        }
        |> Enum.flat_map(fn {_, v} -> v end)
        |> Enum.filter(fn v -> v end)
      end)
      |> Enum.filter(fn l -> length(l) == 2 end)

    gear_ratios_spans
    |> Enum.map(fn [{i1, o1, ln1}, {i2, o2, ln2}] ->
      {num1, _} = lines |> Enum.at(ln1) |> String.slice(i1, o1) |> Integer.parse()
      {num2, _} = lines |> Enum.at(ln2) |> String.slice(i2, o2) |> Integer.parse()
      {num1, num2}
    end)
    |> Enum.map(fn {x, y} -> x * y end)
  end
end
