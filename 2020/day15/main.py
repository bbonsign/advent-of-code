sample = [0, 3, 6]
inp = [0, 1, 4, 13, 15, 12, 16]


def nth_spoken(n, nums):
    """Answers part1, but too slow for part2"""
    while len(nums) < n:
        last = nums[-1]
        prev = False
        for i in range(-2, -len(nums)-1, -1):
            if nums[i] == last:
                prev = True
                nums.append(-1-i)
                break
        if not prev:
            nums.append(0)
    return nums[-1]


def part2(n, nums):
    """Answers part1, but too slow for part2"""
    num_map = {pair[1]: (pair[0]+1) for pair in enumerate(nums)}
    turn = len(nums)
    last = nums[-1]
    while turn < n:
        # print(f"======turn {turn}")
        # print(last, num_map)
        prev = num_map.setdefault(last, turn)  # 3
        # print(prev, turn)
        if prev == turn+1:
            last = 0
        else:
            num_map[last] = turn
            last = turn - prev
        turn += 1
        # print(num_map)
    return last
