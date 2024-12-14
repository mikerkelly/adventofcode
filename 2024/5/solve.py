import sys
from collections import defaultdict


def readlines():
    with open(sys.argv[1]) as f:
        return f.read().splitlines()


def preprocess(lines):
    global earlier_pages
    earlier_pages = defaultdict(list)
    for index, line in enumerate(lines):
        if not line:
            break
        tokens = line.split("|")
        before = int(tokens[0])
        after = int(tokens[1])
        # a|b: if a,b in list, a before b
        #   => if b in list, a NOT after b
        earlier_pages[after].append(before)

    to_check = [[int(val) for val in line.split(",")] for line in lines[index + 1 :]]

    return to_check


def mid_if_valid_order(check_me):
    later_items = set(check_me)
    for elem in check_me:
        for not_after in earlier_pages[elem]:
            if not_after in later_items:
                return 0
        later_items.remove(elem)

    return check_me[len(check_me) // 2]


def part1(to_check):
    return sum(mid_if_valid_order(check) for check in to_check)


def mid_after_fixing(pages):
    page_set = set(pages)
    remaining_pages_before = {
        later_page: {
            earlier_page
            for earlier_page in earlier_pages[later_page]
            if earlier_page in page_set
        }
        for later_page in page_set
    }

    mid_index = len(page_set) // 2
    pages_sorted = 0
    while pages_sorted <= mid_index:
        for current_page, later_pages in remaining_pages_before.items():
            if not later_pages:
                break

        del remaining_pages_before[current_page]
        for later_pages in remaining_pages_before.values():
            later_pages.discard(current_page)

        pages_sorted += 1
    return current_page


def part2(lines):
    invalid = [check for check in to_check if not mid_if_valid_order(check)]
    return sum(mid_after_fixing(pages) for pages in invalid)


to_check = preprocess(readlines())
print(part1(to_check))
print(part2(to_check))
