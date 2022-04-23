from __future__ import annotations
from typing import Any,List,Tuple,Dict
from dataclasses import dataclass,field
import os
from enum import Enum

class CaveSize(Enum):
    SMALL = 0
    LARGE = 1

@dataclass
class Cave:
    name: str
    size: CaveSize
    connections: List[Cave] = field(default_factory=list)
    paths: List[CavePath] = field(default_factory=list)
    visited: int = 0

    @staticmethod
    def create_cave(cave_str: str) -> Cave:
        return Cave(cave_str,CaveSize.SMALL if cave_str.lower() == cave_str else CaveSize.LARGE)

    def can_visit(self) -> bool:
        if self.size == CaveSize.LARGE:
            return True
        elif self.size == CaveSize.SMALL:
            return self.visited == 0

    def visit(self, from_cave: Cave) -> None:
        ...

    def get_cave(self, cave_name: str) -> Cave|None:
        for c in self.connections:
            if c.name == cave_name:
                return c

    def add_connection(self, cave: Cave) -> None:
        if self.get_cave(cave.name) is None:
            self.connections.append(cave)

@dataclass
class CaveWeb:
    name: str
    caves: List[Cave] = field(default_factory=list)

    def get_cave(self, cave_name: str) -> Cave|None:
        for cave in self.caves:
            if cave.name == cave_name:
                return cave

    def add_cave(self, cave: Cave) -> None:
        if self.get_cave(cave.name) is None:
            self.caves.append(cave)

@dataclass
class CavePath:
    path_id: int
    caves_visited: List[Cave] = field(default_factory=list)

    def add_cave(self, cave: Cave) -> bool:
        cave_added = False
        if len(self.caves_visited) == 0:
            if not cave.name == 'start':
                raise ValueError(f'CavePath must start with "start", not {cave.name}')
            else:
                self.caves_visited.append(cave)
                cave_added = True
        else:
            ...
        return cave_added

def parse_input(file_path: str) -> Any:
    if 'test' in os.path.basename(file_path):
        cave_connections = {
            'small': CaveWeb('small'),
            'medium': CaveWeb('medium'),
            'large': CaveWeb('large')
        }
        cave_count = 0
        curr_cave = cave_connections[list(cave_connections.keys())[cave_count]]
        with open(file_path, 'r') as f:
            line = f.readline()
            while line:
                line = line.strip()
                if line == '$$':
                    cave_count += 1
                    curr_cave = cave_connections[list(cave_connections.keys())[cave_count]]
                else:
                    cave1, cave2 = line.split('-')
                    cave1 = curr_cave.get_cave(cave1) or Cave.create_cave(cave1)
                    cave2 = curr_cave.get_cave(cave2) or Cave.create_cave(cave2)
                    cave1.add_connection(cave2)
                    cave2.add_connection(cave1)
                    curr_cave.add_cave(cave1)
                    curr_cave.add_cave(cave2)
                line = f.readline()
    else:
        raise NotImplemented
        cave_connections = []
        with open(file_path, 'r') as f:
            ...
    return cave_connections

if __name__ == '__main__':
    day_dir = os.path.dirname(os.path.realpath(__file__))
    testing = True
    input_file = os.path.join(day_dir, 'input.txt')
    if testing:
        input_file = os.path.join(day_dir, 'test_input.txt')

    cave_connections = parse_input(input_file)
    caves = cave_connections['small']
    start = caves.get_cave('start')
    # for cave in caves.caves:
    #     print(f'Name: {cave.name}')
    #     print(f'Size: {cave.size}')
    #     print('Connections:')
    #     print('|'.join([c.name for c in cave.connections]))
    #     print('##########################')