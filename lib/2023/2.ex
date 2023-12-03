import AOC

aoc 2023, 2 do
  @moduledoc """
  https://adventofcode.com/2023/day/2
  """

  @doc """
      iex> p1(AOC.IEx.example_string())
  """
  def p1(input) do
    input
    |> parse()
    |> filter_valid_games()
    |> Enum.map(fn game -> game.id end)
    |> Enum.sum()
  end

  defp filter_valid_games(games) do
    games |> Enum.filter(&Game.valid?/1)
  end

  @doc """
      iex> p2(AOC.IEx.example_string())
  """
  def p2(input) do
    input
    |> parse()
    |> Enum.map(&Game.min_dice_power/1)
    |> Enum.sum()
  end

  def parse(input) do
    input
    |> String.split("\n", trim: true)
    |> Enum.filter(fn s -> String.trim(s) != "" end)
    |> Enum.map(fn line -> Game.from_string(String.trim(line)) end)
  end
end

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
