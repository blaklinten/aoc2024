import os
from itertools import combinations

part = os.environ.get("part")

def get_input():
        return [[line for line in input.split('\n') if line] for input in file.read().split('\n\n')]

def solve1(input):
    bad_orderings = [tuple([num for num in rule.split('|')[::-1]]) for rule in input[0]]
    pair_list = [[pair for pair in combinations(page_order.split(','), 2)] for page_order in input[1]]
    illegal_ordering = [[page_ordering[0] for page_ordering in enumerate(pairs) if page_ordering[1] in bad_orderings] for pairs in pair_list]
    middle_legal_page = [int(pages[1].split(',')[len(pages[1].split(','))//2]) for pages in enumerate(input[1]) if not illegal_ordering[pages[0]]]
    print(sum(middle_legal_page))

if part == "part1":
    solve1(get_input())


elif part == "part2":
    print("Part 2")
    # solve2(get_input())
