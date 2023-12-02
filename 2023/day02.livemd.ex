# 2023 - Day 02

```elixir
Mix.install([
  {:kino_aoc, git: "https://github.com/ljgago/kino_aoc"},
  :kino,
  :kino_vega_lite
  # :explorer
  # :nx,
])

alias VegaLite, as: Vl
# alias Explorer.DataFrame, as: DF
# alias Explorer.Series
ExUnit.start()
```

## Puzzle

[https://adventofcode.com/2023/day/2](https://adventofcode.com/2023/day/2)

<!-- livebook:{"attrs":{"assign_to":"puzzle_input","day":"2","session_secret":"AOC_TOKEN","year":"2023"},"chunks":null,"kind":"Elixir.KinoAOC.HelperCell","livebook_object":"smart_cell"} -->

```elixir
{:ok, puzzle_input} =
  KinoAOC.download_puzzle("2023", "2", System.fetch_env!("LB_AOC_TOKEN"))
```

## Solution

```elixir
defmodule Game do
  defstruct [:id, :draws]

  @given_dice %{
    "red" => 12,
    "green" => 13,
    "blue" => 14
  }

  def from_string(line) do
    %{"id" => id, "rest" => rest} = Regex.named_captures(~r/^Game (?<id>\d+): (?<rest>.*)/, line)
    {id, _} = Integer.parse(id)

    lists =
      rest
      |> String.split(";", trim: true)
      |> Enum.map(&String.trim/1)
      |> Enum.map(fn set -> String.split(set, ", ", trim: true) end)

    draws =
      for set <- lists do
        set
        |> Enum.map(fn str ->
          [numstr, color] = String.split(str)
          {num, _} = Integer.parse(numstr)
          {color, num}
        end)
        |> Enum.into(%{})
      end

    %__MODULE__{id: id, draws: draws}
  end

  def min_dice_power(game = %__MODULE__{}) do
    ["red", "green", "blue"]
    |> Enum.map(fn color ->
      draw =
        game.draws
        |> Enum.max_by(fn draw -> Map.get(draw, color, 0) end)

      draw[color]
    end)
    |> Enum.product()

    #  max_red = 
    #  max_green = game.draws |> Enum.max_by(fn draw -> Map.get(draw, "green", 0) end)
    #  max_blue = game.draws |> Enum.max_by(fn draw -> Map.get(draw, "blue", 0) end)
    #  max_red Enum.pr
  end

  def valid?(game = %__MODULE__{}) do
    Enum.all?(
      game.draws,
      fn draw -> valid_draw?(draw, @given_dice) end
    )
  end

  defp valid_draw?(draw, given_dice) do
    Enum.all?([
      Map.get(draw, "red", 0) <= Map.get(given_dice, "red", 0),
      Map.get(draw, "green", 0) <= Map.get(given_dice, "green", 0),
      Map.get(draw, "blue", 0) < Map.get(given_dice, "blue", 0),
      Enum.sum(Map.values(draw)) <= Enum.sum(Map.values(given_dice))
    ])
  end
end

defmodule Parse do
  def parse(input) do
    input
    |> String.split("\n", trim: true)
    |> Enum.filter(fn s -> String.trim(s) != "" end)
    |> Enum.map(fn line -> Game.from_string(String.trim(line)) end)
  end
end
```

```elixir
defmodule DayTwo do
  import Parse

  def part_one(input) do
    input
    |> parse()
    |> filter_valid_games()
    |> Enum.map(fn game -> game.id end)
    |> Enum.sum()
  end

  defp filter_valid_games(games) do
    games |> Enum.filter(&Game.valid?/1)
  end

  def part_two(input) do
    input
    |> Parse.parse()
    |> Enum.map(&Game.min_dice_power/1)
    |> Enum.sum()
  end
end
```

## Test

```elixir
defmodule Test do
  use ExUnit.Case, async: true
  @example_input ~s(
  Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
  Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
  Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
  Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
  Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
  )

  test "part 1" do
    assert DayTwo.part_one(@example_input) == 8
  end

  test "part 2" do
    assert DayTwo.part_two(@example_input) == 2286
  end
end

ExUnit.run()
```

```elixir
DayTwo.part_one(puzzle_input)
```

```elixir
DayTwo.part_two(puzzle_input)
```

<!-- livebook:{"offset":3657,"stamp":{"token":"XCP.z4UNnrQhvn9yFQrR-dpN7FgR82_IxFG4-t8n-SV84frGbgVL2d0C8cW5xqdS5RliShiGDcMWBqFzNNeQ8bNm97odu1R2j0RyXFaE9MmJX3B6n6TOCw","version":2}} -->
