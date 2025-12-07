import time
from functools import cache

from lib import load_input


def solve(data):
    # return part_one(data.splitlines())
    return part_two(data.splitlines())


def part_one(data):
    beams = {next((x, y) for x in range(len(data[0])) for y in range(len(data)) if data[y][x] == 'S')}

    splits = set()
    while beams:
        new_beams = set()
        for x, y in beams:
            if y >= len(data):
                continue
            if data[y][x] == '^':
                if (x, y) not in splits:
                    splits.add((x, y))
                    new_beams.add((x - 1, y))
                    new_beams.add((x + 1, y))
            else:
                new_beams.add((x, y + 1))
        beams = new_beams
    return len(splits)


def part_two(data):

    @cache
    def paths_from(x, y):
        if y == len(data):
            return 1
        if data[y][x] == '^':
            return paths_from(x - 1, y) + paths_from(x + 1, y)
        return paths_from(x, y + 1)

    return paths_from(*next((x, y) for x in range(len(data[0])) for y in range(len(data)) if data[y][x] == 'S'))

if __name__ == '__main__':
    print(solve(load_input('small')))
    start = time.time()
    print(solve(load_input()))
    print(time.time() - start)
