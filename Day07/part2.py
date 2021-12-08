from __future__ import annotations
from typing import Any,List,Tuple,Dict
from dataclasses import dataclass
import os

def parse_input(file_path: str) -> Any:
    with open(file_path, 'r') as f:
        init = f.read().split(',')
        crabs = []
        for i in init:
            crabs.append(int(i))
    return crabs

def calc_fuel_usage(crabs: List[int], target: int) -> int:
    fuel = 0
    for crab in crabs:
        moves_needed = abs(crab-target)
        while moves_needed > 0:
            fuel += moves_needed
            moves_needed -= 1
    return fuel

if __name__ == '__main__':
    day_dir = os.path.dirname(os.path.realpath(__file__))
    testing = False
    input_file = os.path.join(day_dir, 'input.txt')
    if testing:
        input_file = os.path.join(day_dir, 'test_input.txt')

    crabs = parse_input(input_file)
    crabs.sort()
    max_x = max(crabs)
    possible_x = []
    for x in range(max_x):
        print(x)
        possible_x.append(calc_fuel_usage(crabs,x))
    print(min(possible_x))