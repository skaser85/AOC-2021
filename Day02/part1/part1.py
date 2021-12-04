# input_file = r'Day02/part1/test_input.txt'
input_file = r'Day02\input.txt'

with open(input_file, 'r') as f:
    line = f.readline()
    horz = 0
    depth = 0
    while line:
        cmd, amt = line.strip().split(' ')
        amt = int(amt)
        if cmd == 'forward':
            horz += amt
        elif cmd == 'down':
            depth += amt
        elif cmd == 'up':
            depth -= amt
        else:
            ValueError(f'Unknown cmd: {cmd}')
        line = f.readline()

print(f'{horz=}')
print(f'{depth=}')
print(f'{horz*depth=}')