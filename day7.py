#!/usr/bin/env python3

import re
import os

def get_bags_from_input(file_name):
    if not os.path.isfile(file_name):
        raise ValueError("Given input file cannot be found.")

    file = open(file_name, "r")
    contents = file.readlines()
    file.close()

    bags = {}
    for line in contents:
        colour = re.match(r"(.+?) bags contain", line)[1]
        bags[colour] = re.findall(r"(\d+?) (.+?) bags?", line)
    return bags

def contains_shiny_gold(bags, current_bag):
    if current_bag == "shiny gold":
        return True
    else:
        return any(contains_shiny_gold(bags, bag) for _, bag in bags[current_bag])

def count_bags_in_bag(bags, bag_type):
    bag_count = 1 + sum(int(number)*count_bags_in_bag(bags, colour)
                        for number, colour in bags[bag_type])
    return bag_count

def main():
    file_name = "input.txt"
    bags = get_bags_from_input(file_name)

    bag_can_contain_gold_count = 0
    for bag in bags.keys():
        if contains_shiny_gold(bags, bag):
            bag_can_contain_gold_count += 1

    number_of_bags_in_gold = count_bags_in_bag(bags, "shiny gold")

    print("Number of bags that can contain shiny gold:\t{}".format(bag_can_contain_gold_count - 1))
    print("Number of bags that contained by shiny gold:\t{}".format(number_of_bags_in_gold - 1))

if __name__ == "__main__":
    main()
