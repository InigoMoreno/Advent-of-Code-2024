#!/bin/env python3
from utils import Day
import functools



@functools.cache
def blink(N, times):
    calls += 1
    if times == 0:
        return 1
    if N == 0:
        return blink(1, times - 1)
    str_n = str(N)
    L = len(str_n)
    L2, Lm = divmod(L, 2)
    if Lm == 0:
        left_side = int(str_n[:L2])
        right_side = int(str_n[L2:])
        return blink(left_side, times - 1) + blink(right_side, times - 1)
    return blink(N * 2024, times - 1)


class Day11(Day):
    def __init__(self):
        super().__init__("11")

    def parse(self, input_data):
        self.stones = list(map(int, input_data.strip().split(' ')))

    def part1(self):
        result = sum(blink(stone, 25) for stone in self.stones)
        print(blink.cache_info())
        return result

    def part2(self):
        result = sum(blink(stone, 75) for stone in self.stones)
        print(blink.cache_info())
        return result


if __name__ == '__main__':
    Day11().main(example=False)
