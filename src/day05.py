#!/bin/env python3
from utils import Day


class Day05(Day):
    def __init__(self):
        super().__init__("05")

    def parse(self, input_data):
        rules_section, updates_section = input_data.strip().split('\n\n')
        self.rules = [tuple(map(int, rule.split('|'))) for rule in rules_section.split('\n')]
        self.updates = [list(map(int, update.split(','))) for update in updates_section.split('\n')]

    def is_correct_order(self, update):
        for x, y in self.rules:
            if x in update and y in update and update.index(x) > update.index(y):
                return False
        return True

    def get_first(self, update):
        update = set(update)
        for x, y in self.rules:
            if x in update and y in update:
                update.remove(y)
        return update.pop()

    def reorder_update(self, update):
        if not isinstance(update, set):
            update = set(update)
        if len(update) == 1:
            return list(update)
        first = self.get_first(update)
        rest = update - {first}
        return [first] + self.reorder_update(rest)

    def part1(self):
        correct_updates = [update for update in self.updates if self.is_correct_order(update)]
        middle_pages_sum = sum(update[len(update) // 2] for update in correct_updates)
        return middle_pages_sum

    def part2(self):
        incorrect_updates = [update for update in self.updates if not self.is_correct_order(update)]
        reordered_updates = [self.reorder_update(update) for update in incorrect_updates]
        middle_pages_sum = sum(update[len(update) // 2] for update in reordered_updates)
        return middle_pages_sum


if __name__ == '__main__':
    Day05().main(example=False)
