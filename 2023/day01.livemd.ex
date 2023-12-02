# 2023 - Day 01

```elixir
Mix.install([
  {:kino_aoc, git: "https://github.com/ljgago/kino_aoc"},
  :kino,
  :kino_vega_lite,
  :explorer
  # :nx,
])

alias VegaLite, as: Vl
alias Explorer.DataFrame, as: DF
alias Explorer.Series
ExUnit.start()
```

## Puzzle

[https://adventofcode.com/2023/day/1](https://adventofcode.com/2023/day/1)

<!-- livebook:{"attrs":{"assign_to":"puzzle_input","day":"1","session_secret":"AOC_TOKEN","year":"2023"},"chunks":null,"kind":"Elixir.KinoAOC.HelperCell","livebook_object":"smart_cell"} -->

```elixir
{:ok, puzzle_input} =
  KinoAOC.download_puzzle("2023", "1", System.fetch_env!("LB_AOC_TOKEN"))
```

## Solution

```elixir
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
```

```elixir
defmodule DayOne do
  import Parse

  def part_one(input) do
    input
    |> parse(&get_digits1/1)
    |> Enum.sum()
  end

  def part_two(input) do
    input
    |> Parse.parse(&get_digits2/1)
    |> Enum.sum()
  end
end
```

```elixir
defmodule Test do
  use ExUnit.Case, async: true
  @example_input ~s(
  1abc2
  pqr3stu8vwx
  a1b2c3d4e5f
  treb7uchet 
  )

  test "part 1" do
    assert DayOne.part_one(@example_input) == 142
  end

  @example_input2 ~s(
  two1nine
  eightwothree
  abcone2threexyz
  xtwone3four
  4nineeightseven2
  zoneight234
  7pqrstsixteen
  )
  test "part 2" do
    assert DayOne.part_two(@example_input2) == 281
  end
end

ExUnit.run()
```

## Test

```elixir
DayOne.part_one(puzzle_input)
```

```elixir
DayOne.part_two(puzzle_input)
```

<!-- livebook:{"offset":2864,"stamp":{"token":"XCP.LNxXq2vcI746FFgVxDWRA8t4BPUITcIT-2jWoe7x0SxDqAwz4b0SBMbx0Q04qtP-r3wVCajeCTMOrTSWbVBwNTqTMHhOEsAw2s-eLKhptGwnTLr7VA","version":2}} -->
