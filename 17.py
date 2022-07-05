from typing import Optional, List
import itertools


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return list()
        phoneMap = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz", }
        group = (phoneMap[digit] for digit in digits)
        groups = itertools.product(*group)
        result = ["".join(combile) for combile in groups]
        return result