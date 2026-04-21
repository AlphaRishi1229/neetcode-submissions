from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set_of_s = defaultdict[str, int](int)
        set_of_t = defaultdict[str, int](int)
        for char in s:
            set_of_s[char] += 1
        for char in t:
            set_of_t[char] += 1
        return set_of_s == set_of_t
