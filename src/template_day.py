#!/bin/env python3
from utils import Day


class Day0(Day):
    def __init__(self):
        super().__init__("0")

    def parse(self, input_data):
        self.input = input_data

    def part1(self):
        return self.input

    def part2(self):
        return None


if __name__ == '__main__':
    Day0().main(example=True)
