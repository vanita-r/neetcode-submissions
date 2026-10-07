'''
U:
- Input: nums (int array) and target (int)
- Output: [i, j]
- Cases:
    - nums[i] + nums[j] == target
    - i != j

M:
- Sliding window, two pointer, brute force, hash map

P:
- If using two pointer and want to use "while left < right" or similar to that, would it
be a good idea to sort the nums array first just in case the numbers in nums aren't in order?
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i
        return []