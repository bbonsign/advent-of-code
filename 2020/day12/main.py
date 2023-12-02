
num_to_dir = {0: 'E', 1: 'S', 2: 'W', 3: 'N'}


def rotate(state, instruction):
    """instruction is like R90, R180, etc"""
    d = instruction[0]
    degrees = int(instruction[1:])
    if d == 'R':
        state['dir'] = (state['dir'] + (degrees//90)) % 4
    if d == 'L':
        state['dir'] = (state['dir'] - (degrees//90)) % 4
    return state


def forward(state, instruction):
    amount = int(instruction[1:])
    d = num_to_dir[state['dir']]
    state['dist'][d] += amount
    return state


def move(state, instruction):
    d = instruction[0]
    amount = int(instruction[1:])
    state['dist'][d] += amount
    return state


def manhattan_dist(state):
    E = state['dist']['E']
    S = state['dist']['S']
    W = state['dist']['W']
    N = state['dist']['N']
    return abs((E-W)) + abs((N-S))


def follow_instructions(instructions):
    state = {'dist': {'N': 0, 'E': 0, 'W': 0, 'S': 0}, 'dir': 0}
    for instruction in instructions:
        init = instruction[0]
        if init in ['E', 'S', 'N', 'W']:
            state = move(state, instruction)
        if init in ['L', 'R']:
            state = rotate(state, instruction)
        if init == 'F':
            state = forward(state, instruction)
    return manhattan_dist(state), state
