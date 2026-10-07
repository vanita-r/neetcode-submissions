class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
       max_num = 0
       cur_num = 0
       for num in nums:
        if num == 1:
            cur_num += 1
            if cur_num > max_num:
                max_num = cur_num
        else:
            cur_num = 0
       return max_num
       