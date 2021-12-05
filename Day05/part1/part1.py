from __future__ import annotations
from math import sqrt
from typing import List
from dataclasses import dataclass, field

testing = False

if testing:
    input_file = r'Day05/part1/test_input.txt'
    board_size = 10
else:
    input_file = r'Day05\input.txt'
    board_size = 1000

@dataclass
class Point:
    x: int
    y: int
    line_count: int = 0

    def cross(self) -> None:
        self.line_count += 1

@dataclass
class Line:
    pBegin: Point
    pEnd: Point
    points: List[Point] = field(default_factory=list)

    def __post_init__(self):
        if self.pBegin.x == self.pEnd.x:
            # vertical line
            x = self.pBegin.x
            y = self.pBegin.y
            if self.pBegin.y < self.pEnd.y:
                while y <= self.pEnd.y:
                    self.points.append(Point(x,y))
                    y += 1
            else:
                while y >= self.pEnd.y:
                    self.points.append(Point(x,y))
                    y -= 1
        elif self.pBegin.y == self.pEnd.y:
            # horizontal line
            x = self.pBegin.x
            y = self.pBegin.y
            if self.pBegin.x < self.pEnd.x:
                while x <= self.pEnd.x:
                    self.points.append(Point(x,y))
                    x += 1
            else:
                while x >= self.pEnd.x:
                    self.points.append(Point(x,y))
                    x -= 1
        else:
            # diagonal line
            x = self.pBegin.x
            y = self.pBegin.y
            x_dir = 1 if self.pBegin.x < self.pEnd.x else -1
            y_dir = 1 if self.pBegin.y < self.pEnd.y else -1
            while x != self.pEnd.x and y != self.pEnd.y:
                self.points.append(Point(x,y))
                x += x_dir
                y += y_dir
            self.points.append(Point(self.pEnd.x, self.pEnd.y))

board = []
for y in range(board_size):
    board.append([])
    for x in range(board_size):
        board[-1].append(Point(x,y))

lines = []
with open(input_file, 'r') as f:
    line = f.readline()
    while line:
        first, last = line.strip().split(' -> ')
        x, y = first.split(',')
        p1 = Point(int(x), int(y))
        x, y = last.split(',')
        p2 = Point(int(x), int(y))
        l = Line(p1,p2)
        lines.append(l)
        line = f.readline()

for i, line in enumerate(lines):
    for p in line.points:
        board[p.y][p.x].cross()

multi_crossings = 0
for y in range(board_size):
    s = ''
    for x in range(board_size):
        b = board[y][x]
        if b.line_count == 0:
            s += '.'
        else:
            if b.line_count > 1:
                multi_crossings += 1
            s += str(b.line_count)
    if testing:
        print(s)

print(multi_crossings)