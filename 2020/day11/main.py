from typing import List
from copy import deepcopy


def count_filled(pattern: str) -> int:
    return len([c for c in pattern if c == '#'])


def get_neighbors(idx: int, pattern: str) -> List[str]:
    lines = pattern.splitlines()
    rows = len(lines)
    cols = len(lines[0])
    idx_row = idx // rows
    idx_col = idx % cols
    offsets = [-1, 0, 1]

    row_idxs = [i for o in offsets if (0 <= (i := idx_row+o) < rows)]
    col_idxs = [i for o in offsets if (0 <= (i := idx_col+o) < cols)]
    # print((idx_row, idx_col), row_idxs, col_idxs)
    neighbors = [lines[j][i] for i in col_idxs
                 for j in row_idxs if (j, i) != (idx_row, idx_col)]
    return neighbors


def step(pattern: str) -> str:
    split_pattern = [[char for char in row] for row in pattern.splitlines()]
    copy = deepcopy(split_pattern)
    for row_idx, row in enumerate(copy):
        for col_idx, char in enumerate(row):
            idx = row_idx*len(row) + col_idx
            neighbor_count = count_filled(''.join(get_neighbors(idx, pattern)))
            if char == 'L' and neighbor_count == 0:
                copy[row_idx][col_idx] = '#'
            if char == '#' and neighbor_count >= 4:
                copy[row_idx][col_idx] = 'L'
    new_pattern = ''.join([''.join(row+['\n']) for row in copy])
    return new_pattern


def fill_seats(pattern: str) -> int:
    old = ''
    new = pattern
    while old != new:
        old = new
        new = step(old)
    return count_filled(new)
