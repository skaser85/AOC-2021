from __future__ import annotations
from typing import Any,List,Tuple,Dict
from dataclasses import dataclass
import os

def parse_input(file_path: str) -> Any:
    with open(file_path, 'r') as f:
        height_map = []
        line = f.readline()
        while line:
            height_map.append([int(l) for l in list(line.strip())])
            line = f.readline()
        return height_map

if __name__ == '__main__':
    day_dir = os.path.dirname(os.path.realpath(__file__))
    testing = False
    input_file = os.path.join(day_dir, 'input.txt')
    if testing:
        input_file = os.path.join(day_dir, 'test_input.txt')

    height_map = parse_input(input_file)
    
    print('map')
    print('-------------------')
    for h in height_map:
        print(h)

    low_points = []
    for y, row in enumerate(height_map):
        for x, val in enumerate(row):
            check = {'up': None,'down':None,'left':None,'right':None}
            if y > 0:
                check['up'] = height_map[y-1][x]
            if y < len(height_map) - 1:
                check['down'] = height_map[y+1][x]
            if x > 0:
                check['left'] = height_map[y][x-1]
            if x < len(row) - 1:
                check['right'] = height_map[y][x+1]
            add_val = True
            for c in check:
                if check[c] is not None:
                    if check[c] <= val:
                        add_val = False
            if add_val:
                low_points.append(val)

    print('\n########################\n')
    print(f'{low_points = }')
    score = 0
    for p in low_points:
        score += (1+p)
    print(f'{score = }')