import AOC

aoc 2023, 4 do
  @moduledoc """
  https://adventofcode.com/2023/day/4
  """

  @doc """
      iex> p1(AOC.IEx.example_string(year: 2023, day: 4))
  """
  def p1(input) do
    input
    |> parse()
    |> Enum.map(&score_game/1)
    |> Enum.sum()
  end

  @doc """
      iex> p2(AOC.IEx.example_string(year: 2023, day: 4))
  """
  def p2(input) do
    input
    |> String.split("\n", trim: true)
    |> Enum.filter(fn s -> String.trim(s) != "" end)
    |> Enum.map(&parse_line/1)
    |> run_part_2()
  end

  def parse(input) do
    input
    |> String.split("\n", trim: true)
    |> Enum.filter(fn s -> String.trim(s) != "" end)
    |> Enum.map(&parse_line/1)
  end

  def parse_line(line) do
    %{
      "draws" => draw_str,
      "card_id" => card_id_str,
      "winning" => winning_str
    } = Regex.named_captures(~r/^Card\s+(?<card_id>\d+): (?<winning>.*)\|(?<draws>.*)/, line)

    {card_id, _} = Integer.parse(card_id_str)

    %{
      "card_id" => card_id,
      "winning" => get_nums(winning_str),
      "draws" => get_nums(draw_str),
      # for part 2
      "count" => 1
    }
  end

  defp get_nums(string_of_numbers) do
    string_of_numbers
    |> String.trim()
    |> String.split()
    |> Enum.map(fn numstr ->
      {num, _} = Integer.parse(numstr)
      num
    end)
    |> Enum.into(MapSet.new())
  end

  def score_game(%{
        "draws" => draws,
        "winning" => winning
      }) do
    overlap = MapSet.intersection(draws, winning) |> MapSet.size()

    if overlap > 0 do
      2 ** (overlap - 1)
    else
      0
    end
  end

  def run_part_2(cards) do
    collected_cards = collect_cards(cards, [])
    length(collected_cards)
  end

  def collect_cards([card | rest] = _cards, collection) do
    %{
      "card_id" => _card_id,
      "winning" => winning,
      "draws" => draws,
      "count" => count
    } = card

    case count do
      0 ->
        collect_cards(rest, collection)

      # Count should be >1 in this case
      _count ->
        overlap = MapSet.intersection(draws, winning) |> MapSet.size()

        {new_cards_copies, tail} = Enum.split(rest, overlap)

        new_cards_copies =
          new_cards_copies
          |> Enum.map(fn card -> Map.update(card, "count", 1, &(&1 + 1)) end)

        collection = [card | collection]
        card = Map.update(card, "count", 1, &(&1 - 1))
        collect_cards([card | Enum.concat(new_cards_copies, tail)], collection)
    end
  end

  def collect_cards([], collection), do: collection
end
