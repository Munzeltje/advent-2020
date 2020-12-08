#!/usr/bin/env python3

import os
import numpy as np

class Map():
    """ Map object contains a map of given area with trees.

    Attributes
    ----------
    map : numpy ndarray
        For each coordinate contains 1 if there is a tree and 0 otherwise.
    width_map : int
        Defines the width of the map, used for modulo since map repeats itself.
    number_of_trees_seen : int
        Counter that keeps track of how many trees have been encountered.
    current_i : int
        Keeps track of current coordinate along 0-axis of 'map'.
    current_j : type
        Keeps track of current coordinate along 1-axis of 'map'.

    """

    def __init__(self):
        self.map = None
        self.width_map = 0
        self.number_of_trees_seen = 0
        self.current_i = 0
        self.current_j = 0

    def set_map(self, lines):
        """Given an input, sets the map as ndarray.

        Parameters
        ----------
        lines : list of strings
            Contains strings denoting where on the map there are trees.

        Returns
        -------
        None
            No return value.

        """
        length = len(lines)
        width = len(lines[0])
        self.map = np.zeros((length, width))
        for i in range(length):
            for j in range(width):
                if lines[i][j] == '#':
                    self.map[i, j] = 1
        self.width_map = width

    def step(self):
        """Step once according to rules: 3 to the right, 1 down. Use modulo
        to account for the map repeating itself along the 1-axis.

        Returns
        -------
        None
            No return value.

        """
        self.current_i += 1
        self.current_j += 3
        self.current_j %= self.width_map - 1

    def check_for_tree(self):
        """Check if there is a tree at current coordinates. If yes,
        add 1 to counter.

        Returns
        -------
        None
            No return value.

        """
        if self.map[self.current_i, self.current_j] == 1:
            self.number_of_trees_seen += 1

    def is_done(self):
        """Check if we are done: if current position is at the bottom of the map.

        Returns
        -------
        bool
            True if done, False otherwise.

        """
        if self.current_i == len(self.map) - 1:
            return True
        return False

    def report_number_of_trees(self):
        """Prints number of trees that were encountered to console.

        Returns
        -------
        None
            No return value.

        """
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
