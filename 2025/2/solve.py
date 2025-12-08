import sys


def readlines():
    with open(sys.argv[1]) as f:
        return f.read().splitlines()


def preprocess(lines):
    return [
        (int(first), int(last))
        for (first, last) in [pair.split("-") for pair in lines[0].split(",")]
    ]


def equal_len_ranges(ranges):
    for first, last in ranges:
        start = first
        end = 0
        while end < last:
            next_999 = 10 ** (len(str(start))) - 1
            # unhandled edge case where start = next_999?
            end = min(last, next_999)
            yield ((start, end), (str(start), str(end)))
            start = end + 1


def invalids_sum(start_int, end_int, start_str, end_str, num_chunks):
    # print(start_int, end_int, start_str, end_str, num_chunks)
    len_range = len(start_str)
    if len_range % num_chunks != 0:
        return []

    len_chunks = len_range // num_chunks
    start_first_chunk = start_str[:len_chunks]
    end_first_chunk = end_str[:len_chunks]

    repeats = [
        int(str(pattern) * num_chunks)
        for pattern in range(int(start_first_chunk), 1 + int(end_first_chunk))
    ]

    return [rep for rep in repeats if start_int <= rep <= end_int]


def solve(ranges, fixed_num_chunks=None):
    repeats = set()
    for (start_int, end_int), (start_str, end_str) in equal_len_ranges(ranges):
        # print((start_int, end_int), (start_str, end_str))
        for num_chunks in fixed_num_chunks or range(2, len(end_str) + 1):
            to_add = invalids_sum(start_int, end_int, start_str, end_str, num_chunks)
            for repeat in to_add:
                repeats.add(repeat)
    # print(sorted(list(repeats)))
    return sum(repeats)


def part1(ranges):
    return solve(ranges, (2,))


def part2(ranges):
    return solve(ranges)


lines = preprocess(readlines())
print(part1(lines))
print(part2(lines))
