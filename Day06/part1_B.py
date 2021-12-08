from __future__ import annotations
from typing import List, Tuple
from dataclasses import dataclass, field

testing = False

if testing:
    input_file = r'Day06\test_input.txt'
else:
    input_file = r'Day06\input.txt'

fishes = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0
}
days_to_simulate = 256

with open(input_file, 'r') as f:
    nums = f.read().split(',')
    for n in nums:
        fishes[int(n)] += 1

for d in range(days_to_simulate):
    new_fishes = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0}
    for f in range(len(fishes)):
        if f == 0:
            if fishes[f] > 0:
                new_fishes[8] = fishes[f]
                new_fishes[6] = fishes[f]
        else:
            new_fishes[f-1] += fishes[f]
    fishes = new_fishes

total = 0
for f in fishes:
    total += fishes[f]
    print(f'{f} = {fishes[f]}')

print(f'{total = }')