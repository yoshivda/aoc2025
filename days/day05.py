import time

from lib import load_input


def solve(data):
    # return part_one(data.split('\n\n'))
    return part_two(data.split('\n\n'))


def part_one(data):
    return sum(any(a <= num <= b for (a, b) in [tuple(map(int, line.split('-'))) for line in data[0].splitlines()]) for num in map(int, data[1].splitlines()))


def part_two(data):
    ranges = sorted([list(map(int, line.split('-'))) for line in data[0].splitlines()])
    new_ranges = []
    a, b = ranges[0]
    for c, d in ranges[1:]:
        if a <= c <= b or a <= d <= b:
            a = min(a, c)
            b = max(b, d)
        else:
            new_ranges.append((a, b))
            a, b = c, d
    new_ranges.append((a, b))
    return sum(b - a + 1 for (a, b) in new_ranges)


if __name__ == '__main__':
    print(solve(load_input('small')))
    start = time.time()
    print(solve(load_input()))
    print(time.time() - start)
