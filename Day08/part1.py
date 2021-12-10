from __future__ import annotations
from typing import Any,List,Tuple,Dict
from dataclasses import dataclass
import os

def parse_input(file_path: str) -> Any:
    with open(file_path, 'r') as f:
        input_data = []
        output_data = []
        line = f.readline()
        while line:
            data = line.strip().split(' | ')
            input_data.append(data[0])
            output_data.append(data[1])
            line = f.readline()
    return input_data, output_data

if __name__ == '__main__':
    day_dir = os.path.dirname(os.path.realpath(__file__))
    testing = False
    input_file = os.path.join(day_dir, 'input.txt')
    if testing:
        input_file = os.path.join(day_dir, 'test_input.txt')

    input_data, output_data = parse_input(input_file)
    
    unique_combos = [7,4,3,2]

    count = 0

    for o in output_data:
        count += len([od for od in o.split(' ') if len(od) in unique_combos])

    print(count)
