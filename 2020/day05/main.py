from typing import Dict, List
from input import input
rows = list(range(128))

assignments = [{'row': a[0:7], 'col': a[7:]} for a in input.split()]


def rowbin(pattern):
    binpat = ''.join(list(map(lambda x: '0' if x == 'F' else '1', pattern)))
    return int('0b'+binpat, 2)


def colbin(pattern):
    binpat = ''.join(list(map(lambda x: '0' if x == 'L' else '1', pattern)))
    return int('0b'+binpat, 2)


part1 = max([8*rowbin(a['row']) + colbin(a['col']) for a in assignments])


def divide(l: List[int]):
    length = len(l)
    if length == 1:
        return l[0]
    return [l[:length//2], l[length//2:]]


def makeTree(l: List[int], d: Dict):
    length = len(l)
    if length == 0:
        return d
    if length == 1:
        d['value'] = l[0]
        return d
    [front, back] = divide(l)
    d['F'] = makeTree(front, {})
    d['B'] = makeTree(back, {})
    return d


def get_number(pattern, tree):
    for d in pattern:
        tree = tree.get('value', tree[d])
    return tree


# Part 2 from ipython:
ids = sorted([8*rowbin(a['row'])+colbin(a['col']) for a in assignments])
x = []
for (i, id) in enumerate(ids):
    if i == 0 or i == len(ids)-1:
        x.append(0)
    test = (ids[i-1]+ids[i+1])/2 - id
    if test == 0:
        x.append(0)
    else:
        x.append(id)
