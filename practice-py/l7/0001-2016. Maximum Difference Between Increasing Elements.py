class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        # Kiểm tra danh sách thảo mãn constraints
        if len(nums) < 2:
            return -1

        # Khởi tạo giá trị đánh dấu giá trị nhỏ nhất
        min_num = nums[0]

        # Khởi tạo max giá trị lớn nhất
        max_diff = -1

        for num in nums[1:]:
            # Kiểm tra xem có giá trị nào bé hơn min_num thì cập nhật giá trị min_num mới chính là giá trị đó
            if num < min_num:
                min_num = num
            else:
                # Tính độ chênh lệch
                current_diff = num - min_num # sai khi mà trong nhánh else xét cái num >= min_num sai ở trường hợp dấu = xảy ra
                '''
                Nếu dấu bằng xảy ra thì current_diff = 0
                '''

                # Kiểm tra độ chênh lệch hiện tại so với max_diff
                if current_diff > max_diff:
                    max_diff = current_diff

        return max_diff if max_diff > 0 else -1
