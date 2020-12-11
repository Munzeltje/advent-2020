#!/usr/bin/env python3

import os
import re

class Passport():
    """Passport object, used to check if given entries make up valid passports.

    Attributes
    ----------
    birth_year : int
        Number between 1920 and 2002.
    issue_year : int
        Number between 2010 and 2020.
    expiration_year : int
        Number between 2020 and 2030.
    height : tuple
        First element denotes height, second denotes metric (cm or in).
    hair_color : string
        A string constisting of a-f and/or 0-9.
    eye_color : string
        One of "amb", "blu", "brn", "gry", "grn", "hzl", "oth"
    passport_id : string
        String constisting of 0-9, must be of length 9.
    country_id : string
        Whatever value was givin.
    valid : bool
        If attribute does not pass check in set_values(), this is set to False.

    """
    def __init__(self):
        self.birth_year = None
        self.issue_year = None
        self.expiration_year = None
        self.height = None
        self.hair_color = None
        self.eye_color = None
        self.passport_id = None
        self.country_id = None
        self.valid = True

    def set_values(self, attributes):
        """Takes a passport entry and sets values of Passport object. Performs
        simple first check to see if passport might be invalid.

        Parameters
        ----------
        attributes : string
            Raw string extracted from input file denoting attribute values.

        Returns
        -------
        None
            No return value.

        """
        attributes = attributes.replace(" ", "\n")
        attributes = attributes.split("\n")
        attributes = [attribute for attribute in attributes if attribute != ""]
        for attribute in attributes:
            attribute = attribute.split(":")
            key = attribute[0]
            value = attribute[1]
            if key == "byr":
                if value.isdigit():
                    self.birth_year = int(value)
                else:
                    self.valid = False

            elif key == "iyr":
                if value.isdigit():
                    self.issue_year = int(value)
                else:
                    self.valid = False

            elif key == "eyr":
                if value.isdigit():
                    self.expiration_year = int(value)
                else:
                    self.valid = False

            elif key == "hgt":
                new_value = re.findall(r'(\d+)(\w+)', value)[0]
                if (len(new_value) == 2 and new_value[0].isdigit()
                        and not new_value[1].isdigit()):
                    self.height = new_value
                else:
                    self.valid = False

            elif key == "hcl":
                if value[0] == '#':
                    self.hair_color = value[1:]
                else:
                    self.valid = False

            elif key == "ecl":
                self.eye_color = value

            elif key == "pid":
                if value.isdigit():
                    self.passport_id = value
                else:
                    self.valid = False

            elif key == "cid":
                self.country_id = value

    def check_validity(self):
        """Elaborate check to see if Passport object is valid.

        Returns
        -------
        bool
            True if Passport is valid, False if not.

        """
        if not self.valid:
            return False

        if self.birth_year is None or not 1920 <= self.birth_year <= 2002:
            return False

        if self.issue_year is None or not 2010 <= self.issue_year <= 2020:
            return False

        if self.expiration_year is None or not 2020 <= self.expiration_year <= 2030:
            return False

        if (self.height is None or (self.height[1] != "cm" and self.height[1] != "in")
                or not self.height[0].isdigit()):
            return False
        if self.height[1] == "cm" and not 150 <= int(self.height[0]) <= 193:
            return False
        if self.height[1] == "in" and not 59 <= int(self.height[0]) <= 76:
            return False

        if self.hair_color is None or len(self.hair_color) != 6:
            return False
        valid_hair_color = re.compile(r'[^a-f0-9.]').search
        if bool(valid_hair_color(self.hair_color)):
            return False

        valid_eye_color = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        if self.eye_color is None or self.eye_color not in valid_eye_color:
            return False

        if self.passport_id is None or len(self.passport_id) != 9:
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
