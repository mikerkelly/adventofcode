import sys
import re

pattern = r"mul\((\d+),(\d+)\)"


def readline():
    with open(sys.argv[1]) as f:
        return f.read()


def mul(pair):
    return int(pair[0]) * int(pair[1])


def part1(line):
    matches = re.findall(pattern, line)
    return sum(mul(pair) for pair in matches)


do_dont_pattern = r"(mul\(\d+,\d+\))|(do\(\))|(don't\(\))"


def part2(line):
    matches = re.findall(do_dont_pattern, line)
    enabled = True
    sum = 0
    for hit in matches:
        if hit[0] and enabled:
            sub_match = re.search(pattern, hit[0])
            sum += mul((sub_match[1], sub_match[2]))
        elif hit[1]:
            enabled = True
        elif hit[2]:
            enabled = False

    return sum


line = readline()
print(part1(line))
print(part2(line))
