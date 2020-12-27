#!/usr/bin/env python3

import os
import re
# import pdb; pdb.set_trace()

def read_instructions(file_name):
    file_name = "input.txt"
    if not os.path.isfile(file_name):
        raise ValueError("Given input file cannot be found.")

    file = open(file_name, "r")
    contents = file.readlines()
    file.close()

    instructions = [(re.match(r"([a-z]+) (-?\+?\d+)\n", line)[1],
                     re.match(r"([a-z]+) (-?\+?\d+)\n", line)[2]) for line in contents]
    return instructions

def modify_instructions(instructions, suspicious_instruction):
    instruction = instructions[suspicious_instruction]
    action_type = instruction[0]
    steps = instruction[1]

    modified_instructions = instructions[:]
    if action_type == "jmp":
        modified_instructions[suspicious_instruction] = ("nop", steps)
    if action_type == "nop":
        modified_instructions[suspicious_instruction] = ("jmp", steps)
    return modified_instructions

def follow_instructions(instructions):
    current_position = 0
    accumulator = 0
    executed_instructions = []
    found_loop = False

    while current_position < len(instructions):
        if current_position in executed_instructions:
            print("Accumulator when loop found:\t{}".format(accumulator))
            found_loop = True
            break
        executed_instructions.append(current_position)

        instruction = instructions[current_position]
        action_type = instruction[0]
        steps_sign = instruction[1][0]
        steps_number = int(instruction[1][1:])

        if action_type == "jmp":
            if steps_sign == "+":
                current_position += steps_number
            else:
                current_position -= steps_number
        else:
            current_position += 1

        if action_type == "acc":
            if steps_sign == "+":
                accumulator += steps_number
            else:
                accumulator -= steps_number
    if not found_loop:
        print("Accumulator after termination:\t{}".format(accumulator))
    return found_loop


def main():
    file_name = "input.txt"
    instructions = read_instructions(file_name)

    loop_exists = follow_instructions(instructions)
    instruction_to_be_changed = 0
    while loop_exists:
        modified_instructions = modify_instructions(instructions, instruction_to_be_changed)
        loop_exists = follow_instructions(modified_instructions)
        instruction_to_be_changed += 1

if __name__ == "__main__":
    main()
