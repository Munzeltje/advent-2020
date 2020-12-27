#!/usr/bin/env python3

import os
from collections import Counter
# import pdb; pdb.set_trace()

def get_adapters(file_name):
    if not os.path.isfile(file_name):
        raise ValueError("Given input file cannot be found.")

    file = open(file_name, "r")
    contents = file.readlines()
    file.close()

    adapters = [int(x) for x in contents]
    adapters.sort()
    adapters.append(adapters[-1] + 3)       # device's built in adapter
    return adapters

def count_differences(adapters):
    differences = Counter()
    for i, adapter in enumerate(adapters):
        if i == 0:
            previous_adapter = 0
        else:
            previous_adapter = adapters[i-1]
        difference = adapter - previous_adapter
        differences[difference] += 1
    return differences

def main():
    adapters = get_adapters("input.txt")
    differences = count_differences(adapters)

    one_jolt_differences = differences[1]
    three_jolt_differences = differences[3]
    product = one_jolt_differences*three_jolt_differences

    print("Product of 1-jolt and 3-jolt differences:\t{}".format(product))

if __name__ == "__main__":
    main()
