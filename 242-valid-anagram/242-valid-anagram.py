class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter_s = collections.Counter(s)
        counter_t = collections.Counter(t)
        for i in counter_s:
            if counter_s[i]!=counter_t[i]:
                return False
        return set(s) == set(t)