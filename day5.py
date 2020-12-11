#!/usr/bin/env python3

import os
import math

file_name = "input.txt"

if not os.path.isfile(file_name):
    raise ValueError("Given input file cannot be found.")

file = open(file_name, "r")
contents = file.readlines()
file.close()

highest_id = 0
id_list = []

for line in contents:
    row_indication = line[:7]
    col_indication = line[7:]

    min_row = 0
    max_row = 127
    for letter in row_indication:
        difference = max_row - min_row
        if letter == "F":
            max_row = math.floor(max_row - (difference/2))
        if letter == "B":
            min_row = math.ceil(min_row + (difference/2))
    row = max_row

    min_col = 0
    max_col = 7
    for letter in col_indication:
        difference = max_col - min_col
        if letter == "L":
            max_col = math.floor(max_col - (difference/2))
        if letter == "R":
            min_col = math.ceil(min_col + (difference/2))
    col = max_col

    seat_id = row*8 + col
    id_list.append(seat_id)

    if seat_id > highest_id:
        highest_id = seat_id

print("Highest seat ID:\t{}".format(highest_id))

for number in range(818):
    if number not in id_list:
        if number - 1 in id_list and number + 1 in id_list:
            print("Your seat ID:\t{}".format(number))
