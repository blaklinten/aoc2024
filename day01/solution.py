import os
from collections import Counter

part = os.environ.get("part")

def get_input():
    with open('./input.txt', 'r') as file:
        # Thanks to Rembane for this elegant solution to skip double iterators and teaching me about splat operator :D
        return list(zip(*[[int(col) for col in line.split()] for line in file]))

def solve1(input):
    individual_distances = [abs(left - right) for left, right in zip(sorted(input[0]), sorted(input[1]))]
    total_distance = sum(individual_distances)
    print(total_distance)

def solve2(input):
    # Also thanks Rembane for showing me the Counter class and guide me on how to use it
    counter = Counter(input[1])
    score = sum([value * counter[value] for value in input[0]])
    print(score)

if part == "part1":
    solve1(get_input())


elif part == "part2":
    solve2(get_input())
