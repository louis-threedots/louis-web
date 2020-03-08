#! /usr/bin/python3
characters = {
    'a': [1, 0, 0, 0, 0, 0],
    'b': [1, 1, 0, 0, 0, 0],
    'c': [1, 0, 0, 1, 0, 0],
    'd': [1, 0, 0, 1, 1, 0],
    'e': [1, 0, 0, 0, 1, 0],
    'f': [1, 1, 0, 1, 0, 0],
    'g': [1, 1, 0, 1, 1, 0],
    'h': [1, 1, 0, 0, 1, 0],
    'i': [0, 1, 0, 1, 0, 0],
    'j': [0, 1, 0, 1, 1, 0],
    'k': [1, 0, 1, 0, 0, 0],
    'l': [1, 1, 1, 0, 0, 0],
    'm': [1, 0, 1, 1, 0, 0],
    'n': [1, 0, 1, 1, 1, 0],
    'o': [1, 0, 1, 0, 1, 0],
    'p': [1, 1, 1, 1, 0, 0],
    'q': [1, 1, 1, 1, 1, 0],
    'r': [1, 1, 1, 0, 1, 0],
    's': [0, 1, 1, 1, 0, 0],
    't': [0, 1, 1, 1, 1, 0],
    'u': [1, 0, 1, 0, 0, 1],
    'v': [1, 1, 1, 0, 0, 1],
    'w': [0, 1, 0, 1, 1, 1],
    'x': [1, 0, 1, 1, 0, 1],
    'y': [1, 0, 1, 1, 1, 1],
    'z': [1, 0, 1, 0, 1, 1],
    '0': [0, 1, 0, 1, 1, 0],
    '1': [1, 0, 0, 0, 0, 0],
    '2': [1, 1, 0, 0, 0, 0],
    '3': [1, 0, 0, 1, 0, 0],
    '4': [1, 0, 0, 1, 1, 0],
    '5': [1, 0, 0, 0, 1, 0],
    '6': [1, 1, 0, 1, 0, 0],
    '7': [1, 1, 0, 1, 1, 0],
    '8': [1, 1, 0, 0, 1, 0],
    '9': [0, 1, 0, 1, 0, 0],
    '.': [0, 1, 0, 0, 1, 1],
    ',': [0, 1, 0, 0, 0, 0],
    ';': [0, 1, 1, 0, 0, 0],
    ':': [0, 1, 0, 0, 1, 0],
    '/': [0, 0, 1, 1, 0, 0],
    '?': [0, 1, 1, 0, 0, 1],
    '!': [0, 1, 1, 0, 1, 0],
    '@': [0, 0, 1, 1, 1, 0],
    '#': [0, 0, 1, 1, 1, 1],
    '+': [0, 1, 1, 0, 1, 0],
    '-': [0, 0, 1, 0, 0, 1],
    '*': [0, 0, 1, 0, 1, 0],
    '<': [1, 1, 0, 0, 0, 1],
    '>': [0, 0, 1, 1, 1, 0],
    '(': [0, 1, 1, 0, 1, 1],
    ')': [0, 1, 1, 0, 1, 1],
    ' ': [0, 0, 0, 0, 0, 0],
    'CAPITAL': [0, 0, 0, 0, 0, 1],
    'LETTER': [0, 0, 0, 0, 1, 1],
    'NUMBER': [0, 0, 1, 1, 1, 1],
    'ou': [1, 1, 0, 0, 1, 1]
}

pronunciation = {
    'a': "ay",
    'b': "b",
    'c': "c",
    'd': "d",
    'e': "e",
    'f': "f",
    'g': "g",
    'h': "h",
    'i': "i",
    'j': "j",
    'k': "k",
    'l': "l",
    'm': "m",
    'n': "n",
    'o': "o",
    'p': "p",
    'q': "q",
    'r': "r",
    's': "s",
    't': "t",
    'u': "u",
    'v': "v",
    'w': "w",
    'x': "x",
    'y': "y",
    'z': "z",
    '.': "dot",
    ',': "comma",
    ';': "semi colon",
    ':': "colon",
    '/': "slash",
    '?': "question mark",
    '!': "exclamation mark",
    '@': "at symbol",
    '#': "hash",
    '+': "plus symbol",
    '-': "minus symbol",
    '*': "asterisk",
    '<': "less than",
    '>': "greater than",
    '(': "left parentheses",
    ')': "right parentheses",
    ' ': "blank space",
    '0': "zero",
    '1': "one",
    '2': "two",
    '3': "three",
    '4': "four",
    '5': "five",
    '6': "six",
    '7': "seven",
    '8': "eight",
    '9': "nine"
}

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
    list_of_pins = characters[character]
    first_three = list_of_pins[:3]
    second_three = list_of_pins[3:]
    first_three_str = ''.join(str(pin) for pin in first_three)
    second_three_str = ''.join(str(pin) for pin in second_three)

    return {'big': degrees_big[first_three_str], 'small': degrees_small[second_three_str]}
