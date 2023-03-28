"""
Author : Ajeet
Date : 28/03/2023

Task

You have a test string S.
Your task is to write a regex that will match S using the following conditions:

S must be of length equal to 45.
The first 40 characters should consist of letters(both lowercase and uppercase), or of even digits.
The last 5 characters should consist of odd digits or whitespace characters.
"""
import re

Regex_Pattern = r'^[A-Za-z02468]{40}[13579\s]{5}$'

print(str(bool(re.search(Regex_Pattern, input()))).lower())
