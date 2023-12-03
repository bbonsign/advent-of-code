import AOC

aoc_test 2023, 1, async: true do
  @example_string AOC.IEx.example_string(year: 2023, day: 1)
  @example_string_2 ~s(
  two1nine
  eightwothree
  abcone2threexyz
  xtwone3four
  4nineeightseven2
  zoneight234
  7pqrstsixteen
  )

  test "part 1" do
    assert p1(@example_string) == 142
  end

  test "part 2" do
    assert p2(@example_string_2) == 281
  end
end
