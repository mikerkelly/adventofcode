import sys
from collections import Counter


def readlines():
    with open(sys.argv[1]) as f:
        return f.read().splitlines()


def preprocess(lines):
    return [[int(elem) for elem in line.split()] for line in lines]


ascending_diffs = {1, 2, 3}
descending_diffs = {-1, -2, -3}


def diff(level):
    return [level[index + 1] - level[index] for index in range(len(level) - 1)]


def safe(level):
    diffs = set(diff(level))
    return (
        1
        if (diffs.issubset(ascending_diffs) or diffs.issubset(descending_diffs))
        else 0
    )


def list_without_index(the_list, index):
    list_copy = the_list.copy()
    del list_copy[index]
    return list_copy


def safe_when_damp(level):
    for index in range(len(level)):
        if safe(list_without_index(level, index)):
            return 1
    return 0


def part1(lines):
    return sum(safe(level) for level in lines)


def part2(lines):
    return sum(safe_when_damp(level) for level in lines)


lines = preprocess(readlines())
print(part1(lines))
print(part2(lines))
