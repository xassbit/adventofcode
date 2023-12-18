#!/usr/bin/env python

def get_first_digit(string: str):
    return next(element for element in string if element in '1234567890')


if __name__ == '__main__':
    sum = 0
    with open('day1data.txt') as file:
        content = file.read()

    for line in content.split('\n'):
        first = get_first_digit(line)
        last = get_first_digit(line[::-1])
        sum += int(f'{first}{last}')

    print(sum)
