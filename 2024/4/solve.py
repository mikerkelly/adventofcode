import sys


def readlines():
    with open(sys.argv[1]) as f:
        return f.read().splitlines()


def part1(lines):
    target = "XMAS"
    targets = {target, target[::-1]}

    target_length = len(target)
    target_range = range(target_length)
    row_length = len(lines[0])
    col_length = len(lines)

    transpose = ["".join(item) for item in zip(*lines)]

    total = 0
    for index_y in range(col_length):
        for index_x in range(row_length):
            # horizontal
            if index_x <= row_length - target_length:
                if lines[index_y][index_x : index_x + target_length] in targets:
                    total += 1

            # vertical
            if index_y <= col_length - target_length:
                if transpose[index_x][index_y : index_y + target_length] in targets:
                    total += 1

            if index_y <= col_length - target_length:
                # diagonal down right
                if index_x <= row_length - target_length:
                    diag = ""
                    for inc in target_range:
                        diag += lines[index_y + inc][index_x + inc]
                    if diag in targets:
                        total += 1
                # diagonal down left
                if index_x + 1 >= target_length:
                    diag = ""
                    for inc in target_range:
                        diag += lines[index_y + inc][index_x - inc]
                    if diag in targets:
                        total += 1

    return total


def part2(lines):
    target = "MAS"
    targets = {target, target[::-1]}

    target_length = len(target)
    row_length = len(lines[0])
    col_length = len(lines)

    total = 0
    for index_y in range(col_length - target_length + 1):
        for index_x in range(row_length - target_length + 1):
            right_diag = "".join(
                [
                    lines[index_y + 0][index_x + 0],
                    lines[index_y + 1][index_x + 1],
                    lines[index_y + 2][index_x + 2],
                ]
            )
            if right_diag in targets:
                left_diag = "".join(
                    [
                        lines[index_y + 2][index_x],
                        lines[index_y + 1][index_x + 1],
                        lines[index_y + 0][index_x + 2],
                    ]
                )
                if left_diag in targets:
                    total += 1

    return total


lines = readlines()
print(part1(lines))
print(part2(lines))
