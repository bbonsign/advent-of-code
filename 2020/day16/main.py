from functools import reduce
from typing import Dict, List
from input import rules, your_ticket, nearby_tickets


def part1():
    invalids = []
    for tkt in nearby_tickets:
        for n in tkt:
            if all(f(n) == False for f in rules.values()):
                invalids.append(n)
    return sum(invalids)


def part2():
    keys = ['departure_location',
            'departure_station',
            'departure_platform',
            'departure_track',
            'departure_date',
            'departure_time']
    idxs = [find_fields(nearby_tickets)[key] for key in keys]
    nums = [your_ticket[i[0]] for i in idxs]
    return reduce(lambda x, y: x*y, nums, 1)


def valid_tickets(tickets):
    valids = []
    for tkt in tickets:
        if not (any(all(f(n) == False for f in rules.values()) for n in tkt)):
            valids.append(tkt)
    return valids


def find_fields(tickets) -> Dict[str, List[int]]:
    valids = valid_tickets(tickets)
    no_fields = len(valids[0])
    d = {key: [] for key in rules.keys()}
    for key, rule in rules.items():
        for i in range(no_fields):
            if all(rule(tkt[i]) for tkt in valids):
                d[key].append(i)
    determined = set()
    while any(len(l) > 1 for l in d.values()):
        for key, l in d.items():
            if len(l) == 1:
                determined.add(l[0])
        for key in d.keys():
            for n in determined:
                if d[key] != [n] and n in d[key]:
                    d[key].remove(n)
    return d
