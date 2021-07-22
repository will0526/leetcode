from typing import List

def intToRoman(self, num: int) -> str:

    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

    symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    res = ''
    for i in range(13):
        while num >= values[i]:
            num -= values[i]
            res += symbols[i]
    return res
