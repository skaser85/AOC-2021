from typing import List

testing = False

if testing:
    input_file = r'Day03/part1/test_input.txt'
    bit_len = 5
else:
    input_file = r'Day03\input.txt'
    bit_len = 12

values = []

def get_places(byte_list: List[str]) -> List[List[str]]:
    places = [[] for _ in range(bit_len)]
    for byte in byte_list:
        bits = [b for b in byte]
        for i, b in enumerate(bits):
            places[i].append(b)
    return places

def get_reading(values_to_check: List[str], take_ones: bool) -> str:
    place_to_check = 0
    check_bit = '1' if take_ones else '0'
    check_bit_flipped = '0' if take_ones else '1'
    while len(values_to_check) > 1:
        places = get_places(values_to_check)
        place = places[place_to_check]
        b = ''.join(place)
        ones = b.count('1')
        zeros = b.count('0')
        if ones > zeros or ones == zeros:
            values_to_check = [v for v in values_to_check if v[place_to_check] == check_bit]
        else:
            values_to_check = [v for v in values_to_check if v[place_to_check] == check_bit_flipped]
        print(values_to_check)
        place_to_check += 1
    return values_to_check[0]

with open(input_file, 'r') as f:
    line = f.readline().strip()
    while line:
        values.append(line)
        line = f.readline().strip()

o2_values = values[:]
o2_bin_str = get_reading(o2_values,True)
o2_dec = int(o2_bin_str, base=2)

co2_values = values[:]
co2_bin_str = get_reading(co2_values,False)
co2_dec = int(co2_bin_str, base=2)

life_support_rating = o2_dec * co2_dec

print(life_support_rating)