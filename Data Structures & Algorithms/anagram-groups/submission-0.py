from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        matched_result = defaultdict(list)
        
        for string in strs:
            count_key = [0] * 26
            for s in string:
                count_key[ord(s) - ord("a")] += 1
            matched_result[tuple(count_key)].append(string)

        return list(matched_result.values())
