'''
https://leetcode.com/problems/apply-operations-to-an-array/
'''

from typing import *

def applyOperations(nums: List[int]) -> List[int]:
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            nums[i] *= 2
            nums[i+1] = 0

    gen_list_zero = [0]*nums.count(0) # tạo danh sách các số 0
    return gen_list_zero + list(filter(lambda item: item != 0, nums))  # cộng gen_list_zero ở cuối

'''
https://leetcode.com/problems/delete-greatest-value-in-each-row/
'''

def deleteGreatestValue(grid: List[List[int]]) -> int:

    total = 0

    sort_grid = [
        sorted(row)
        for row in grid
    ]
    len_row = len(sort_grid[0])

    for col in range(len_row):
        '''
            [
                [1,2,4],
                [3,3,1]
            ]
            ->
            [
                [1,2,4],
                [1,3,3]
            ]

            (1,1) = 1
            (2,3) = 3
            (4,3) = 4
            4+3+1=8
        '''
        total += max([sort_grid[row][col] for row in range(len(sort_grid))])

    return total

def closestTarget(words: List[str], target: str, startIndex: int) -> int:
    min_dis = float('inf')

    for index, word in enumerate(words):
        if word == target:

            dis = min(abs(index - startIndex), len(words)-abs(index - startIndex))

            if dis < min_dis:
                min_dis = dis
            
            if min_dis == 0:
                return 0
            
    return min_dis if min_dis != float('inf') else -1

if __name__ == '__main__':
    words = ["a","b","leetcode"]
    print(closestTarget(words, "leetcode", 0))