import os
from collections import Counter

part = os.environ.get("part")

def get_input():
    with open('./input.txt', 'r') as file:
        return list(zip(*[[int(col) for col in line.split()] for line in file]))

def solve1(input):
    individual_distances = [abs(left - right) for left, right in zip(sorted(input[0]), sorted(input[1]))]
    total_distance = sum(individual_distances)
    print(total_distance)

def solve2(input):
    counter = Counter(input[1])
    score = sum([value * counter[value] for value in input[0]])
    print(score)

if part == "part1":
    solve1(get_input())


elif part == "part2":
    solve2(get_input())
