#!/usr/bin/env python3

import os

file_name = "input.txt"

if not os.path.isfile(file_name):
    raise ValueError("Given input file cannot be found.")

file = open(file_name, "r")
contents = file.read()
file.close()

split_contents = contents.split("\n")
numbers = [int(x) for x in split_contents if x != ""]

for i, number1 in enumerate(numbers):
    number2 = 2020 - number1
    if number2 in numbers[i:]:
        print("The product of the two numbers is:\t{}".format(number1*number2))
    else:
        for j, number3 in enumerate(numbers):
            number4 = number2 - number3
            if number4 in numbers[j:]:
                print("The product of the three numbers is:\t{}".format(number1*number3*number4))
