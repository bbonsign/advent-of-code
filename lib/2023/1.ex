import AOC

defmodule Parse do
  @digits %{
    "1" => "1",
    "2" => "2",
    "3" => "3",
    "4" => "4",
    "5" => "5",
    "6" => "6",
    "7" => "7",
    "8" => "8",
    "9" => "9",
    "one" => "1",
    "two" => "2",
    "three" => "3",
    "four" => "4",
    "five" => "5",
    "six" => "6",
    "seven" => "7",
    "eight" => "8",
    "nine" => "9"
  }

  def parse(input, get_digits_from_line_fn) do
    input
    |> String.split("\n", trim: true)
    |> Enum.filter(fn s -> String.trim(s) != "" end)
    |> Enum.map(fn line -> get_digits_from_line_fn.(line |> String.trim()) end)
  end

  def get_digits1(line) do
    nums =
      line
      |> String.split("", trim: true)
      |> Enum.map(&Integer.parse/1)
      |> Enum.filter(fn x -> x != :error end)

    {{first, _}, {last, _}} = {List.first(nums), List.last(nums)}
    10 * first + last
  end

  def get_digits2(line) do
    len = String.length(line)

    digit_str =
      Enum.reduce(
        0..len,
        "",
        fn idx, acc ->
          slice = line |> String.slice(idx..-1)

          maybe_digit =
            Enum.find(
              @digits,
              fn {digitstr, _v} -> slice |> String.starts_with?(digitstr) end
            )

          next_char =
            case maybe_digit do
              {_str, val} -> val
              _ -> ""
            end

          acc <> next_char
        end
      )

    get_digits1(digit_str)
  end
end

aoc 2023, 1 do
  @moduledoc """
  https://adventofcode.com/2023/day/1
  """
  import Parse

  @doc """
      iex> p1(AOC.IEx.example_string(year: 2023, day: 1))
  """
  def p1(input) do
    input
    |> parse(&get_digits1/1)
    |> Enum.sum()
  end

  @doc """
      iex> p2(AOC.IEx.example_string(year: 2023, day: 1))
  """
  def p2(input) do
    input
    |> parse(&get_digits2/1)
    |> Enum.sum()
  end
end
