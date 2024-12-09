#!/bin/env python3
from utils import Day
import numpy as np


class Day09(Day):
    def __init__(self):
        super().__init__("09")

    def parse(self, input_data):
        self.input = input_data
        self.files = []
        self.free_spaces = []
        disk_map = []
        free_space = False
        next_id = 0
        for c in self.input:
            if free_space:
                self.free_spaces.append((len(disk_map), int(c)))
                disk_map += [-1] * int(c)
                free_space = False
            else:
                self.files.append((len(disk_map), int(c)))
                disk_map += [next_id] * int(c)
                free_space = True
                next_id += 1
        self.disk_map = np.array(disk_map)

    def part1(self):
        disk_map = self.disk_map.copy()

        free_spaces = np.where(self.disk_map == -1)[0]
        full_spaces = list(np.where(self.disk_map != -1)[0])
        for free_space in free_spaces:
            if free_space > len(disk_map):
                break
            next_full_space = full_spaces.pop()
            disk_map[free_space] = disk_map[next_full_space]
            disk_map = disk_map[:next_full_space]
            # print(''.join([str(x) if x >= 0 else '.' for x in disk_map]))

        return sum(a * b for a, b in enumerate(disk_map) if b != -1)

    def part2(self):
        disk_map = self.disk_map.copy()
        free_spaces = self.free_spaces.copy()
        for file_pos, file_len in self.files[::-1]:
            found = -1
            for free_id, (free_pos, free_len) in enumerate(free_spaces):
                if free_len >= file_len:
                    found = free_id
                    break
                if free_pos >= file_pos:
                    break
            if found != -1:
                disk_map[free_pos:free_pos + file_len] = disk_map[file_pos:file_pos + file_len]
                disk_map[file_pos:file_pos + file_len] = -1
                if free_len == file_len:
                    del free_spaces[found]
                else:
                    free_spaces[found] = (free_pos + file_len, free_len - file_len)
                # print(''.join([str(x) if x >= 0 else '.' for x in disk_map]))
                # print(free_spaces)

        return sum(a * b for a, b in enumerate(disk_map) if b != -1)


if __name__ == '__main__':
    Day09().main(example=False)
