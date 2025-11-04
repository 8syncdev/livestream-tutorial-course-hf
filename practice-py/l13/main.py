from typing import *

def maxDivScore(nums: List[int], divisors: List[int]) -> int:

    return max(
        [ (sum(1 for num in nums if num % divisor == 0), divisor)
        for _, divisor in enumerate(divisors) ],
        key=lambda item: (
            item[0],
            -item[1]
        )
    )[1]

def semiOrderedPermutation(nums: List[int]) -> int:
    pos_one = nums.index(1)
    pos_n = nums.index(len(nums))

    return pos_one + (len(nums)-1 - pos_n) if pos_one < pos_n else pos_one + (len(nums) - 1- pos_n) -1


if __name__ == '__main__':
    nums = [2,1,4,3]

    print(semiOrderedPermutation(nums))