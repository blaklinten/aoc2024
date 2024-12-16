import os
from enum import Enum

part = os.environ.get("part")

MATRIX_LENGTH = 140

class Direction(Enum):
    E = 1
    SE = 2
    S = 3
    SW = 4
    W = 5
    NW = 6
    N = 7
    NE = 8

def get_input():
    with open('./input.txt', 'r') as file:
        return list(''.join([line.strip("\n") for line in file]))

def east(index):
    col = index % MATRIX_LENGTH
    row = index // MATRIX_LENGTH

    n = index + 1
    n_col = n % MATRIX_LENGTH
    n_row = n // MATRIX_LENGTH

    if n_col == col + 1 and n_row == row and n < MATRIX_LENGTH * MATRIX_LENGTH and n > -1:
        return n
    return None

def south_east(index):
    col = index % MATRIX_LENGTH
    row = index // MATRIX_LENGTH

    n = index + 1 + MATRIX_LENGTH
    n_col = n % MATRIX_LENGTH
    n_row = n // MATRIX_LENGTH

    if n_col == col + 1 and n_row == row + 1 and n < MATRIX_LENGTH * MATRIX_LENGTH and n > -1:
        return n
    return None

def south(index):
    col = index % MATRIX_LENGTH
    row = index // MATRIX_LENGTH

    n = index + MATRIX_LENGTH
    n_col = n % MATRIX_LENGTH
    n_row = n // MATRIX_LENGTH

    if n_col == col and n_row == row + 1 and n < MATRIX_LENGTH * MATRIX_LENGTH and n > -1:
        return n
    return None

def south_west(index):
    col = index % MATRIX_LENGTH
    row = index // MATRIX_LENGTH

    n = index + MATRIX_LENGTH - 1
    n_col = n % MATRIX_LENGTH
    n_row = n // MATRIX_LENGTH

    if n_col == col - 1 and n_row == row + 1 and n < MATRIX_LENGTH * MATRIX_LENGTH and n > -1:
        return n
    return None

def west(index):
    col = index % MATRIX_LENGTH
    row = index // MATRIX_LENGTH

    n = index - 1
    n_col = n % MATRIX_LENGTH
    n_row = n // MATRIX_LENGTH

    if n_col == col - 1 and n_row == row and n < MATRIX_LENGTH * MATRIX_LENGTH and n > -1:
        return n
    return None

def north_west(index):
    col = index % MATRIX_LENGTH
    row = index // MATRIX_LENGTH

    n = index - 1 - MATRIX_LENGTH
    n_col = n % MATRIX_LENGTH
    n_row = n // MATRIX_LENGTH

    if n_col == col - 1 and n_row == row - 1 and n < MATRIX_LENGTH * MATRIX_LENGTH and n > -1:
        return n
    return None

def north(index):
    col = index % MATRIX_LENGTH
    row = index // MATRIX_LENGTH

    n = index - MATRIX_LENGTH
    n_col = n % MATRIX_LENGTH
    n_row = n // MATRIX_LENGTH

    if n_col == col and n_row == row - 1 and n < MATRIX_LENGTH * MATRIX_LENGTH and n > -1:
        return n
    return None

def north_east(index):
    col = index % MATRIX_LENGTH
    row = index // MATRIX_LENGTH

    n = index + 1 - MATRIX_LENGTH
    n_col = n % MATRIX_LENGTH
    n_row = n // MATRIX_LENGTH

    if n_col == col + 1 and n_row == row - 1 and n < MATRIX_LENGTH * MATRIX_LENGTH and n > -1:
        return n
    return None

def create_neighbour_map():
    neighbours = [{} for _ in range(MATRIX_LENGTH*MATRIX_LENGTH)]

    for index  in range(MATRIX_LENGTH * MATRIX_LENGTH):
        east_neighbour = east(index)
        if east_neighbour is not None:
            neighbours[index][Direction.E] = east_neighbour

        south_east_neighbour = south_east(index)
        if south_east_neighbour is not None:
            neighbours[index][Direction.SE] = south_east_neighbour

        south_neighbour = south(index)
        if south_neighbour is not None:
            neighbours[index][Direction.S] = south_neighbour

        south_west_neighbour = south_west(index)
        if south_west_neighbour is not None:
            neighbours[index][Direction.SW] = south_west_neighbour

        west_neighbour = west(index)
        if west_neighbour is not None:
            neighbours[index][Direction.W] = west_neighbour

        north_west_neighbour = north_west(index)
        if north_west_neighbour is not None:
            neighbours[index][Direction.NW] = north_west_neighbour

        nort_neighbour = north(index)
        if nort_neighbour is not None:
            neighbours[index][Direction.N] = nort_neighbour

        nort_east_neighbour = north_east(index)
        if nort_east_neighbour is not None:
            neighbours[index][Direction.NE] = nort_east_neighbour

    return neighbours

def is_XMAS(index, dir, neighbours, input) -> bool:
    maybe_M = neighbours[index].get(dir)
    if maybe_M is not None and input[maybe_M] == 'M':
        maybe_A = neighbours[maybe_M].get(dir)
        if maybe_A is not None and input[maybe_A] == 'A':
            maybe_S = neighbours[maybe_A].get(dir)
            if maybe_S is not None and input[maybe_S] == 'S':
                return True
    return False

def solve1(input) -> int:
    xmas_count = 0

    neighbours_map = create_neighbour_map()
    xs = []
    for index, char in enumerate(input):
        if char == 'X':
            xs.append(index)

    for x in xs:
        for direction in Direction.E, Direction.SE, Direction.S, Direction.SW, Direction.W, Direction.NW, Direction.N, Direction.NE:
            if is_XMAS(x, direction, neighbours_map, input):
                xmas_count += 1
    return xmas_count

def is_X_MAS(index, neighbours, input) -> bool:
    SE_neighbour = neighbours[index].get(Direction.SE)
    SW_neighbour = neighbours[index].get(Direction.SW)
    NE_neighbour = neighbours[index].get(Direction.NE)
    NW_neighbour = neighbours[index].get(Direction.NW)
    if SE_neighbour is None or SW_neighbour is None or NE_neighbour is None or NW_neighbour is None:
        return False

    SE_X_MAS = input[SE_neighbour] == "M" and input[NW_neighbour] == "S"
    SW_X_MAS = input[SW_neighbour] == "M" and input[NE_neighbour] == "S"
    NE_X_MAS = input[NE_neighbour] == "M" and input[SW_neighbour] == "S"
    NW_X_MAS = input[NW_neighbour] == "M" and input[SE_neighbour] == "S"

    return (SE_X_MAS or NW_X_MAS) and (SW_X_MAS or NE_X_MAS)

def solve2(input):
    x_mas_count = 0

    neighbours_map = create_neighbour_map()
    a_s = []
    for index, char in enumerate(input):
        if char == 'A':
            a_s.append(index)

    for a in a_s:
        if is_X_MAS(a, neighbours_map, input):
            x_mas_count += 1
    return x_mas_count

if part == "part1":
    count = solve1(get_input())
    print(count)


elif part == "part2":
    count = solve2(get_input())
    print(count)
