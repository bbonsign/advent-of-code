import AOC

aoc_test 2023, 3, async: true do
  @example_string AOC.IEx.example_string(year: 2023, day: 3)

  test "part 1" do
    assert p1(@example_string) == 4361
  end

  test "part 2" do
    assert p2(@example_string) == 467_835
  end
end
