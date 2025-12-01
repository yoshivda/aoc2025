import time

from lib import load_input


def solve(data):
    # return part_one(data.splitlines())
    return part_two(data.splitlines())


def part_one(data):
    i = 50
    res = 0
    for line in data:
        steps = int(line[1:])
        if line[0] == 'R':
            i += steps
        else:
            i -= steps
        i %= 100
        if i == 0:
            res += 1
    return res


def part_two(data):
    i = 50
    res = 0
    direction = ''
    for line in data:

        # from pos to pos: steps on 0
        if line[0] == 'R' and direction == 'L' and i == 0:
            res += 1
        # from neg to neg: counted twice
        elif line[0] == 'L' and direction == 'R' and i == 0:
            res -= 1
        direction = line[0]

        steps = int(line[1:])
        if line[0] == 'R':
            i += steps
        else:
            i -= steps

        if i < 0 or i > 99:
            res += abs(i // 100)
            i %= 100

    return res


if __name__ == '__main__':
    print(solve(load_input('small')))
    start = time.time()
    print(solve(load_input()))
    print(time.time() - start)
