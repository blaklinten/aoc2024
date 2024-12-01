import os

part = os.environ.get("part")

def get_input():
    with open('./input.txt', 'r') as file:
        lines = file.readlines()
        return ([int(line.split()[0]) for line in lines], [int(line.split()[1]) for line in lines])

def solve1(input):
    individual_distances = [abs(left - right) for left, right in zip(sorted(input[0]), sorted(input[1]))]
    total_distance = sum(individual_distances)
    print(total_distance)

def solve2(input):
    offset = 0
    score = 0
    multiplier = 1
    right = sorted(input[1])
    left = sorted(input[0])

    for index in range(len(left)):
        if index + offset > len(right):
            print(score)
            return
        if left[index] < right[index + offset]:
            offset -= 1
            continue
        while left[index] > right[index + offset]:
            offset += 1
            if index + offset >= len(right):
                print(score)
                return
            continue
        if left[index] == right[index + offset] and index + 1 < len(left) and left[index + 1] == right[index + offset]:
            multiplier += 1
            offset -= 1
            continue
        while left[index] == right[index + offset]:
            score += multiplier * left[index]
            offset += 1
            if offset > len(right):
                print(score)
                return
        multiplier = 1 
        offset -= 1
    print(score)

if part == "part1":
    solve1(get_input())


elif part == "part2":
    solve2(get_input())
