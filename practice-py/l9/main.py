'''
List:
- List built-in
- List comp
- List slicing
- Sort tiêu chí
'''
from typing import *

# https://leetcode.com/problems/the-employee-that-worked-on-the-longest-task/

def hardestWorker(n: int, logs: List[List[int]]) -> int:
    # Khởi tạo biến lưu trữ id của nhân viên và thời gian làm việc của nhân viên

    max_id = logs[0][0] # giả sử id của nhân viên đầu tiên

    max_duration = logs[0][1]-0  # giả sử thời gian làm việc dài nhất của nhân viên đầu tiên, starts = 0 cho task đầu tiên

    for i in range(1, len(logs)):
        # Tính thời gian làm việc của nhân viên hiện tại
        current_duration = logs[i][1] - logs[i-1][1]

        if current_duration > max_duration or (
            current_duration == max_duration and
            logs[i][0] < max_id
        ):
            # Thời gian hiện tại dài hơn, cập nhật max_id và max_duration
            max_id = logs[i][0]

            max_duration = current_duration

    return max_id

def haveConflict(event1: List[str], event2: List[str]) -> bool:
    # Dùng kĩ thuật unpacking
    start1, end1 = event1
    start2, end2 = event2

    if start1 < start2:
        if end1 >= start2:
            return True
        else:
            return False
    else:
        if end2 >= start1:
            return True
        else:
            return False
        

if __name__ == '__main__':
    # event1 = ["10:00","11:00"]
    # event2 = ["14:00","15:00"]

    # print(haveConflict(event1, event2))

    print(ord("1"), ord("2"))





