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
        got_reset = False
        if self.spawn_timer == 0:
            self.spawn_timer = 6
            got_reset = True
            f = Fish(8)
        if not got_reset:
            self.spawn_timer -= 1
        return f

days_to_simulate = 256
fish_files = r'Day06\fish_files'

def get_fishes_from_file(file_path: str) -> List[Fish]:
    fishes = []
    with open(file_path, 'r') as f:
        nums = f.read().split(',')
        for n in nums:
            fishes.append(Fish(int(n)))
    return fishes

def clear_fishes_files():
    if len(os.listdir(fish_files)):
        for ff in os.listdir(fish_files):
            os.remove(os.path.join(fish_files, ff))


fishes = get_fishes_from_file(input_file)
new_fishes = []

log = []
clear_fishes_files()
copyfile(input_file, os.path.join(fish_files,'initial.txt'))
for i in range(days_to_simulate):
    print(i)
    if testing:
        if i > 0:
            log_entry = f'After {str(i-1).rjust(2, " ")} day{"s" if i > 1 else " "}: ({str(len(fishes)).zfill(2)}) {[f.spawn_timer for f in fishes]}'
            log.append(log_entry)
            print(log_entry)

    for fi, ff in enumerate(os.listdir(fish_files)):
        ff_path = os.path.join(fish_files,ff)
        fishes = get_fishes_from_file(ff_path)
        new_fishes = []
        
        for f in fishes:
            new_fish = f.cycle_day()
            new_fishes.append(new_fish)

        fishes.extend([f for f in new_fishes if f is not None])
        
        os.remove(ff_path)
        si = 0
        for sf in range(0,len(fishes),10_000_000):
            si += 1
            fishes_to_save = [str(f.spawn_timer) for f in fishes[sf:sf+10_000_000]]
            save_path = os.path.join(fish_files, f'fishes_Day-{i}_File Number-{fi}_Day File Iteration-{si}.txt')
            with open(save_path, 'w') as save_file:
                save_file.write(','.join(fishes_to_save))
            

if testing:
    log_entry = f'After {str(i).rjust(2, " ")} day{"s" if i > 1 else " "}: ({str(len(fishes)).zfill(2)}) {[f.spawn_timer for f in fishes]}'
    log.append(log_entry)
    print(log_entry)
    with open(f'Day06\log2.txt', 'w') as f:
        f.write('\n'.join(log))
fishes = []
for ff in os.listdir(fish_files):
    ff_path = os.path.join(fish_files,ff)
    f = []
    f1 = fishes[:]
    f2 = get_fishes_from_file(ff_path)
    f.extend(f1)
    f.extend(f2)
    fishes = f[:]
print(len(fishes))
clear_fishes_files()