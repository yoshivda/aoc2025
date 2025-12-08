import time
from math import sqrt, prod

from lib import load_input


def solve(data):
    # return part_one(data.splitlines())
    return part_two(data.splitlines())


def part_one(data):
    points = [tuple(map(int, line.split(','))) for line in data]
    dists = list()
    for a in points:
        for b in points:
            if a < b:
                dists.append((sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2), a, b))
    dists.sort()
    circuits = [{p} for p in points]
    for i, (dist, a, b) in enumerate(dists):
        if i == (10 if len(points) == 20 else 1000):
            return prod(sorted([len(circuit) for circuit in circuits])[-3:])
        a_circ = next(a_circ for a_circ in circuits if a in a_circ)
        if b in a_circ:
            continue
        b_circ = next(b_circ for b_circ in circuits if b in b_circ)
        circuits.remove(b_circ)
        a_circ |= b_circ


def part_two(data):
    points = [tuple(map(int, line.split(','))) for line in data]
    dists = list()
    for a in points:
        for b in points:
            if a < b:
                dists.append((sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2), a, b))
    dists.sort()
    circuits = [{p} for p in points]
    for i, (dist, a, b) in enumerate(dists):
        a_circ = next(a_circ for a_circ in circuits if a in a_circ)
        if b in a_circ:
            continue
        b_circ = next(b_circ for b_circ in circuits if b in b_circ)
        circuits.remove(b_circ)
        a_circ |= b_circ
        if len(circuits) == 1:
            return a[0] * b[0]

if __name__ == '__main__':
    print(solve(load_input('small')))
    start = time.time()
    print(solve(load_input()))
    print(time.time() - start)
