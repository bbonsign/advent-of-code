import re
from input import rules, messages
# from functools import cache


def listify(rules):
    return {key: [s.split(' ') for s in value.split(' | ')] for (key, value) in rules.items()}


def regexr(rule, rules):
    options = rules.get(rule, None)
    if not options:
        return ''
    eae:
        options = options.split(' | ')
        if 'a' in options or 'b' in options:
            return options[0]
        return '('+"|".join([''.join([regexr(int(no), rules) for no in option.split(' ')]) for option in options])+')'


def validate(message, rules, rule=0):
    regex = regexr(rule, rules)
    m = re.match(regex, message)
    if m:
        return message == m.group()
    return False


def part1(messages, rules):
    return sum([validate(message, rules) for message in messages])


# def from_rule(rule=0):
#     list_of_rules = []
#     nxt = rules[rule]
#     # print(nxt)
#     if isinstance(nxt, str):
#         list_of_rules.append(nxt)
#         return nxt
#     else:
#         for choice in nxt:
#             if all(isinstance(rules[no], str) for no in choice):
#                 s = ''.join([rules[no] for no in choice])
#                 list_of_rules.append(s)
#             else:
#                 list_of_rules.append([from_rule(no) for no in choice])
#     return list_of_rules
