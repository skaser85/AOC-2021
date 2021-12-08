import sys
import os
from shutil import copyfile

if len(sys.argv) == 1:
    print('''
    ERROR: No Day argument provided

    USAGE: python create_day.py <DayNum>

    EXAMPLE: python create_day.py 8
    This creates a Day08 directory
    ''')
else:
    day_num = sys.argv[1].zfill(2)

    base_dir = os.path.dirname(os.path.realpath(__file__))
    day_dir= os.path.join(base_dir, f'Day{day_num}')

    if os.path.exists(day_dir):
        print(f'Day {day_num} already exists!')
    else:
        os.mkdir(day_dir)
        copyfile(os.path.join(base_dir, 'template.py'), os.path.join(day_dir, 'part1.py'))
        copyfile(os.path.join(base_dir, 'template.py'), os.path.join(day_dir, 'part2.py'))
        with open(os.path.join(day_dir, 'test_input.txt'), 'w') as f:
            f.write('')
        with open(os.path.join(day_dir, 'input.txt'), 'w') as f:
            f.write('')
        print(f'Day {day_num} has been created!')