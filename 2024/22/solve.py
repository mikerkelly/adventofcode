import sys


def readlines():
    with open(sys.argv[1]) as f:
        return f.read().splitlines()


def preprocess(lines):
    return [int(line) for line in lines]


def mix(a, b):
    return a ^ b


def prune(a):
    return a % 16777216


def next_secret(num):
    num = prune(mix(num, num * 64))
    num = prune(mix(num, num // 32))
    return prune(mix(num, num * 2048))


def part1(lines, length):
    total = 0
    for line in lines:
        for _ in range(length):
            line = next_secret(line)
        total += line
    return total


def part2(lines, length):
    seq_prices = {}
    for secret in lines:
        secrets = [secret] + [secret := next_secret(secret) for _ in range(length- 1)]
        prices = [secret % 10 for secret in secrets]
        moves = [prices[1:][ii] - prices[ii] for ii in range(len(prices)-1)]

        seqs_seen = set()
        for index in range(len(prices) - 4):
            seq = tuple(moves[index : index + 4])
            if seq not in seqs_seen:
                seq_prices[seq] = seq_prices.get(seq, 0) + prices[index + 4]
                seqs_seen.add(seq)

    return seq_prices[max(seq_prices, key=seq_prices.get)]


lines = preprocess(readlines())
length = 2000
print(part1(lines, length))
print(part2(lines, length))
