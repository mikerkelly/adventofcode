import sys


def readlines():
    with open(sys.argv[1]) as f:
        return f.read().splitlines()


def preprocess(lines):
    return [line.split() for line in lines]


def part1(lines):
    for line in lines:
        print(line)
    return


def part2(lines):
    return


lines = preprocess(readlines())
print(part1(lines))
print(part2(lines))
