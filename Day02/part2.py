# input_file = r'Day02/part2/test_input.txt'
input_file = r'Day02\input.txt'

with open(input_file, 'r') as f:
    line = f.readline()
    horz = 0
    aim = 0
    depth = 0
    while line:
        cmd, amt = line.strip().split(' ')
        amt = int(amt)
        if cmd == 'forward':
            horz += amt
            depth += aim * amt
        elif cmd == 'down':
            aim += amt
        elif cmd == 'up':
            aim -= amt
        else:
            ValueError(f'Unknown cmd: {cmd}')
        line = f.readline()

print(f'{horz=}')
print(f'{depth=}')
print(f'{horz*depth=}')