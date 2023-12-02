import re
from operator import add, mul

from input import inp


def no_parens(s):
    print("no_parens1: ", s)
    if isinstance(s, re.Match):
        s = s.group()
        if '(' in s:
            s = s.group()[1:-1]
    ops = {'+': add, '*': mul}
    parsed = ['']
    for i in s:
        if i.isdigit() and parsed[-1] not in ops.keys():
            parsed[-1] += i
        elif i in ops.keys():
            parsed += [i]
        else:
            parsed.append(i)
    for i in range(len(parsed)):
        if parsed[i].isnumeric():
            parsed[i] = int(parsed[i])
    operand1 = parsed[0]
    operator = parsed[1]
    operand2 = parsed[2]
    for p in parsed[2:]:
        if isinstance(p, int):
            operand2 = p
            operand1 = ops[operator](operand1, operand2)
        else:
            operator = p
    return str(operand1)


def eval_expression(s):
    # print(s)
    if '(' in s:
        s = re.sub(r'\([\d+*]*\)', no_parens, s)
        return eval_expression(s)
    else:
        return no_parens(s)


def part1():
    return sum(int(eval_expression(s)) for s in inp)


def eval_expression2(s):
    print("eval: ", s)
    if '(' in s:
        s = re.sub(r'\([\d+*]*\)', no_parens2, s)
        return eval_expression2(s)
    else:
        return no_parens2(s)


def no_parens2(s):
    if isinstance(s, re.Match):
        s = s.group()[1:-1]
    # ops = {'+': add, '*': mul}
    print(s)
    if '+' in s:
        s = re.sub(r'\d+\+\d+', no_parens, s)
        print(s)
        return no_parens2(s)
    elif '*' in s:
        return no_parens(s)
    else:
        return s


def part2():
    return sum(int(eval_expression2(s)) for s in inp)
