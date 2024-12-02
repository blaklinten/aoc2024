import os

part = os.environ.get("part")

def get_input():
    with open('./input.txt', 'r') as file:
        return [[int(level) for level in report.split()] for report in file]

def allowed_diff(first, second) -> bool:
    diff = abs(first - second)
    if diff > 3 or diff < 1:
        return False
    return True


def is_safe1(report) -> int:
    first_level = report[0]
    second_level = report[1]
    if not allowed_diff(first_level, second_level):
        return 0

    incdec = first_level < second_level
    for index, level in enumerate(report):
        if index == 0 or index == 1:
            continue

        previous = report[index - 1]
        if not (allowed_diff(level, previous) and (previous < level) == incdec):
            return 0
    return 1

def is_safe2(report) -> int:
    return 1

def solve1(input):
    report_status = [is_safe1(report) for report in input ]
    print(sum(report_status))
        


def solve2(input):
    report_status = [is_safe2(report) for report in input ]
    print(sum(report_status))

if part == "part1":
    solve1(get_input())


elif part == "part2":
    solve2(get_input())
