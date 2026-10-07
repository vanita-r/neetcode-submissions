'''
U:
- Input: s (str) and t (str)
- Output: 
    - True if anagrams of each other
    - False otherwise

M: for loop, [*s] and [*t], sort(), or sorted()

P:
- Check if both strings contain the same characters appearing the same number of times regardless of order
    - What if we turn both strings into lists with characters listed individually and then sort them alphabetically?
        - We can use the sorted() method to do both these or do them individually 
    - Then check if s == t, if they do then return True, otherwise False
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #option A
        '''s1 = [*s]
        s2 = [*t]
        s1.sort()
        s2.sort()
        if s1 == s2:
            return True
        return False'''

        #option B
        return sorted(s) == sorted(t)
        