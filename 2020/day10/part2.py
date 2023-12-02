from functools import reduce, cache
import operator


# This one finally works -- dynamic programming
def part2(inp_sorted):
    cache = {0: 1}
    for n in inp_sorted:
        for prev in [n-3, n-2, n-1]:
            if prev in cache:
                cache.setdefault(n, 0)
                cache[n] += cache[prev]
    return cache[inp_sorted[-1]]


def no_next_steps(inp_sorted):
    nums = []
    for i in inp_sorted:
        l = sum([0 < n-i <= 3 for n in inp_sorted])
        nums.append(l)
    return sum([n for n in nums if n != 1])+1, nums[:-1]


def isDict(d):
    return isinstance(d, dict)


def isAtomOrFlat(d):
    return not isDict(d) or not any(isDict(v) for v in d.values())


def leafPaths(nestedDicts, noDeeper=isAtomOrFlat):
    """
        For each leaf in NESTEDDICTS, this yields a
        dictionary consisting of only the entries between the root
        and the leaf.
    """
    for key, value in list(nestedDicts.items()):
        if noDeeper(value):
            yield [key]
        else:
            for subpath in leafPaths(value):
                yield [key]+subpath


def getFromDict(dataDict, mapList):
    return reduce(operator.getitem, mapList, dataDict)


def setInDict(dataDict, mapList, value):
    getFromDict(dataDict, mapList[:-1])[mapList[-1]] = value


def prod(nums):
    return reduce(lambda x, y: x*y, nums, 1)


def leaves(tree, leafs=[]):
    for key, value in tree.items():
        if len(value) == 0:
            leafs.append(key)
        else:
            leaves(value, leafs)
    return leafs


@cache
def tree(i, inp_sorted: tuple):
    if i == inp_sorted[-1]:
        return {}
    else:
        ret_tree = {}
        idx = inp_sorted.index(i)
        for val in inp_sorted[idx+1:]:
            # print(idx, val, inp_sorted[idx:])
            if val-i <= 3:
                ret_tree[val] = tree(val, inp_sorted)
        return ret_tree


def collections(inp_sorted):
    last = inp_sorted[-1]
    old_tree = {last: {}}
    tree = {}
    for i in inp_sorted[:-1]:
        for path in leafPaths(tree):
            for idx, val in enumerate(path):
                if 0 <= i-val <= 3:
                    tree[i] = old_tree
        old_tree = tree
    return tree


sample = [16,
          10,
          15,
          5,
          1,
          11,
          7,
          19,
          6,
          12,
          4]
sample_sorted = sorted(sample)

sample2 = [28,
           33,
           18,
           42,
           31,
           14,
           46,
           20,
           48,
           47,
           24,
           23,
           49,
           45,
           19,
           38,
           39,
           11,
           1,
           32,
           25,
           35,
           8,
           17,
           7,
           9,
           4,
           2,
           34,
           10,
           3]
sample2_sorted = sorted(sample2)

inp = [95,
       43,
       114,
       118,
       2,
       124,
       120,
       127,
       140,
       21,
       66,
       103,
       102,
       132,
       136,
       93,
       59,
       131,
       32,
       9,
       20,
       141,
       94,
       109,
       143,
       142,
       65,
       73,
       27,
       83,
       133,
       104,
       60,
       110,
       89,
       29,
       78,
       49,
       76,
       16,
       34,
       17,
       105,
       98,
       15,
       106,
       4,
       57,
       1,
       67,
       71,
       14,
       92,
       39,
       68,
       125,
       113,
       115,
       26,
       33,
       61,
       45,
       46,
       11,
       99,
       7,
       25,
       130,
       42,
       3,
       10,
       54,
       44,
       139,
       50,
       8,
       58,
       86,
       64,
       77,
       35,
       79,
       72,
       36,
       80,
       126,
       28,
       123,
       119,
       51,
       22]

inp_sorted = sorted(inp)
