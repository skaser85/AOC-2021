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
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }

    brackets = [Bracket('(',')'),Bracket('[',']'),Bracket('{','}'),Bracket('<','>')]

    lines = parse_input(input_file)

    line_completions = []
    for i, line in enumerate(lines):
        opens = []
        line_corrupt = False
        for char in line:
            bracket = find_bracket_type(brackets,char)
            if char == bracket.o:
                opens.append(char)
            elif char == bracket.c:
                last_open = opens.pop()
                if last_open != bracket.o:
                    line_corrupt = True
                    break
            else:
                raise ValueError(f'Invalid character: {char}')
        if not line_corrupt:
            closes = ''
            for o in reversed(opens):
                b = find_bracket_type(brackets,o)
                closes += b.c
            line_completions.append(closes)

    scores = []
    for line in line_completions:
        score = 0
        for c in line:
            score *= 5
            score += points[c]
        scores.append(score)
    
    scores.sort()
    score = scores[int(len(scores)/2-.5)]
    print(f'{score = }')