import time
from functools import reduce

from lib import load_input


def solve(data):
    # return part_one(data.splitlines())
    return part_two(data.splitlines())


def part_one(data):
    return len({(x, y) for (x, y) in rolls \
                if len({(x + dx, y + dy) for dx in range(-1, 2) for dy in range(-1, 2) if (dx != 0 or dy != 0) and (x + dx, y + dy) in rolls}) < 4}) \
        if (rolls := {(x, y) for x in range(len(data[0])) for y in range(len(data)) if data[y][x] == '@'}) else 0


def part_two(data):
    return ((y := lambda self, res, rolls: self(self, res + len(can_remove), rolls - can_remove)
            if len(can_remove := {(x, y) for (x, y) in rolls if len({(x + dx, y + dy) for dx in range(-1, 2) for dy in range(-1, 2) if (dx != 0 or dy != 0) and (x + dx, y + dy) in rolls}) < 4}) > 0
            else res)
        (y, 0, {(x, y) for x in range(len(data[0])) for y in range(len(data)) if data[y][x] == '@'}))


if __name__ == '__main__':
    print(solve(load_input('small')))
    start = time.time()
    print(solve(load_input()))
    print(time.time() - start)
