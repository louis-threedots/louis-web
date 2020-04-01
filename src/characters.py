#! /usr/bin/python3

alphabet_dict = {
    'a': {'dots': [1, 0, 0, 0, 0, 0], 'display': 'a'},
    'b': {'dots': [1, 1, 0, 0, 0, 0], 'display': 'b'},
    'c': {'dots': [1, 0, 0, 1, 0, 0], 'display': 'c'},
    'd': {'dots': [1, 0, 0, 1, 1, 0], 'display': 'd'},
    'e': {'dots': [1, 0, 0, 0, 1, 0], 'display': 'e'},
    'f': {'dots': [1, 1, 0, 1, 0, 0], 'display': 'f'},
    'g': {'dots': [1, 1, 0, 1, 1, 0], 'display': 'g'},
    'h': {'dots': [1, 1, 0, 0, 1, 0], 'display': 'h'},
    'i': {'dots': [0, 1, 0, 1, 0, 0], 'display': 'i'},
    'j': {'dots': [0, 1, 0, 1, 1, 0], 'display': 'j'},
    'k': {'dots': [1, 0, 1, 0, 0, 0], 'display': 'k'},
    'l': {'dots': [1, 1, 1, 0, 0, 0], 'display': 'l'},
    'm': {'dots': [1, 0, 1, 1, 0, 0], 'display': 'm'},
    'n': {'dots': [1, 0, 1, 1, 1, 0], 'display': 'n'},
    'o': {'dots': [1, 0, 1, 0, 1, 0], 'display': 'o'},
    'p': {'dots': [1, 1, 1, 1, 0, 0], 'display': 'p'},
    'q': {'dots': [1, 1, 1, 1, 1, 0], 'display': 'q'},
    'r': {'dots': [1, 1, 1, 0, 1, 0], 'display': 'r'},
    's': {'dots': [0, 1, 1, 1, 0, 0], 'display': 's'},
    't': {'dots': [0, 1, 1, 1, 1, 0], 'display': 't'},
    'u': {'dots': [1, 0, 1, 0, 0, 1], 'display': 'u'},
    'v': {'dots': [1, 1, 1, 0, 0, 1], 'display': 'v'},
    'w': {'dots': [0, 1, 0, 1, 1, 1], 'display': 'w'},
    'x': {'dots': [1, 0, 1, 1, 0, 1], 'display': 'x'},
    'y': {'dots': [1, 0, 1, 1, 1, 1], 'display': 'y'},
    'z': {'dots': [1, 0, 1, 0, 1, 1], 'display': 'z'},
}
punctuation_dict = {
    '.': {'dots': [0, 1, 0, 0, 1, 1], 'display': 'period'},
    ',': {'dots': [0, 1, 0, 0, 0, 0], 'display': 'comma'},
    ';': {'dots': [0, 1, 1, 0, 0, 0], 'display': 'semicolon'},
    ':': {'dots': [0, 1, 0, 0, 1, 0], 'display': 'colon'},
    '/': {'dots': [0, 0, 1, 1, 0, 0], 'display': 'slash'},
    '?': {'dots': [0, 1, 1, 0, 0, 1], 'display': 'question mark'},
    '!': {'dots': [0, 1, 1, 0, 1, 0], 'display': 'exclamation mark'},
    '@': {'dots': [0, 0, 1, 1, 1, 0], 'display': 'at symbol'},
    '#': {'dots': [0, 0, 1, 1, 1, 1], 'display': 'hash'},
    '+': {'dots': [0, 1, 1, 0, 1, 0], 'display': 'plus'},
    '-': {'dots': [0, 0, 1, 0, 0, 1], 'display': 'minus'},
    '*': {'dots': [0, 0, 1, 0, 1, 0], 'display': 'asterisk'},
    '<': {'dots': [1, 1, 0, 0, 0, 1], 'display': 'less than symbol'},
    '>': {'dots': [0, 0, 1, 1, 1, 0], 'display': 'greater than symbol'},
    '(': {'dots': [0, 1, 1, 0, 1, 1], 'display': 'left parenthesis'},
    ')': {'dots': [0, 1, 1, 0, 1, 1], 'display': 'right parenthesis'},
    '\'': {'dots': [0, 0, 1, 0, 0, 0], 'display': 'apostrophe'},
    '\"': {'dots': [0, 0, 1, 0, 0, 0], 'display': 'quotation mark'}, # TODO check
    ' ': {'dots': [0, 0, 0, 0, 0, 0], 'display': 'blank space'},
}
digit_dict = {
    '0': {'dots': [0, 1, 0, 1, 1, 0], 'display': 'zero'},
    '1': {'dots': [1, 0, 0, 0, 0, 0], 'display': 'one'},
    '2': {'dots': [1, 1, 0, 0, 0, 0], 'display': 'two'},
    '3': {'dots': [1, 0, 0, 1, 0, 0], 'display': 'three'},
    '4': {'dots': [1, 0, 0, 1, 1, 0], 'display': 'four'},
    '5': {'dots': [1, 0, 0, 0, 1, 0], 'display': 'five'},
    '6': {'dots': [1, 1, 0, 1, 0, 0], 'display': 'six'},
    '7': {'dots': [1, 1, 0, 1, 1, 0], 'display': 'seven'},
    '8': {'dots': [1, 1, 0, 0, 1, 0], 'display': 'eight'},
    '9': {'dots': [0, 1, 0, 1, 0, 0], 'display': 'nine'},
}
indicator_dict = {
    'CAPITAL': {'dots': [0, 0, 0, 0, 0, 1], 'display': 'capital'},
    'LETTER': {'dots': [0, 0, 0, 0, 1, 1], 'display': 'letter'},
    'NUMBER': {'dots': [0, 0, 1, 1, 1, 1], 'display': 'number'},
}
contraction_dict = {
    'ou': {'dots': [1, 1, 0, 0, 1, 1], 'display': 'ou'},
}

character_dict = {**alphabet_dict, **digit_dict, **punctuation_dict, **indicator_dict, **contraction_dict}

degrees_small = {
    '000': [0, 180],
    '001': [22, 202], # 0.5
    '010': [45, 225],
    '101': [67, 247], # 0.5
    '011': [90, 270],
    '111': [112, 292], # 0.5
    '110': [135, 315],
    '100': [157, 337], # 0.5
}

degrees_big = {
    '000': [0, 120, 240],
    '001': [15, 135, 255],
    '010': [30, 150, 270],
    '101': [45, 165, 285],
    '011': [60, 180, 300],
    '111': [75, 195, 315],
    '110': [90, 210, 330],
    '100': [105, 225, 345],
}

def character_degrees(character):
    list_of_pins = character_dict[character]['dots']
    first_three = list_of_pins[:3]
    second_three = list_of_pins[3:]
    first_three_str = ''.join(str(pin) for pin in first_three)
    second_three_str = ''.join(str(pin) for pin in second_three)

    return {'big': degrees_big[first_three_str], 'small': degrees_small[second_three_str]}
