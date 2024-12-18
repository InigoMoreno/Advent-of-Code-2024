#!/bin/env python3
from utils import Day
import sympy
import random
import numpy as np


class Day17(Day):
    def __init__(self):
        super().__init__("17")

    def parse(self, input_data):
        registers, program = input_data.split("\n\n")
        self.registers = {ord(k[-1]) - ord('A') + 4: int(v)
                          for k, v in (line.split(':') for line in registers.splitlines())}
        self.program = list(map(int, program.split(':')[1].split(',')))
        self.registers.update({i: i for i in range(4)})

    def part1(self, A_value=None):
        program = self.program.copy()
        registers = self.registers.copy()
        pointer = 0

        A = 4
        B = 5
        C = 7

        if A_value is not None:
            registers[A] = A_value

        output = ""
        while True:
            # print(registers, program[pointer:pointer + 3])
            match program[pointer:]:
                case [0, op, *_]:
                    # print(f"adv {op}")
                    registers[A] //= 2**registers[op]
                    pointer += 2
                case [1, op, *_]:
                    # print(f"bxl {op}")
                    registers[B] ^= op
                    pointer += 2
                case [2, op, *_]:
                    # print(f"bst {op}")
                    registers[B] = registers[op] % 8
                    pointer += 2
                case [3, op, *_]:
                    # print(f"jnz {op}")
                    if registers[A] != 0:
                        pointer = op
                    else:
                        pointer += 2
                case [4, *_]:
                    # print(f"bxc {op}")
                    registers[B] ^= registers[C]
                    pointer += 2
                case [5, op, *_]:
                    # print(f"out {op}")
                    output += str(registers[op] % 8) + ","
                    pointer += 2
                case [6, op, *_]:
                    # print(f"bvd {op}")
                    registers[B] = registers[A] // 2**registers[op]
                    pointer += 2
                case [7, op, *_]:
                    # print(f"cvd {op}")
                    registers[C] = registers[A] // 2**registers[op]
                    pointer += 2
                case _:
                    break
        return output[:-1]

    def part1_sym(self):

        program = self.program.copy()
        registers = self.registers.copy()
        pointer = 0

        A = 4
        B = 5
        C = 7
        registers[A] = sympy.symbols('A')

        output = []
        while True:
            # print(registers, program[pointer:pointer + 3])
            match program[pointer:]:
                case [0, op, *_]:
                    # print(f"adv {op}")
                    registers[A] = sympy.Function('//')(registers[A], sympy.Function('pow')(2, registers[op]))
                    pointer += 2
                case [1, op, *_]:
                    # print(f"bxl {op}")
                    # registers[B] ^= op
                    registers[B] = sympy.Function('xor')(registers[B], op)
                    pointer += 2
                case [2, op, *_]:
                    # print(f"bst {op}")
                    registers[B] = sympy.Function('mod')(registers[op], 8)
                    pointer += 2
                case [3, op, *_]:
                    print(f"jmp to {op} if {registers[A]}!=0")
                    # print(f"jnz {op}")
                    if registers[A] != 0:
                        pointer = op
                    else:
                        pointer += 2
                case [4, *_]:
                    # print(f"bxc {op}")
                    registers[B] = sympy.Function('xor')(registers[B], registers[C])
                    pointer += 2
                case [5, op, *_]:
                    out = sympy.Function('mod')(registers[op], 8)
                    print(f"output {out}")
                    output.append(out)
                    if len(output) > 10:
                        break
                    pointer += 2
                case [6, op, *_]:
                    # print(f"bvd {op}")
                    registers[B] = sympy.Function('//')(registers[A], sympy.Function('pow')(2, registers[op]))
                    pointer += 2
                case [7, op, *_]:
                    # print(f"cvd {op}")
                    registers[C] = sympy.Function('//')(registers[A], sympy.Function('pow')(2, registers[op]))
                    pointer += 2
                case _:
                    break
        return output[:-1]

    def part2(self):
        # self.part1_sym()
        # using sympy we found that output[i] only depends on A//8**i so
        # so the ouptut of A*8 should be the same as A plus one more byte at the begining

        # A = random.randint(8**15, 8**16)
        # print(self.part1(A))
        # print(self.part1(A * 8))

        possibilites = set((0,))
        for p in self.program[::-1]:
            new_possibilites = set()
            for A in possibilites:
                for b in range(8):
                    res = self.part1(A * 8 + b)
                    if int(res.split(',')[0]) == p:
                        new_possibilites.add(A * 8 + b)
            possibilites = new_possibilites

        A = min(possibilites)
        return A


if __name__ == '__main__':
    Day17().main(example=False)
