ntd = {0: 'E', 1: 'S', 2: 'W', 3: 'N'}
dtn = {'E': 0, 'S': 1, 'W': 2, 'N': 3}

# waypoint = {'N': 1, 'E': 10, 'W': 0, 'S': 0}


def rotate(waypoint, instruction):
    """instruction is like R90, R180, etc"""
    d = instruction[0]
    amount = (int(instruction[1:])//90) % 4
    shift = {1: 3, 2: 2, 3: 1}
    new_waypoint = {}
    for vane in waypoint:
        if d == 'R':
            new_waypoint[vane] = waypoint[ntd[(dtn[vane] + shift[amount]) % 4]]
        if d == 'L':
            new_waypoint[vane] = waypoint[ntd[(dtn[vane] - shift[amount]) % 4]]
    return new_waypoint


def forward(state, waypoint, instruction):
    amount = int(instruction[1:])
    for vane in waypoint:
        vane_amt = waypoint[vane]
        state['dist'][vane] += vane_amt*amount
    return state


def move(waypoint, instruction):
    d = instruction[0]
    amount = int(instruction[1:])
    waypoint[d] += amount
    return waypoint


def manhattan_dist(state):
    E = state['dist']['E']
    S = state['dist']['S']
    W = state['dist']['W']
    N = state['dist']['N']
    return abs((E-W)) + abs((N-S))


def follow_instructions(instructions):
    state = {'dist': {'N': 0, 'E': 0, 'W': 0, 'S': 0}}
    waypoint = {'N': 1, 'E': 10, 'W': 0, 'S': 0}
    for instruction in instructions:
        init = instruction[0]
        if init in ['E', 'S', 'N', 'W']:
            waypoint = move(waypoint, instruction)
        if init in ['L', 'R']:
            waypoint = rotate(waypoint, instruction)
        if init == 'F':
            state = forward(state, waypoint, instruction)
    return manhattan_dist(state), state
