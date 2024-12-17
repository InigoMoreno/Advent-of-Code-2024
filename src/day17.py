#!/bin/env python3
from utils import Day


class Day17(Day):
    def __init__(self):
        super().__init__("17")

    def parse(self, input_data):
        registers, program = input_data.split("\n\n")
        self.registers = {ord(k[-1]) - ord('A') + 4: int(v)
                          for k, v in (line.split(':') for line in registers.splitlines())}
        self.program = list(map(int, program.split(':')[1].split(',')))
        self.registers.update({i: i for i in range(4)})

    def part1(self):
        program = self.program.copy()
        registers = self.registers.copy()
        pointer = 0

        A = 4
        B = 5
        C = 7

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
        self.log(registers, output)
        return output[:-1]

    def part2(self):
        return None


if __name__ == '__main__':
    Day17().main(example=True)
