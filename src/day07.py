#!/bin/env python3
from utils import Day
import itertools


class Day07(Day):
    def __init__(self):
        super().__init__("07")

    def parse(self, input_data):
        self.equations = []
        for line in input_data.splitlines():
            left, right = line.split(": ")
            right = right.split(" ")
            self.equations.append((int(left), list(map(int, right))))

    def generic_part(self, available_operators):
        sum_correct = 0
        for expected_result, numbers in self.equations:
            for operators in itertools.product(available_operators, repeat=len(numbers) - 1):
                result = numbers[0]
                for number, operator in zip(numbers[1:], operators):
                    if operator == "+":
                        result += number
                    elif operator == "*":
                        result *= number
                    elif operator == "|":
                        result = int(str(result) + str(number))
                    if result > expected_result:
                        break
                if expected_result == result:
                    sum_correct += result
                    break
        return sum_correct

    def part1(self):
        return self.generic_part("+*")

    def part2(self):
        return self.generic_part("+*|")


if __name__ == '__main__':
    Day07().main(example=False)
