import os
import re

"""
I wrote this to take a text file full of whatever
crap and extract all IPs out of it.
Then it takes all IPs, condenses them down and sorts them.
Writes them out to the output file.  I also avoid subnet masks at the bottom.

Love you long time.
    - Giggly Bits
"""


#######
path = "/my/path/of/where/stuff/lives/"
input_file = "raw.txt"
output_file = "ip.txt"
#######

import sys # delete me after you do the variable shits above.
sys.exit() # delete me after you do the variable shits above.


dirname = os.path.dirname(path)
input = os.path.join(path, input_file)
output = os.path.join(path, output_file)


print(input)

with open(input, 'r') as f:
    text = f.readlines()

# pattern = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
pattern = r'[0-9]+(?:\.[0-9]+){3}'

first = []
for line in text:
    ip = re.findall( pattern, line )
    if ip:
        for i in ip:
            first.append(i)

final = list(set(first))
final.sort()

with open(output, 'w') as w:
    for ip in final:
        if ip[:8] == "255.255.":
            pass
        else:
            w.write(f"{ip}\n")
