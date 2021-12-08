from __future__ import annotations
from typing import Any,List,Tuple,Dict
from dataclasses import dataclass
import os

def parse_input(file_path: str) -> Any:
    with open(file_path, 'r') as f:
        ...

if __name__ == '__main__':
    day_dir = os.path.dirname(os.path.realpath(__file__))
    testing = True
    input_file = os.path.join(day_dir, 'input.txt')
    if testing:
        input_file = os.path.join(day_dir, 'test_input.txt')