"""
Author : Ajeet
Date : 29/03/2023
"""
import re

for _ in range(int(input())):
    res = re.search(r'^(_|\.)\d+[a-zA-Z]*_?$', input())
    if res:
        print("VALID")
    else:
        print("INVALID")