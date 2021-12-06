# input_file = r'Day03/part1/test_input.txt'
input_file = r'Day03\input.txt'

# bit_len = 5 # test input
bit_len = 12 # actual input

places = [[] for _ in range(bit_len)]

with open(input_file, 'r') as f:
    line = f.readline()
    while line:
        bits = [b for b in line.strip()]
        for i, b in enumerate(bits):
            places[i].append(b)
        line = f.readline()

gamma = ''
epsilon = ''

for p in places:
    b = ''.join(p)
    ones = b.count('1')
    zeros = b.count('0')
    if ones > zeros:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

print(f'{gamma = }')
gamma_dec = int(gamma, base=2)
print(f'{gamma_dec = }')

print(f'{epsilon = }')
epsilon_dec = int(epsilon, base=2)
print(f'{epsilon_dec = }')

power_consumption = gamma_dec * epsilon_dec
print(f'{power_consumption = }')