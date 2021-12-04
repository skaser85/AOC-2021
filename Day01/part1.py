input_file = 'Day01\part1_input.txt'

with open(input_file, 'r') as f:
    line = f.readline()
    prev_depth = -1
    count = 0
    while line:
        depth = int(line)
        if prev_depth > -1:
            if depth > prev_depth:
                count += 1
        prev_depth = depth
        line = f.readline()

print(count)