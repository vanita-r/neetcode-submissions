'''
U:
    - Input: nums array
    - Output: max num of consecutive nums in array
    - we're looking at each item in the array, so use a loop

P:
    - count = 0
        - use this for keeping track of the consecutive numbers
    - max_count = 0


'''
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        count = 0
        for num in nums: 
            if num == 1:
                count += 1
                if count > max_count:
                    max_count = count
            else:
                count = 0
        return max_count

        