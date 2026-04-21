from collections import Counter
from typing import List
# [1], 1
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_counter = Counter(nums)
        count_list = [[] for i in range(len(nums) + 1)]
        for num, count in nums_counter.items():
            index_to_store = count - 1
            count_list[index_to_store].append(num)
            
        result = []
        for i in range(len(count_list) - 1, 0, -1):
            for n in count_list[i - 1]:
                result.append(n)
                if len(result) == k:
                    return result
