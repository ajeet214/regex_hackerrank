"""
Author : Ajeet
Date : 28/03/2023
"""

import re

pattern = r'<a href="(.*?)".*?>([\w ,./]*)(?=</)'
# pat = r'<a href="(.+)">(.+)<'

"""
2
<p><a href="http://www.quackit.com/html/tutorial/html_links.cfm">Example Link</a></p>
<div class="more-info"><a href="http://www.quackit.com/html/examples/html_links_examples.cfm">More Link Examples...</a></div>
"""

for _ in range(int(input())):
    res = re.findall(pattern, input())
    for link, title in res:
        print("{},{}".format(link, title.strip()))
