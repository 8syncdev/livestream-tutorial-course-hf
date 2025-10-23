from typing import *
def find_closest_to_zero(nums: list[int]) -> int:
    nums = set(nums) # bỏ đi các phần tử trùng nhau, tốc độ duyệt phần tử trong set là  tốc độ hằng O(1), list tốc độ O(n)
    closest_num = None # Khởi tạo 1 giá trị để lưu kết quả

    for num in nums:
        if closest_num is None or abs(num) < abs(closest_num):
            closest_num = num
        elif abs(num) == abs(closest_num) and num > closest_num:
            closest_num = num
    
    return closest_num


def checkXMatrix(grid: List[List[int]]) -> bool:
    # Lấy kích thước ma trận
    n = len(grid)
    for i in range(n):
        for j in range(n):

            # Kiểm tra cho đường chéo chính phụ (diagonals)
            if i == j or i+j==n-1:
                if grid[i][j] == 0:
                    return False
            else:
                if grid[i][j] != 0:
                    return False
    return True

def largestLocal(grid: List[List[int]]) -> List[List[int]]:
    # Kích thước ma trận
    n = len(grid)

    # Ma trận lưu kết quả
    '''
    max_local_matrix = [[0] * (n-2) for _ in range(n-2)]
    [0] * (n-2): tạo ra 1 hàng toàn là số 0
    '''
    max_local_matrix = [[0] * (n-2) for _ in range(n-2)]

    for i in range(n-2):
        for j in range(n-2):
            max_local_matrix[i][j] = max(
                grid[i][j], grid[i][j+1], grid[i][j+2], # 3 ô liên tiếp của dòng đầu tiên
                grid[i+1][j], grid[i+1][j+1], grid[i+1][j+2], # 3 ô liên tiếp của dòng đầu tiên
                grid[i+2][j], grid[i+2][j+1], grid[i+2][j+2], # 3 ô liên tiếp của dòng đầu tiên
            )

    return max_local_matrix


if __name__ == '__main__':
    grid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]
    print(largestLocal(grid))