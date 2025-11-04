from typing import *


def leftRightDifference(nums: List[int]) -> List[int]:
    return [abs(sum(nums[:i]) - sum(nums[i+1:])) for i in range(len(nums))]


# print(leftRightDifference([10, 3, 5, 2]))


def findColumnWidth(grid: List[List[int]]) -> List[int]:
    '''
    grid = [
        [1],
        [22],
        [333]
    ]
    grid[0] = [1] -> có 1 phần tử, biết được có 1 cột
    len(grid), grid = [1], [22], [333], -> có 3 hàng

    '''
    return [
        max([
                str(grid[row][col]).__len__() # ép kiểu int -> str, chuỗi kí tự sẽ có len xem độ dài kí tự
                for row in range(len(grid))
            ]) # xét tất cả hàng khi duyệt đến mỗi cột
        for col in range(len(grid[0])) # xét mỗi cột
    ]

def rowAndMaximumOnes(mat: List[List[int]]) -> List[int]:
    # pythonic phong cách vắng tắt, cách giải trên 1 dòng
    return max([
        [index, row.count(1)] # vị trí của số hàng, số lượng số 1 của hàng
            for index, row in enumerate(mat)
        ],
        key=lambda item: (
            +item[1], # item[1] -> row.count(1) số lượng
            -item[0], # vị trí lấy vị trí đầu tiên là nhỏ nhất dùng dấu - để đảo chiều bất đẳng thức
        )
    )

if __name__ == '__main__':
    grid = mat = [[0,1],[1,0]]
    print(rowAndMaximumOnes(grid))