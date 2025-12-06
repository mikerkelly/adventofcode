import sys


def readlines():
    with open(sys.argv[1]) as f:
        return f.read().splitlines()


def preprocess(lines):
    print(lines)
    return [(line[0], int(line[1:])) for line in lines if line[0]]


def part1(lines):
    print(lines)
    pos = 50
    pw = 0
    print(pos)
    for op, num in lines:
        print(op)
        print(num)
        if op == "L":
            res = pos - num
        elif op == "R":
            res = pos + num
        pos = res % 100
        if pos == 0:
            pw += 1
            print(f"={pw}")
        print(pos)

    print(f"={pw}")

    return


def part2(lines):
    print(lines)
    pos = 50
    pw = 0
    for op, num in lines:
        print(pos, op, num, pw)
        if op == "L":
            res = pos - num
        elif op == "R":
            res = pos + num

        print(res)
        pw += abs((res - (1 if res < 1 else 0)) // 100)
        if pos == 0 and res < 0:
            pw -= 1
        pos = res % 100
    return (pos, pw)


lines = preprocess(readlines())
print(part1(lines))
print(part2(lines))
