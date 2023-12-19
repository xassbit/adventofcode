#!/usr/bin/env python
import re

MAPPER = [
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
]
INVERTED_MAPPER = [element[::-1] for element in MAPPER]


def get_first_digit(string: str):
    result = re.findall(
        r'1|2|3|4|5|6|7|8|9|(?:one)|(?:two)|(?:three)|(?:four)|(?:five)|(?:six)|(?:seven)|(?:eight)|(?:nine)',
        string,
    )[0]
    if result in MAPPER:
        result = MAPPER.index(result) + 1
    return result


def get_last_digit(string: str):
    string = string[::-1]
    result = re.findall(
        r'1|2|3|4|5|6|7|8|9|(?:eno)|(?:owt)|(?:eerht)|(?:ruof)|(?:evif)|(?:xis)|(?:neves)|(?:thgie)|(?:enin)',
        string,
    )[0]
    if result in INVERTED_MAPPER:
        result = INVERTED_MAPPER.index(result) + 1
    return result


if __name__ == '__main__':
    sum = 0
    with open('day1data.txt') as file:
        content = file.read()

    for line in content.split('\n'):
        first = get_first_digit(line)
        last = get_last_digit(line)
        sum += int(f'{first}{last}')

    print(sum)
