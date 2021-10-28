import os
import random
import copy
input_path = 'input.txt'
output_path = 'output.txt'
f_o = open(input_path)
lines = f_o.readlines()

output_file = open(output_path, 'w')

for l in lines:
    l = l.rstrip()
    split_l = l.split(' ')
    base_l = copy.deepcopy(split_l)
    print(base_l)
    print(split_l)
    while base_l == split_l:
        random.shuffle(split_l)
    print(split_l)
    output_file.write(' '.join(split_l) + "\n")

output_file.close()

