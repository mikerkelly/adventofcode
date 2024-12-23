import sys
from collections import defaultdict


def readlines():
    with open(sys.argv[1]) as f:
        return f.read().splitlines()


def preprocess(lines):
    return [line.split("-") for line in lines]


def get_links(lines):
    links_of = defaultdict(list)
    for line in lines:
        links_of[line[0]].append(line[1])
        links_of[line[1]].append(line[0])
    return links_of


def get_triplets(links_of):
    triplets = set()
    for left in links_of:
        for middle in links_of[left]:
            for right in links_of[middle]:
                if right in links_of[left]:
                    triplet = tuple(sorted([left, right, middle]))
                    triplets.add(triplet)
    return triplets


def part1(lines):
    links_of = get_links(lines)
    triplets = get_triplets(links_of)
    return len(
        [
            triplet
            for triplet in triplets
            if any(name.startswith("t") for name in triplet)
        ]
    )


def part2(lines):
    links_of = get_links(lines)
    triplets = get_triplets(links_of)
    biggest_sets = triplets

    while len(biggest_sets) > 1:
        new_biggest_sets = set()
        for linked_set in biggest_sets:
            for name in linked_set:
                for link in links_of[name]:
                    if all(link in links_of[item] for item in linked_set):
                        new_list = list(linked_set)
                        new_list.append(link)
                        new_list.sort()
                        new_biggest_sets.add(tuple(new_list))
        biggest_sets = new_biggest_sets
        print(biggest_sets)

    return ",".join(biggest_sets.pop())


lines = preprocess(readlines())
print(part1(lines))
print(part2(lines))
