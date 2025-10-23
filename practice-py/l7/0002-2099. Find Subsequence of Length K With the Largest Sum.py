class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # sắp xếp giãm dần các cặp giá trị và vị trị để mục đích đưa các giá trị lớn nhất lên đầu
        # sorted_num =  [(num, idx), (num, idx), ....]
        sorted_num = sorted([
            (num, idx)
            for idx, num in enumerate(nums)
        ], key=lambda item: -item[0]) # (num, idx) là giá trị trả về nên chỗ này item[0] = num, dấu trừ chính sắp xếp giãm dần

        # Lấy ra k phần tử đầu tiên, dùng list slicing
        slice_k_ptu = sorted_num[:k]

        # Sắp xếp về vị trí ban đầu, chính là giá trị idx trong sorted_num, sort theo key của index số 1 item[1] chính là idx trong (num, idx) [0,1]
        sorted_original = sorted(slice_k_ptu, key=lambda item: item[1])
        return [num for num, idx in sorted_original]