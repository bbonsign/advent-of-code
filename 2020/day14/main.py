from typing import List
from inp import inp


def mask_num(mask: str, n: int):
    mask = mask[7:]  # cut off leading 'mask = '
    bin_n = format(n, f'0{len(mask)}b')  # Padded with leading 0s
    pairs = list(zip(bin_n, mask))
    masked_bin = '0b'+''.join([d[0] if d[1] == 'X' else d[1] for d in pairs])
    return int(masked_bin, base=2)


def run1(instructions: List[str]):
    mask = ''
    memory = {}
    for instruction in instructions:
        if instruction[:3] == 'mas':
            mask = instruction
        else:
            addr = int(instruction[instruction.index(
                '[')+1:instruction.index(']')])
            n = int(instruction[instruction.index('= ')+2:])
            memory.update([(addr, mask_num(mask, n))])
    return sum(memory.values())


def floating_masks(mask: str, n: int) -> List[int]:
    mask = mask[7:]  # cut off leading 'mask = '
    bin_n = format(n, f'0{len(mask)}b')  # Padded with leading 0s
    pairs = list(zip(bin_n, mask))
    masked_bin = ''
    for pair in pairs:
        if pair[1] == '0':
            masked_bin += pair[0]
        elif pair[1] == '1':
            masked_bin += '1'
        else:
            masked_bin += 'X'
    addrs = []
    for bin_i in binstrings(masked_bin.count('X')):
        addr, j = '', 0
        for d in masked_bin:
            if d == 'X':
                addr += bin_i[j]
                j += 1
            else:
                addr += d
        addrs.append(int('0b'+addr, base=2))
    return addrs


def binstrings(n):
    """return list of binary strings of length n"""
    if n == 1:
        return ['0', '1']
    else:
        return ['0'+d for d in binstrings(n-1)]+['1'+d for d in binstrings(n-1)]


def run2(instructions: List[str]):
    mask = ''
    memory = {}
    for instruction in instructions:
        if instruction[:3] == 'mas':
            mask = instruction
        else:
            addr = int(instruction[instruction.index(
                '[')+1:instruction.index(']')])
            masked_addrs = floating_masks(mask, addr)
            n = int(instruction[instruction.index('= ')+2:])
            memory.update([(addr, n) for addr in masked_addrs])
    return sum(memory.values())
