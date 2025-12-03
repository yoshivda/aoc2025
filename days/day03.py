import time

from lib import load_input


def solve(data):
    # return part_one(data.splitlines())
    return part_two(data.splitlines())


def part_one(data):
    res = 0
    for line in data:
        first = max(int(x) for x in line[:-1])
        second = max(int(x) for x in line[line.index(str(first)) + 1:])
        res += first * 10 + second
    return res


def part_two(data):
    return sum(int(find_max(line, 0, len(line) - 11)) for line in data)


def find_max(line, start, end):
    index = value = 0
    for i in range(start, end):
        if int(line[i]) > value:
            value = int(line[i])
            index = i
    if end == len(line):
        return str(value)
    return str(value) + find_max(line, index + 1, end + 1)


if __name__ == '__main__':
    print(solve(load_input('small')))
    start = time.time()
    print(solve(load_input()))
    print(time.time() - start)
