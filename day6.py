#!/usr/bin/env python3

import os

file_name = "input.txt"

if not os.path.isfile(file_name):
    raise ValueError("Given input file cannot be found.")

file = open(file_name, "r")
contents = file.read()
file.close()

group_answers = contents.split("\n\n")
counts = []

for group_answer in group_answers:
    new_group_answer = group_answer.replace("\n", "")
    questions = {char for char in new_group_answer}
    counts.append(len(questions))

sum_counts = sum(counts)
print("The sum of all counts for ANYONE answering 'yes' is:\t{}".format(sum_counts))


counts = []

for group_answer in group_answers:
    individual_answers = group_answer.split("\n")
    individual_answers = [x for x in individual_answers if x != ""]
    for i, individual_answer in enumerate(individual_answers):
        new_individual_answer = {char for char in individual_answer}
        individual_answers[i] = new_individual_answer
    intersection = set.intersection(*individual_answers)
    counts.append(len(intersection))

sum_counts = sum(counts)
print("The sum of all counts for EVERYONE answering 'yes' is:\t{}".format(sum_counts))
