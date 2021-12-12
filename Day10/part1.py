from __future__ import annotations
from typing import Any,List,Tuple,Dict
from dataclasses import dataclass
import os

@dataclass
class Bracket:
    o: str
    c: str

def parse_input(file_path: str) -> Any:
    with open(file_path, 'r') as f:
        return [l.strip() for l in f.readlines()]

def find_bracket_type(brackets: List[Bracket], char: str) -> Bracket:
    for b in brackets:
        if char == b.o or char == b.c:
            return b

if __name__ == '__main__':
    day_dir = os.path.dirname(os.path.realpath(__file__))
    testing = False
    input_file = os.path.join(day_dir, 'input.txt')
    if testing:
        input_file = os.path.join(day_dir, 'test_input.txt')

    points = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }

    brackets = [Bracket('(',')'),Bracket('[',']'),Bracket('{','}'),Bracket('<','>')]

    lines = parse_input(input_file)

    corrupt = []
    for i, line in enumerate(lines):
        print(i)
        opens = []
        for char in line:
            bracket = find_bracket_type(brackets,char)
            if char == bracket.o:
                opens.append(char)
            elif char == bracket.c:
                last_open = opens.pop()
                if last_open != bracket.o:
                    corrupt.append(char)
            else:
                raise ValueError(f'Invalid character: {char}')

    print(f'{corrupt = }')
    score = 0
    for c in corrupt:
        score += points[c]
    print(f'{score = }')