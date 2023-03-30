"""
Author : Ajeet
Date : 30/03/2023
"""

import re

n = int(input())

for i in range(n):
    line = input()

    if re.search(
            '^(([0-9]|[0-9]{2}|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[0-9]{2}|1[0-9]{2}|2[0-4][0-9]|25[0-5])$',
            line):
        print('IPv4')
    elif re.search(
            '^([a-f0-9]{0,4}:[a-f0-9]{0,4}:[a-f0-9]{0,4}:[a-f0-9]{0,4}:[a-f0-9]{0,4}:[a-f0-9]{0,4}:[a-f0-9]{0,4}:[a-f0-9]{0,4})$',
            line):
        print('IPv6')
    else:
        print('Neither')