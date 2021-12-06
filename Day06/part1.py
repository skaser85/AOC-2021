from __future__ import annotations
from typing import List, Tuple
from dataclasses import dataclass, field

testing = False

if testing:
    input_file = r'Day06\test_input.txt'
else:
    input_file = r'Day06\input.txt'

@dataclass
class Fish:
    spawn_timer: int

    def cycle_day(self) -> Fish:
        f = None
        got_reset = False
        if self.spawn_timer == 0:
            self.spawn_timer = 6
            got_reset = True
            f = Fish(8)
        if not got_reset:
            self.spawn_timer -= 1
        return f

fishes = []
days_to_simulate = 80

with open(input_file, 'r') as f:
    nums = f.read().split(',')
    for n in nums:
        fishes.append(Fish(int(n)))

new_fishes = []
for i in range(days_to_simulate+1):
    fishes.extend([f for f in new_fishes if f is not None])
    new_fishes = []
    if testing:
        if i > 0:
            print(f'After {str(i).rjust(2, " ")} day{"s" if i > 1 else " "}: ({str(len(fishes)).zfill(2)}) {[f.spawn_timer for f in fishes]}')
    for f in fishes:
        new_fishes.append(f.cycle_day())

if testing:
    print(f'After {str(i+1).rjust(2, " ")} day{"s" if i > 1 else " "}: ({str(len(fishes)).zfill(2)}) {[f.spawn_timer for f in fishes]}')
print(len(fishes))