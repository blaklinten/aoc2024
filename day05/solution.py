import os
from itertools import combinations

part = os.environ.get("part")

def get_input():
    with open('./input.txt', 'r') as file:
        return [[line for line in input.split('\n') if line] for input in file.read().split('\n\n')]

def solve1(input):
    bad_orderings = [tuple([num for num in rule.split('|')[::-1]]) for rule in input[0]]
    pair_list = [[pair for pair in combinations(page_order.split(','), 2)] for page_order in input[1]]
    illegal_ordering = [[page_ordering[0] for page_ordering in enumerate(pairs) if page_ordering[1] in bad_orderings] for pairs in pair_list]
    middle_legal_page = [int(pages[1].split(',')[len(pages[1].split(','))//2]) for pages in enumerate(input[1]) if not illegal_ordering[pages[0]]]
    print(sum(middle_legal_page))

def correct(page_order, bad_rules):
    pair_list = [pair for pair in combinations(page_order, 2)]

    illegal_ordering = [pair for pair in pair_list if pair in bad_rules]
    while illegal_ordering:
        index_pair_1 = page_order.index(illegal_ordering[0][0])
        index_pair_2 = page_order.index(illegal_ordering[0][1])

        tmp = page_order[index_pair_1]
        page_order[index_pair_1] = page_order[index_pair_2]
        page_order[index_pair_2] = tmp

        pair_list = [pair for pair in combinations(page_order, 2)]
        illegal_ordering = [pair for pair in pair_list if pair in bad_rules]

    return page_order


def solve2(input):
    bad_rules = [tuple([num for num in rule.split('|')[::-1]]) for rule in input[0]]
    all_pairs = [
            [pair for pair in combinations(page_order.split(','), 2)]
            for page_order in input[1]]
    index_illegal_pairs = [
            [pair for pair in enumerate(pairs) if pair[1] in bad_rules]
            for pairs in all_pairs ]
    corrected = [
            correct([ordering for ordering in input[1][index[0]].split(',')], bad_rules)
            for index in enumerate(index_illegal_pairs) if index[1]]
    middle_legal_page = [int(pages[len(pages)//2]) for pages in corrected]
    print(sum(middle_legal_page))

if part == "part1":
    solve1(get_input())


elif part == "part2":
    solve2(get_input())
