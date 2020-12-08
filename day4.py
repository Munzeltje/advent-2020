#!/usr/bin/env python3

import os

class Passport():
    def __init__(self):
        self.birth_year = None
        self.issue_year = None
        self.expiration_year = None
        self.height = None
        self.hair_color = None
        self.eye_color = None
        self.passport_id = None
        self.country_id = None

    def set_values(self, attributes):
        attributes = attributes.replace(" ", "\n")
        attributes = attributes.split("\n")
        attributes = [attribute for attribute in attributes if attribute != ""]
        for attribute in attributes:
            attribute = attribute.split(":")
            key = attribute[0]
            value = attribute[1]
            if key == "byr":
                self.birth_year = value
            elif key == "iyr":
                self.issue_year = value
            elif key == "eyr":
                self.expiration_year = value
            elif key == "hgt":
                self.height = value
            elif key == "hcl":
                self.hair_color = value
            elif key == "ecl":
                self.eye_color = value
            elif key == "pid":
                self.passport_id = value
            elif key == "cid":
                self.country_id = value

    def check_validity(self):
        if (self.birth_year is None or self.issue_year is None
                or self.expiration_year is None or self.height is None
                or self.hair_color is None or self.eye_color is None
                or self.passport_id is None):
            return False
        return True

file_name = "input.txt"
if not os.path.isfile(file_name):
    raise ValueError("Given input file cannot be found.")

file = open(file_name, "r")
contents = file.read()
file.close()

passports = contents.split("\n\n")

number_of_valid_passports = 0

for entry in passports:
    passport = Passport()
    passport.set_values(entry)
    is_valid = passport.check_validity()
    if is_valid:
        number_of_valid_passports += 1

print("Number of valid passports in file:\t{}".format(number_of_valid_passports))
