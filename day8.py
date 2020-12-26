#!/usr/bin/env python3

import os
import re

file_name = "input.txt"
if not os.path.isfile(file_name):
    raise ValueError("Given input file cannot be found.")

file = open(file_name, "r")
contents = file.readlines()
file.close()

instructions = [(re.match(r"([a-z]+) (-?\+?\d+)\n", line)[1],
                 re.match(r"([a-z]+) (-?\+?\d+)\n", line)[2]) for line in contents]
executed_instructions = len(instructions) * [False]

accumulator = 0
current_position = 0

while not executed_instructions[current_position]:
    executed_instructions[current_position] = True
    instruction = instructions[current_position]
    action_type = instruction[0]
    steps = instruction[1]
    steps_sign = steps[0]
    steps_number = int(steps[1:])

    if action_type == "acc":
        if steps_sign == "+":
            accumulator += steps_number
        else:
            accumulator -= steps_number
        current_position += 1
    elif action_type == "jmp":
        if steps_sign == "+":
            current_position += steps_number
        else:
            current_position -= steps_number
    elif action_type == "nop":
        current_position += 1

print("The value of accumulator when executing instruction twice is:\t{}".format(accumulator))
