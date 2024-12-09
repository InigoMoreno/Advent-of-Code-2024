#!/bin/env python3
from utils import Day
import numpy as np
from itertools import combinations


class Point(tuple):
    def __add__(self, other):
        return Point(x + y for x, y in zip(self, other))

    def __sub__(self, other):
        return Point(x - y for x, y in zip(self, other))

    def __le__(self, other):
        return all(x <= y for x, y in zip(self, other))

    def __lt__(self, other):
        return all(x < y for x, y in zip(self, other))

    def __gt__(self, other):
        return all(x > y for x, y in zip(self, other))

    def __ge__(self, value):
        return all(x >= y for x, y in zip(self, value))

    def modulo(self, other):
        return Point(x % y for x, y in zip(self, other))


class Day08(Day):
    def __init__(self):
        super().__init__("08")

    def parse(self, input_data):
        self.map = np.array([list(line.strip()) for line in input_data.strip().splitlines()])
        distinct = np.unique(self.map)
        self.frequencies = distinct[distinct != "."]
        self.antennas = {freq: np.where(self.map == freq) for freq in self.frequencies}

    def part1(self):
        antinodes = set()
        for freq, (xs, ys) in self.antennas.items():
            for (antenna1, antenna2) in combinations(zip(xs, ys), 2):
                antenna1 = Point(antenna1)
                antenna2 = Point(antenna2)
                antinode1 = antenna1 + (antenna1 - antenna2)
                antinode2 = antenna2 + (antenna2 - antenna1)
                if antinode1 < Point(self.map.shape) and antinode1 >= Point((0, 0)):
                    antinodes.add(antinode1)
                if antinode2 < Point(self.map.shape) and antinode2 >= Point((0, 0)):
                    antinodes.add(antinode2)
        return len(antinodes)

    def part2(self):
        bounds = set()
        for x in range(self.map.shape[0]):
            for y in range(self.map.shape[1]):
                bounds.add((x, y))

        found = 0
        for bound in bounds:
            found_this = False
            for freq, (xs, ys) in self.antennas.items():
                for (antenna1, antenna2) in combinations(zip(xs, ys), 2):
                    diff = Point(antenna1) - Point(antenna2)
                    dist = Point(bound) - Point(antenna1)
                    modulo = tuple(a % b for a, b in zip(dist, diff))
                    rem = tuple(a // b for a, b in zip(dist, diff))
                    if modulo == (0, 0) and rem[0] == rem[1]:
                        found += 1
                        found_this = True
                        break
                if found_this:
                    break
        return found


if __name__ == '__main__':
    Day08().main(example=False)
