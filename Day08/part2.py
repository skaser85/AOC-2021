from __future__ import annotations
from typing import Any,List,Tuple,Dict
from dataclasses import dataclass
import os

def parse_input(file_path: str) -> Any:
    with open(file_path, 'r') as f:
        input_data = []
        output_data = []
        line = f.readline()
        while line:
            data = line.strip().split(' | ')
            input_data.append(data[0])
            output_data.append(data[1])
            line = f.readline()
    return input_data, output_data

if __name__ == '__main__':
    day_dir = os.path.dirname(os.path.realpath(__file__))
    testing = True
    input_file = os.path.join(day_dir, 'input.txt')
    if testing:
        input_file = os.path.join(day_dir, 'test_input.txt')

    input_data, output_data = parse_input(input_file)

    seg_letter_map = {
        0: ['a','b','c','e','f','g'],
        1: ['c','f'],
        2: ['a','c','d','e','g'],
        3: ['a','c','d','f','g'],
        4: ['b','c','d','f'],
        5: ['a','b','d','f','g'],
        6: ['a','b','d','e','f','g'],
        7: ['a','c','f'],
        8: ['a','b','c','d','e','f','g'],
        9: ['a','b','c','d','f','g']
    }

    seg_letter_num_map = {
        'a': [0,2,3,5,6,7,8,9],
        'b': [0,4,5,6,8,9],
        'c': [0,1,2,3,4,7,8,9],
        'd': [2,3,4,5,6,8,9],
        'e': [0,2,6,8],
        'f': [0,1,3,4,5,6,7,8,9],
        'g': [0,2,3,5,6,8,9]
    }

    seg_num_map = {
        0: 6,
        1: 2, # unique
        2: 5,
        3: 5,
        4: 4, # unique
        5: 5,
        6: 6,
        7: 3, # unique
        8: 7, # unique
        9: 5
    }

    seg_num_count_map = {
        2: [1],
        3: [7],
        4: [4],
        5: [2,3,5],
        6: [0,6,9],
        7: [8]
    }

    unique_lens = [2,4,3,7]

    total = 0
    o_nums = []

    test_input = 'acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab'
    test_output = 'cdfeb fcadb cdfeb cdbaf'

    test_segs = {
        0: '',
        1: '',
        2: '',
        3: '',
        4: '',
        5: '',
        6: '',
        7: '',
        8: '',
        9: '',
    }

    test_seg_len_map = {
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: []
    }

    for i in test_input.split(' '):
        test_seg_len_map[len(i)].append(i)
        if len(i) in unique_lens:
            test_segs[seg_num_count_map[len(i)][0]] = i
            # ['ab','eafb','dab','acedgfb']

    test_uniques = {
        1: test_segs[1],
        4: test_segs[4],
        7: test_segs[7],
        8: test_segs[8]
    }

    # print(test_seg_len_map)
            

    def decode_a(char_dict: Dict[int,str]) -> str:
        # eliminate cf (the chars that make 1), and what remains is
        # the character at the top of 7, which in the regular seg map
        # is 'a'
        return eliminate_vals(char_dict[7], char_dict[1])[0]

    def decode_b_d_g(char_dict: Dict[int,str], three: str) -> Tuple[str,str,str]:
        a_char = decode_a(char_dict)
        four = eliminate_vals(char_dict[4], char_dict[1])
        eight = eliminate_vals(char_dict[8], char_dict[1])
        eight = eight.replace(a_char, '')
        three = eliminate_vals(three,char_dict[1])
        three = three.replace(a_char, '')
        for char in three:
            if char in four:
                d = char
            else:
                g = char
        for char in four:
            if char not in three:
                b = char
        return b,d,g

    def eliminate_vals(test_str: str, vals_to_eliminate: str):
        keep = ''
        for char in test_str:
            if not char in vals_to_eliminate:
                keep += char
        return keep

    def decode_6(seg_len_map_6: list[str], char_dict: Dict[int,str]) -> str:
        a_char = decode_a(char_dict)
        eight = eliminate_vals(char_dict[8], char_dict[1])
        eight = ''.join(sorted(eight.replace(a_char, '')))
        for i in seg_len_map_6:
            test = eliminate_vals(i, char_dict[1])
            test = ''.join(sorted(test.replace(a_char,'')))
            if test == eight:
                return i

    def decode_3(seg_len_map_5: list[str], char_dict: Dict[int,str]) -> str:
        a_char = decode_a(char_dict)
        for seg in seg_len_map_5:
            test = eliminate_vals(seg,char_dict[1])
            test = test.replace(a_char,'')
            if len(test) == 2:
                return seg

    def decode_2_5_e(seg_len_map_5: list[str], char_dict: Dict[int,str], three: str, a: str, b: str, d: str, g: str) -> Tuple[str,str,str]:
        two = ''
        five = ''
        e = ''
        for i in seg_len_map_5:
            if ''.join(sorted(i)) == ''.join(sorted(three)):
                continue
            test = eliminate_vals(i, char_dict[1])
            test = test.replace(a,'')
            test = test.replace(b,'')
            test = test.replace(d,'')
            test = test.replace(g,'')
            if len(test) == 0:
                five = i
            else:
                two = i
                e = test
        return two,five,e

    def decode_c(two: str, a: str, d: str, e: str, g: str) -> str:
        two = two.replace(a,'')
        two = two.replace(d,'')
        two = two.replace(e,'')
        two = two.replace(g,'')
        return two

    def decode_f(c: str, one: str) -> str:
        return one.replace(c,'')

    def decode_0(actual_zero: list[str], decded_chars: Dict[str,str]) -> str:
        zero = ''
        for z in actual_zero:
            zero += decded_chars[z]
        return zero

    def decode_9(actual_nine: list[str], decded_chars: Dict[str,str]) -> str:
        nine = ''
        for n in actual_nine:
            nine += decded_chars[n]
        return nine

    test_segs[6] = decode_6(test_seg_len_map[6],test_uniques)
    test_segs[3] = decode_3(test_seg_len_map[5],test_uniques)

    decoded_chars = {}

    decoded_chars['a'] = decode_a(test_uniques)
    decoded_chars['b'],decoded_chars['d'],decoded_chars['g'] = decode_b_d_g(test_uniques,test_segs[3])

    test_segs[2],test_segs[5],decoded_chars['e'] = decode_2_5_e(test_seg_len_map[5],test_uniques,test_segs[3],decoded_chars['a'],decoded_chars['b'],decoded_chars['d'],decoded_chars['g'])

    decoded_chars['c'] = decode_c(test_segs[2],decoded_chars['a'],decoded_chars['d'],decoded_chars['e'],decoded_chars['g'])

    decoded_chars['f'] = decode_f(decoded_chars['c'],test_segs[1])

    test_segs[0] = decode_0(seg_letter_map[0],decoded_chars)

    test_segs[9] = decode_9(seg_letter_map[9],decoded_chars)

    for s in test_segs:
        print(f'{s} = {test_segs[s]}')

    print('----------')

    for d in sorted(decoded_chars):
        print(f'{d} = {decoded_chars[d]}')

    code_to_num = {}
    for s in test_segs:
        code_to_num[''.join(sorted(test_segs[s]))] = s

    print('----------')

    for c in code_to_num:
        print(f'{c} = {code_to_num[c]}')

    ########################################


    # i need to use the input_data for this output_data to figure out what the
    # numbers are before i can do this
    o_nums = []
    for o in output_data:
        o_vals = []
        for od in o.split(' '):
            o_vals.append(code_to_num[''.join(sorted(od))])
        o_nums.append(int(''.join(o_vals)))

    print(o_nums)









    # segs = {
    #     'acedgfb': 8,
    #     'cdfbe': 5,
    #     'gcdfa': 2,
    #     'fbcad': 3,
    #     'dab': 7,
    #     'cefabd': 9,
    #     'cdfgeb': 6,
    #     'eafb': 4,
    #     'cagedb': 0,
    #     'ab': 1
    # }

    # s2 = {}
    # for s in segs:
    #     s2[''.join(sorted(s))] = segs[s]

    # segs = s2