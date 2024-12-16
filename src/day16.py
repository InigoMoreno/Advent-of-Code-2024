#!/bin/env python3
from utils import Day
import numpy as np
from astar import AStar
from queue import PriorityQueue


class Pos(tuple):
    def __add__(self, other):
        return Pos(s + o for s, o in zip(self, other))

    def __sub__(self, other):
        return Pos(s - o for s, o in zip(self, other))


class Day16(Day, AStar):
    def __init__(self):
        super().__init__("16")

    def parse(self, input_data):
        self.grid = np.array([list(line) for line in input_data.splitlines()])
        self.start = (Pos(np.argwhere(self.grid == 'S')[0]), Pos((0, 1)))
        self.end = Pos(np.argwhere(self.grid == 'E')[0])
        self.grid[self.start] = '.'

    def neighbors(self, node):
        pos, direction = node
        next_pos = pos + direction
        if self.grid[next_pos] != '#':
            yield next_pos, direction
        if direction[0] == 0:
            new_directions = [Pos((1, 0)), Pos((-1, 0))]
        else:
            new_directions = [Pos((0, 1)), Pos((0, -1))]
        for new_direction in new_directions:
            yield (pos, new_direction)

    def distance_between(self, n1, n2):
        pos1, _ = n1
        pos2, _ = n2
        if pos1 != pos2:
            return 1
        else:
            return 1000

    def heuristic_cost_estimate(self, current, goal):
        pos, _ = current
        return abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])

    def is_goal_reached(self, current, goal):
        return current[0] == goal

    def part1(self):  # Using the AStar library
        path = list(self.astar(self.start, self.end))
        return sum(self.distance_between(n1, n2) for n1, n2 in zip(path, path[1:]))

    def part2(self):  # Had to implement my own AStar to keep track of all paths
        all_visited = set()
        for path in self.all_best_paths(self.start, self.end):
            all_visited.update(pos for pos, _ in path)
        return len(all_visited)

    def all_best_paths(self, start, end):
        from collections import defaultdict
        qcost = defaultdict(lambda: float('inf'))
        queue = PriorityQueue()
        queue.put((self.heuristic_cost_estimate(start, end), 0, start, [start]))
        best_cost = float('inf')
        while not queue.empty():
            expected_cost, cost, current, path = queue.get()
            if expected_cost > best_cost:
                break
            if self.is_goal_reached(current, end):
                best_cost = cost
                yield path
            for neighbor in self.neighbors(current):
                new_cost = cost + self.distance_between(current, neighbor)
                if qcost[neighbor] < new_cost:
                    continue
                new_estimated_cost = new_cost + self.heuristic_cost_estimate(neighbor, end)
                new_path = path + [neighbor]
                qcost[neighbor] = new_cost
                queue.put((new_estimated_cost, new_cost, neighbor, new_path))


if __name__ == '__main__':
    Day16().main(example=False)
