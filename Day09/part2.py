from __future__ import annotations
from genericpath import exists
from typing import Any,List,Tuple,Dict
from dataclasses import dataclass,field
import os

@dataclass
class Basin:
    x: int
    y: int
    val: int
    nums: list[int] = field(default_factory=list)

    def __post_init__(self):
        self.nums.append(self.val)

@dataclass
class Spot:
    x: int
    y: int
    val: int
    counted: bool = False
    completed: bool = False
    include_val: bool = True
    neighbors: List[Spot] = field(default_factory=list)

    def check_neighbors(self):
        self.completed = True
        neighbors = [n for n in self.neighbors if not n.completed]
        for n in neighbors:
            if n.val == 9:
                n.include_val = False
                n.completed = True
            else:
                n.get_neighbors()
                n.check_neighbors()

    def neighbor_exists(self, n: Spot) -> bool:
        return n in self.neighbors

    def get_neighbors(self):
        if self.y > 0:
            neighbor = height_map[self.y-1][self.x]
            if not self.neighbor_exists(neighbor):
                self.neighbors.append(neighbor)
        if self.y < len(height_map) - 1:
            neighbor = height_map[self.y+1][self.x]
            if not self.neighbor_exists(neighbor):
                self.neighbors.append(neighbor)
        if self.x > 0:
            neighbor = height_map[self.y][self.x-1]
            if not self.neighbor_exists(neighbor):
                self.neighbors.append(neighbor)
        if self.x < len(height_map[self.y]) - 1:
            neighbor = height_map[self.y][self.x+1]
            if not self.neighbor_exists(neighbor):
                self.neighbors.append(neighbor)

    def calc_size(self):
        size = 1
        self.counted = True
        neighbors = [n for n in self.neighbors if n.include_val and not n.counted]
        for n in neighbors:
            if not n.counted:
                size += n.calc_size()
        return size

def parse_input(file_path: str) -> List[List[Spot]]:
    with open(file_path, 'r') as f:
        h_map = []
        line = f.readline()
        while line:
            h_map.append([int(l) for l in list(line.strip())])
            line = f.readline()
        height_map = []
        for y, row in enumerate(h_map):
            height_map.append([])
            for x, val in enumerate(row):
                height_map[y].append(Spot(x,y,val))
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

    basin_lowest_points: List[Basin] = []
    for y, row in enumerate(height_map):
        for x, spot in enumerate(row):
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
                    if check[c].val <= spot.val:
                        add_val = False
            if add_val:
                basin_lowest_points.append(height_map[y][x])

    print('\n########################\n')

    basin_centers = []
    for b in basin_lowest_points:
        b.get_neighbors()
        b.check_neighbors()
        basin_centers.append(b)

    sizes = []
    for b in basin_centers:
        size = b.calc_size()
        print(f'{b.x = }, {b.y = }, {size = }')
        sizes.append(size)

    top_3 = sorted(sizes,reverse=True)[:3]
    print(top_3)
    total = top_3[0] * top_3[1] * top_3[2]
    print(f'{total = }')

    