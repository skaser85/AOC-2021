from __future__ import annotations
from typing import List, Tuple
from dataclasses import dataclass, field
import os
from shutil import copyfile

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
        if self.spawn_timer == 0:
            self.spawn_timer = 6
            f = Fish(8)
        if f is None:
            self.spawn_timer -= 1
        return f

# fishes = []
days_to_simulate = 80

def get_fishes_from_file(file_path: str) -> List[Fish]:
    fishes = []
    with open(file_path, 'r') as f:
        nums = f.read().split(',')
        for n in nums:
            fishes.append(Fish(int(n)))
    return fishes

fish_files = r'Day06\fish_files'
if len(os.listdir(fish_files)):
    for ff in os.listdir(fish_files):
        os.remove(os.path.join(fish_files, ff))

copyfile(input_file, os.path.join(fish_files,'initial.txt'))

new_fishes = []
for i in range(days_to_simulate+1):
    print(i)
    for fi, ff in enumerate(os.listdir(fish_files)):
        if ff.startswith('x_'):
            continue
        ff_path = os.path.join(fish_files,ff)
        fishes = get_fishes_from_file(ff_path)
        new_fishes = []
        
        for f in fishes:
            new_fish = f.cycle_day()
            if new_fish is not None:
                new_fishes.append(new_fish)

        fishes.extend(new_fishes)

        ff2 = f'x_{ff}'
        ff2_path = os.path.join(fish_files,ff2)
        if os.path.exists(ff2_path):
            os.remove(ff2_path)
        os.rename(ff_path, ff2_path)
        
        for i in range(0,len(fishes),100_000):
            fishes_to_save = [str(f.spawn_timer) for f in fishes[i:i+100_000]]
            save_path = os.path.join(fish_files, f'fishes_{fi}_{i}.txt')
            with open(save_path, 'w') as save_file:
                save_file.write(','.join(fishes_to_save))
            

# if testing:
#     print(f'After {str(i+1).rjust(2, " ")} day{"s" if i > 1 else " "}: ({str(len(fishes)).zfill(2)}) {[f.spawn_timer for f in fishes]}')
fishes = []
for ff in os.listdir(fish_files):
    if ff.startswith('x_'):
        continue
    ff_path = os.path.join(fish_files,ff)
    f = []
    f1 = fishes[:]
    f2 = get_fishes_from_file(ff_path)
    f.extend(f1)
    f.extend(f2)
    fishes = f[:]
print(len(fishes))