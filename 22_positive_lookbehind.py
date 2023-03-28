"""
Author : Ajeet
Date : 28/03/2023

(?<=regex_2)regex_1
The positive lookbehind (?<=) asserts regex_1 to be immediately preceded by regex_2. Lookbehind is excluded from
the match (do not consume matches of regex_2), but only assert whether a match is possible or not.

Task

You have a test String S.
Write a regex which can match all the occurences of digit which are immediately preceded by odd digit.
"""

Regex_Pattern = r"(?<=[13579])\d"

import re

Test_String = input()

match = re.findall(Regex_Pattern, Test_String)

print("Number of matches :", len(match))

match = re.findall(Regex_Pattern, Test_String)

print("Number of matches :", len(match))
match = re.findall(Regex_Pattern, Test_String)

print("Number of matches :", len(match))

print(str(bool(re.search(Regex_Pattern, input()))).lower())
