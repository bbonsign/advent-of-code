import re
from input import tst, inp, invalids, valids
from typing import Dict, Iterator, List, Tuple


def split(inp: str) -> Iterator[List[str]]:
    chunks = inp.split("\n\n")
    return map(lambda chunk: chunk.split(), chunks)


def parse(chunk: List[str]) -> Dict[str, str]:
    fields: List[Tuple[str, str]] = [
        tuple(field.split(':')) for field in chunk]
    return dict(fields)


def passports(inp: str) -> Iterator[Dict[str, str]]:
    return map(parse, split(inp))


def isValid(passport: Dict[str, str]) -> bool:
    return len(passport) == 8 or (len(passport) == 7 and 'cid' not in passport)


def fieldValidate(param: str, passport: Dict[str, str]):
    field = passport.get(param, None)
    if field is None:
        return False
    if param == 'byr':
        field = int(field)
        return 1920 <= field <= 2002
    if param == 'iyr':
        field = int(field)
        return 2010 <= field <= 2020
    if param == 'eyr':
        field = int(field)
        return 2020 <= field <= 2030
    if param == 'hgt':
        split = re.split(r'(cm|in)', field)
        if len(split) == 3:
            if split[2] == '':
                [meas, unit] = split[:2]
                if unit == 'in':
                    return 59 <= int(meas) <= 76
                if unit == 'cm':
                    return 150 <= int(meas) <= 193
            return False
        return False
    if param == 'hcl':
        return bool(re.match(r'^#[0-9a-f]{6}', field))
    if param == 'ecl':
        return field in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if param == 'pid':
        return bool(re.match(r'[0-9]{9}', field))


def isValid2(passport):
    params = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    return all(map(lambda fld: fieldValidate(fld, passport), params))


def part2Test():
    v_passports = list(passports(valids))
    iv_passports = list(passports(invalids))
    v = len(
        list(filter(lambda x: x, [isValid2(passport) for passport in v_passports])))
    iv = len(
        list(filter(lambda x: x, [isValid2(passport) for passport in iv_passports])))
    print(
        f"valids: {v}/{len(v_passports)},\ninvalids: {iv}/{len(iv_passports)}")


def part2():
    test = len(
        list(filter(lambda x: x, [isValid2(passport) for passport in passports(tst)])))
    real = len(
        list(filter(lambda x: x, [isValid2(passport) for passport in passports(inp)])))
    print(f"test: {test},\nreal: {real}")


def part1():
    sample = len(
        list(filter(lambda x: x, [isValid(passport) for passport in passports(tst)])))
    real = len(
        list(filter(lambda x: x, [isValid(passport) for passport in passports(inp)])))
    print(f"test: {sample},\nreal: {real}")
