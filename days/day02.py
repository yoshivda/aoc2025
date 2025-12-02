import re
import time

from lib import load_input


def solve(data):
    # return part_one(data.split(','))
    return part_two(data.split(','))


def part_one(data):
    return sum(x for line in data for x in range(int(line.split('-')[0]), int(line.split('-')[1]) + 1) if re.match(r'^(\d+)\1$', str(x)))


def part_two(data):
    return sum(x for line in data for x in range(int(line.split('-')[0]), int(line.split('-')[1]) + 1) if re.match(r'^(\d+)(?:\1){1,}$', str(x)))


if __name__ == '__main__':
    print(solve(load_input('small')))
    start = time.time()
    print(solve(load_input()))
    print(time.time() - start)
