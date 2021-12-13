from __future__ import annotations
from typing import Any, List,Tuple,Dict
from dataclasses import dataclass,field
import os

@dataclass
class Dumbo:
    x: int
    y: int
    val: int
    flashed: bool = False
    neighbors: List[Dumbo] = field(default_factory=list)

    def get_neighbors(self):
        if self.y > 0: # middle up
            self.neighbors.append(dumbos[self.y-1][self.x])
            if self.x > 0: # up left
                self.neighbors.append(dumbos[self.y-1][self.x-1])
            if self.x < len(dumbos[0]) - 1: # up right
                self.neighbors.append(dumbos[self.y-1][self.x+1])
        if self.x > 0: # middle left
            self.neighbors.append(dumbos[self.y][self.x-1])
        if self.x < len(dumbos[0]) - 1: # middle right
            self.neighbors.append(dumbos[self.y][self.x+1])
        if self.y < len(dumbos) - 1: # middle down
            self.neighbors.append(dumbos[self.y+1][self.x])
            if self.x > 0: # down left
                self.neighbors.append(dumbos[self.y+1][self.x-1])
            if self.x < len(dumbos[0]) - 1: # down right
                self.neighbors.append(dumbos[self.y+1][self.x+1])

    def power_up(self):
        if self.val < 10:
            self.val += 1
            self.flashed = False

    def update(self):
        if self.val == 10:
            self.flashed = True
            self.val = 0
            neighbors = [n for n in self.neighbors if not n.flashed]
            for n in neighbors:
                n.power_up()
            for n in neighbors:
                n.update()

def parse_input(file_path: str) -> Any:
    with open(file_path, 'r') as f:
        grid_vals = []
        line = f.readline()
        while line:
            grid_vals.append([int(l) for l in line.strip()])
            line = f.readline()
        return grid_vals

# def print_dumbos(dumbos: List[List[Dumbo]]):
def print_dumbos(step: int):
    print(f'Step: {step}')
    p = ''
    for y, row in enumerate(dumbos):
        for x, d in enumerate(row):
            p += '* ' if d.val == 0 else (str(d.val) + ' ')
        print(p)
        p = ''

if __name__ == '__main__':
    day_dir = os.path.dirname(os.path.realpath(__file__))
    testing = False
    input_file = os.path.join(day_dir, 'input.txt')
    if testing:
        input_file = os.path.join(day_dir, 'test_input.txt')

    # grid_vals = [
    #     [1,1,1,1,1],
    #     [1,9,9,9,1],
    #     [1,9,1,9,1],
    #     [1,9,9,9,1],
    #     [1,1,1,1,1]
    # ]

    grid_vals = parse_input(input_file)

    dumbos = []

    for y, row in enumerate(grid_vals):
        dumbos.append([])
        for x, val in enumerate(row):
            dumbos[-1].append(Dumbo(x,y,val))
    
    for y, row in enumerate(dumbos):
        for x, d in enumerate(row):
            d.get_neighbors()

    steps = 100
    print_dumbos(-1)
    flash_count = 0
    for s in range(steps):
        for y, row in enumerate(dumbos):
            for x in range(len(row)):
                dumbos[y][x].power_up()
        for y, row in enumerate(dumbos):
            for x, val in enumerate(row):
                dumbos[y][x].update()
        for y, row in enumerate(dumbos):
            for x, d in enumerate(row):
                if d.flashed:
                    flash_count += 1
        print_dumbos(s)
    print(f'{flash_count = }')