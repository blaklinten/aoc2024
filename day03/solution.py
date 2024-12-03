import os
import re

part = os.environ.get("part")

def get_input():
    with open('./input.txt', 'r') as file:
        return ''.join([line.strip("/n") for line in file])



def solve1(input):
    mul_exp = re.compile(r"mul\([\d]{1,3},[\d]{1,3}\)")
    matches = ' '.join(mul_exp.findall(input))
    filter = re.compile(r"[\d]{1,3},[\d]{1,3}")
    factors = filter.findall(matches)
    products = [int(a) * int(b) for pair in factors for a, b in [pair.split(',')]]
    print(sum(products))

def solve2(input):
    collection = {}

    mul_exp = re.compile(r"mul\([\d]{1,3},[\d]{1,3}\)")
    mul_matches = mul_exp.findall(input)
    for mul in mul_matches:
        collection[input.index(mul)] = mul

    index = 0
    while True:
        index = input.find(r"do()", index)
        if index == -1:
            break
        collection[index] = "do()"
        index += 1

    index = 0
    while True:
        index = input.find(r"don't()", index)
        if index == -1:
            break
        collection[index] = "dont()"
        index += 1

    do_dont = True
    filter = re.compile(r"[\d]{1,3},[\d]{1,3}")
    factors = []
    for index in sorted(collection.keys()):
        action = collection[index]
        if action == r"do()":
            do_dont = True
        elif action == r"dont()":
            do_dont = False
        else:
            if do_dont:
                factors.append(filter.findall(action))

    products = [int(a) * int(b) for pair in factors for a, b in (pair[0].split(','),)]
    print(sum(products))

if part == "part1":
    solve1(get_input())


elif part == "part2":
    solve2(get_input())
