class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = [*s]
        s2 = [*t]

        s1.sort()
        s2.sort()

        if s1 == s2:
            return True
        return False
