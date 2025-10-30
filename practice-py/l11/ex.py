from typing import *
from functools import reduce

def differenceOfSum(nums: List[int]) -> int:
    digits = []

    for num in nums:
        '''
        str(num) -> str, ví dụ 123->'123'
        sau đó dùng list -> '123' -> ['1','2','3']
        map(int, ...) -> [1,2,3]
        -> ép kiểu về list
        '''
        digits = [
            *digits,
            *(list(map(int, list(str(num)))))
        ]

    return abs(sum(nums) - sum(digits))

print(differenceOfSum([1,2,3,4]))