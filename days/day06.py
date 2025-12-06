import math
import re
import time

from lib import load_input
from math import prod


def solve(data):
    # return part_one(data.splitlines())
    return part_two(data.splitlines())


def part_one(data):
    nums = [[int(x) for x in re.split(r' +', line.strip())] for line in data[:-1]]
    ops = list(map(lambda op: prod if op == '*' else sum, re.split(r' +', data[-1].strip())))
    return sum(ops[i](nums[j][i] for j in range(len(nums))) for i in range(len(ops)))


def part_two(data):
    max_len = max(len(row) for row in data)
    line = [''.join(data[y][i] if i < len(data[y]) and data[y][i] != ' ' else '' for y in range(len(data))) for i in range(max_len)]
    for i in range(1, len(line) - 1):
        line[i] = '+' if line[i] == '' else line[i] + line[i - 1][-1] if len(line[i - 1]) > 1 and line[i + 1] != '' else line[i]
    return eval(''.join(line))



if __name__ == '__main__':
    print(solve(load_input('small')))
    start = time.time()
    print(solve(load_input()))
    print(time.time() - start)
