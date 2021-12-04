from __future__ import annotations
from math import sqrt
from typing import List
from dataclasses import dataclass, field

@dataclass
class Tile:
    value: int
    marked: bool = False

@dataclass
class Board:
    size: int
    tile_values: List[str]
    rows: List[Tile] = field(default_factory=list)
    cols: List[Tile] = field(default_factory=list)
    winner: bool = False

    def __post_init__(self):
        tile_values_index = 0

        for _ in range(self.size):
            self.rows.append([])
            for _ in range(self.size):
                self.rows[-1].append(Tile(int(self.tile_values[tile_values_index])))
                tile_values_index += 1

        self.cols = [[] for _ in range(self.size)]
        for r in self.rows:
            for i, tile in enumerate(r):
                self.cols[i].append(tile)

    @staticmethod
    def make_board(board_values: str) -> Board:
        board_values = board_values.split(',')
        size = int(sqrt(len(board_values)))
        return Board(size,board_values)

    def check_board(self, num: int) -> bool:
        # i think we only need to check the rows, because the rows and cols share tiles,
        # so if a row tile gets updated, then the col tile should as well since they're
        # the same tile in memory - i think, at least - i guess we'll see
        tile_got_marked = False
        for row in self.rows:
            for tile in row:
                if tile.value == num:
                    tile.marked = True
                    tile_got_marked = True
        
        for col in self.cols:
            for tile in col:
                if tile.value == num:
                    tile.marked = True
                    tile_got_marked = True

        return tile_got_marked

    def has_won(self) -> bool:
        for row in self.rows:
            if all([t.marked for t in row]):
                self.winner = True
                return True

        for col in self.cols:
            if all([t.marked for t in col]):
                self.winner = True
                return True

        return False

    def print_board(self, board_num: int) -> None:
        print(f'Board {board_num} data :::\n')
        for row in self.rows:
            s = ''
            for tile in row:
                s += f'{str(tile.value).rjust(2," ")} {"X" if tile.marked else "!"} '
            marked_count = len([t for t in row if t.marked])
            s += f' -> {marked_count}'
            if marked_count == self.size:
                s += ' WINNER#WINNER#WINNER#WINNER#WINNER#WINNER'
            print(s)
        print('-----------------------------------')
        s = ''
        for col in self.cols:
            marked_count = len([t for t in col if t.marked])
            s += str(marked_count).rjust(4, ' ') + ' '
        if str(self.size) in s:
            s += ' -> WINNER#WINNER#WINNER#WINNER#WINNER#WINNER'
        print(s)
        print('\n')

    def get_sum_of_unmarked_tiles(self) -> int:
        total = 0
        for row in self.rows:
            for tile in row:
                if not tile.marked:
                    total += tile.value
        return total
                

testing = False

if testing:
    input_file = r'Day04/part1/test_input.txt'
else:
    input_file = r'Day04\input.txt'

numbers_to_draw: List[int] = []
boards: List[Board] = []

with open(input_file, 'r') as f:
    data = f.read().split('\n')
    board_values = ''
    for line in data:
        if line != '':
            if len(numbers_to_draw) == 0:
                numbers_to_draw = [int(n) for n in line.split(',')]
            else:
                if board_values == '':
                    board_values = ','.join([n for n in line.split(' ') if n.strip()])
                else:
                    board_values += ',' + ','.join([n for n in line.split(' ') if n.strip()])
        else:
            if len(board_values) > 0:
                boards.append(Board.make_board(board_values))
                board_values = ''
    if len(board_values) > 0:
        boards.append(Board.make_board(board_values))

for num in numbers_to_draw:
    board_has_won = False
    for i, board in enumerate(boards):
        if board.check_board(num):
            board.print_board(i)
            if board.has_won():
                print(f'{num = }')
                total_unmarked = board.get_sum_of_unmarked_tiles()
                print(f'{total_unmarked = }')
                board_score = num * total_unmarked
                print(f'{board_score = }\n')
                board_has_won = True
                break
    if board_has_won:
        break