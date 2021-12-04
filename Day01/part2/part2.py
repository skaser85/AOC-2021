# input_file = r'Day01\part2\test_input.txt'
input_file = r'Day01\input.txt'

with open(input_file, 'r') as f:
    a = int(f.readline())
    b = int(f.readline())
    c = int(f.readline())
    d = int(f.readline())
    count = 0
    while d:
        w1 = a + b + c
        w2 = b + c + d
        if w2 > w1:
            count += 1
        a = b
        b = c
        c = d
        d = f.readline()
        if d:
            d = int(d)

print(count)