import sys
from collections import Counter
import operator


def readlines():
    with open(sys.argv[1]) as f:
        return f.read().splitlines()


def preprocess(lines):
    sp = [line.split() for line in lines]
    firsts, seconds = [item for item in zip(*[line.split() for line in lines])]
    return firsts, seconds


def part1(firsts, seconds):
    pairs = zip(
        sorted(int(item) for item in firsts),
        sorted(int(item) for item in seconds)
    )
    return sum(abs(pair[0] - pair[1]) for pair in pairs)


def part2(firsts, seconds):
    counts = Counter(seconds)
    return sum(int(elem) * int(counts[elem]) for elem in firsts)


firsts, seconds = preprocess(readlines())
print(part1(firsts, seconds))
print(part2(firsts, seconds))
