from typing import List, Tuple


test = [35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102,
        117, 150, 182, 127, 219, 299, 277, 309, 576, ]


def check_error(stream: List[int], pos: int, amount: int = 25) -> bool:
    """Returns True if the stream[pos] is invalid"""
    target = stream[pos]
    candidates = set(stream[pos-amount:pos])
    differences = {target-candidate for candidate in candidates}
    return candidates.isdisjoint(differences)


def part1(stream: List[int], amount: int = 25) -> int:
    t = {'is_error': False, 'idx': amount+1}
    while not t['is_error']:
        t['is_error'] = check_error(stream, t['idx'], amount)
        t['idx'] += 1
    return stream[t['idx']-1]


def part2(stream: List[int], target: int) -> int:
    """Target is the result of part1"""
    idx_of_target = stream.index(target)
    # candidates = stream[:idx_of_target]
    for i in range(idx_of_target):
        j = 0
        summands = []
        while sum(summands) < target:
            summands.append(stream[i+j])
            j += 1
        if sum(summands) == target:
            print(summands)
            return min(summands)+max(summands)
    return -1
