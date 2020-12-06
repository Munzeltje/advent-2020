#!/usr/bin/env python3

import os

def extract_policy_password(input):
    pair = input.split(":")
    policy = pair[0]
    policy = policy.replace(" ", "-")
    policy = policy.split("-")
    password = pair[1]
    return policy, password

def check_old_validity(policy, password):
    min_count = int(policy[0])
    max_count = int(policy[1])
    required_char = policy[2]
    count = password.count(required_char)
    if min_count <= count <= max_count:
        return True
    return False

def check_new_validity(policy, password):
    pos1 = int(policy[0])
    pos2 = int(policy[1])
    required_char = policy[2]
    if password[pos1] == required_char and password[pos2] != required_char:
        return True
    if password[pos1] != required_char and password[pos2] == required_char:
        return True
    return False


file_name = "input.txt"
if not os.path.isfile(file_name):
    raise ValueError("Given input file cannot be found.")

file = open(file_name, "r")
contents = file.read()
file.close()

split_contents = contents.split("\n")
pairs = [x for x in split_contents if x != ""]

old_valid_count = 0
new_valid_count = 0
for pair in pairs:
    policy, password = extract_policy_password(pair)

    if check_old_validity(policy, password):
        old_valid_count += 1
    if check_new_validity(policy, password):
        new_valid_count += 1

print("Number of passwords valid according to old policy:\t{}".format(old_valid_count))
print("Number of passwords valid according to new policy:\t{}".format(new_valid_count))
