"""
Author : Ajeet
Date : 29/03/2023

Task
2
<p><a href="http://www.quackit.com/html/tutorial/html_links.cfm">Example Link</a></p>
<div class="more-info"><a href="http://www.quackit.com/html/examples/html_links_examples.cfm">More Link Examples...</a></div>
"""

first_input = int(input())

import re
lst =[]
for i in range(first_input):
    lst.extend(re.findall('<( ?\w+)', input()))

s = sorted(set(lst))
print(';'.join(s))
