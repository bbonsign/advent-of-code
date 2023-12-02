from typing import Dict, List, Tuple
from input import inp, test

State = Dict[str, int]
Instruction = Tuple[str, int]

inp: List[str] = inp.splitlines()
test: List[str] = test.splitlines()


def parse_line(line: str) -> Instruction:
    operation = line[:3]
    argument = int(line[4:])
    return (operation, argument)


inp = [parse_line(i) for i in inp]
test = [parse_line(i) for i in test]


def run_instruction(instruction: Instruction, state: State) -> State:
    operation = instruction[0]
    amount = instruction[1]
    if operation == 'nop':
        state['adr'] += 1
    if operation == 'acc':
        state['acc'] += amount
        state['adr'] += 1
    if operation == 'jmp':
        state['adr'] += amount
    return state


# Workds for Part 1
def run(instructions: List[Instruction]) -> State:
    state = {'acc': 0, 'adr': 0}
    visited = set()
    i = 0
    while i not in visited and i < len(instructions):
        visited.add(i)
        state = run_instruction(instructions[i], state)
        i = state['adr']
    return state
    # return state['acc']


def swap(instruction: Instruction) -> Instruction:
    op, amt = instruction
    if op == 'nop':
        return ('jmp', amt)
    if op == 'jmp':
        return ('nop', amt)


def swap_at(i: int, instructions: List[Instruction]) -> List[Instruction]:
    newins = instructions.copy()
    newins[i] = swap(newins[i])
    return newins


def fix(instructions: List[Instruction]) -> int:
    nops_and_jmps = [i for (i, (op, _)) in enumerate(
        instructions) if op in ['nop', 'jmp']]
    for i in nops_and_jmps:
        state = run(swap_at(i, instructions))
        if state['adr'] == len(instructions):
            return state['acc']
    return -1


# Apparently much fast version of fix(), since it changes the
# instructions list in place, whereas fix() makes copies
# Tested with %timeit in ipython
def fix2(instructions: List[Instruction]) -> int:
    nops_and_jmps = [i for (i, (op, _)) in enumerate(
        instructions) if op in ['nop', 'jmp']]
    for i in nops_and_jmps:
        instructions[i] = swap(instructions[i])
        state = run(instructions)
        if state['adr'] == len(instructions):
            return state['acc']
        instructions[i] = swap(instructions[i])
    return -1
