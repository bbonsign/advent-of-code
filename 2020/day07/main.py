import re
import functools
from typing import Dict, List
from inp import test, inp

test: List[str] = test.splitlines()
inp: List[str] = inp.splitlines()


def memoize(func):
    cache = func.cache = {}

    @functools.wraps(func)
    def memoized_func(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return memoized_func


def parse_line(line: str) -> List[List[str]]:
    pieces = re.split(r'bags contain|bags?[,.]', line)
    pieces = [x for piece in pieces if (x := re.split(r'(\d+)', piece))]
    pieces = [[x for s in piece if (x := s.strip())] for piece in pieces]
    pieces = [piece for piece in pieces if piece]
    return [piece if piece[-1] != 'no other' else ['0', ''] for piece in pieces]

    # return pieces if pieces[-1] != 'no other' else [pieces[0], '']


def make_dict(lines: List[str]) -> Dict[str, List[str]]:
    d = {}
    for line in lines:
        line = parse_line(line)
        d[line[0][0]] = line[1:]
    return d


@memoize
def check(bag: str, rules: Dict[str, List[str]]) -> bool:
    """Can a bag hold a shiny gold bag at some depth?"""
    innerbags = [spec[1] for spec in rules[bag]]
    if innerbags[0] == '':
        return False
    if 'shiny gold' in innerbags:
        return True
    else:
        return any(check(bag, rules) for bag in innerbags)


@memoize
def count(bag: str, rules: Dict[str, List[str]]) -> int:
    """How many bags must be cotained in bag?"""
    innerbags = rules[bag]
    if innerbags[0][0] == '0':
        return 0
    return sum(int(bag[0])+int(bag[0])*count(bag[1], rules) for bag in innerbags)


def part1():
    rules = make_dict(inp)
    return sum(check(bag, rules) for bag in rules)


def part2():
    rules = make_dict(inp)
    return count('shiny gold', rules)
