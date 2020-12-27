#!/usr/bin/env python3

import os

def read_xmas_data(file_name):
    if not os.path.isfile(file_name):
        raise ValueError("Given input file cannot be found.")

    file = open(file_name, "r")
    contents = file.readlines()
    file.close()

    xmas_data = [int(x) for x in contents]
    return xmas_data

def next_step(xmas_data, current_position):
    current_position += 1
    current_number = xmas_data[current_position]
    prev_25 = xmas_data[current_position - 25 : current_position]
    return current_position, current_number, prev_25

def is_valid(current_number, prev_25):
    prev_25.sort()

    left_pointer = 0
    right_pointer = 24

    while left_pointer < right_pointer:
        if prev_25[left_pointer] + prev_25[right_pointer] == current_number:
            return True
        if prev_25[left_pointer] + prev_25[right_pointer] < current_number:
            left_pointer += 1
        else:
            right_pointer -= 1
    return False

def find_contiguous_set(xmas_data, number):
    for start_index, _ in enumerate(xmas_data):
        end_index = start_index + 1
        while sum(xmas_data[start_index:end_index]) < number:
            end_index += 1
        if sum(xmas_data[start_index:end_index]) == number:
            return xmas_data[start_index:end_index]

def find_weakness(contiguous_set):
    min_value = min(contiguous_set)
    max_value = max(contiguous_set)
    weakness = min_value + max_value
    return weakness

def main():
    xmas_data = read_xmas_data("input.txt")

    current_position = 25
    current_number = xmas_data[current_position]
    prev_25 = xmas_data[:25]

    while is_valid(current_number, prev_25):
        current_position, current_number, prev_25 = next_step(xmas_data, current_position)

    print("The first invalid number:\t{}".format(current_number))

    contiguous_set = find_contiguous_set(xmas_data, current_number)
    weakness = find_weakness(contiguous_set)

    print("The encryption weakness is:\t{}".format(weakness))


if __name__ == "__main__":
    main()
