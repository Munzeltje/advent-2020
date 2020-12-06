#!/usr/bin/env python3

import os
import numpy as np

class Map():
    def __init__(self):
        self.map = None
        self.width_map = 0
        self.number_of_trees_seen = 0
        self.current_i = 0
        self.current_j = 0

    def set_map(self, lines):
        length = len(lines)
        width = len(lines[0])
        self.map = np.zeros((length, width))
        for i in range(length):
            for j in range(width):
                if lines[i][j] == '#':
                    self.map[i, j] = 1
        self.width_map = width

    def step(self):
        self.current_i += 1
        self.current_j += 3
        self.current_j %= self.width_map - 1

    def check_for_tree(self):
        if self.map[self.current_i, self.current_j] == 1:
            self.number_of_trees_seen += 1

    def is_done(self):
        if self.current_i == len(self.map) - 1:
            return True
        return False

    def report_number_of_trees(self):
        print("Number of trees that are encountered:\t{}".format(self.number_of_trees_seen))


file_name = "input.txt"
if not os.path.isfile(file_name):
    raise ValueError("Given input file cannot be found.")

file = open(file_name, "r")
contents = file.readlines()
file.close()

tree_map = Map()
tree_map.set_map(contents)

while not tree_map.is_done():
    tree_map.step()
    tree_map.check_for_tree()

tree_map.report_number_of_trees()
