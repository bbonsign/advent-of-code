# Part 1 from ipython:

# get lines of the input file
# ins = !cat input

i = 0
d = {0: set()}

for line in ins:
    if line == '':
        i += 1
        d[i] = set()
    else:
        s = d.get(i, set())
        d[i] = s.union(set(line))

answer = sum((len(v) for v in d.values()))

# Part 2 similar:
i = 0
d = {0: set('abcdefghijklmnopqrstuvwxyz')}

for line in ins:
    if line == '':
        i += 1
        d[i] = set('abcdefghijklmnopqrstuvwxyz')
    else:
        s = d.get(i, set('abcdefghijklmnopqrstuvwxyz'))
        d[i] = s.union(set(line))

answer2 = sum((len(v) for v in d.values()))
