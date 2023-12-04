import AOC

aoc_test 2023, 4, async: true do
  @example_string AOC.IEx.example_string(year: 2023, day: 4)

  test "part 1" do
    assert p1(@example_string) == 13
  end

  test "part 2" do
    assert p2(@example_string) == 30
  end
end
