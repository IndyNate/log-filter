import sys
from collections import defaultdict


split_by = sys.argv[2]
filename = sys.argv[1]
infile = open(filename)


substr_dict = defaultdict(int)
for line in infile:
    for substr in line.split(split_by):
        substr_dict[substr] += 1

infile.close()


for key, value in sorted(substr_dict.items()):
    print(f"{key} : {value}")
