import re
import copy
from typing import Pattern


def get_head_of_stacks(stacks):
    final_head_of_stacks = ""
    for stack in stacks:
        if len(stack) != 0:
            final_head_of_stacks += stack[0]
    return final_head_of_stacks


def move_crates(regex: Pattern[str], text: str, input_stacks: list[list[str]],
                version: int):
    stacks = copy.deepcopy(input_stacks)
    for line in text:
        match = regex.match(line)
        if match:
            number_of_crates_to_move = int(match[1])
            from_stack = int(match[2])
            to_stack = int(match[3])
            if version == 1:
                stacks = move_crates_1(number_of_crates_to_move, from_stack,
                                       to_stack, stacks)
            elif version == 2:
                stacks = move_crates_2(number_of_crates_to_move, from_stack,
                                       to_stack, stacks)
    return stacks


def move_crates_1(number_of_crates_to_move: int, from_stack: int,
                  to_stack: int, stacks: list[list[str]]):
    for i in range(0, number_of_crates_to_move):
        if len(stacks[from_stack]) != 0:
            temp = stacks[from_stack].pop(0)
            stacks[to_stack].insert(0, temp)
    return stacks


def move_crates_2(number_of_crates_to_move: int, from_stack: int,
                  to_stack: int, stacks: list[list[str]]):
    if len(stacks[from_stack]) != 0:
        temp = stacks[from_stack][0:number_of_crates_to_move]
        stacks[from_stack] = stacks[from_stack][number_of_crates_to_move:]
        stacks[to_stack] = temp + stacks[to_stack]
    return stacks


sample_stacks = [[], ["N", "Z"], ["D", "C", "M"], ["P"]]
puzzle_stacks = [
    [],
    ["F", "H", "M", "T", "V", "L", "D"],
    ["P", "N", "T", "C", "J", "G", "Q", "H"],
    ["H", "P", "N", "D", "S", "R"],
    ["F", "V", "B", "L"],
    ["Q", "L", "G", "H", "N"],
    ["P", "M", "R", "G", "D", "B", "W"],
    ["Q", "R", "H", "C", "R", "N", "M", "G"],
    ["W", "L", "C"],
    ["T", "M", "Z", "J", "Q", "L", "D", "R"],
]
input = open("input.txt", "r", encoding="utf-8")
text = input.read().split("\n")
move_pattern = r"move (\d+) from (\d+) to (\d+)"
move_regex = re.compile(move_pattern)
input_stack = puzzle_stacks

# Part 1
stacks = move_crates(move_regex, text, input_stack, 1)
print(get_head_of_stacks(stacks))

# Part 2
stacks = move_crates(move_regex, text, input_stack, 2)
print(get_head_of_stacks(stacks))