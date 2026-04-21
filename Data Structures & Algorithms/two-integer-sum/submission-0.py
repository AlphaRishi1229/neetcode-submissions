from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping_of_nums = {}
        for index, value in enumerate(nums):
            if (req := target - value) in mapping_of_nums:
                return [mapping_of_nums[req], index]
            mapping_of_nums[value] = index
        return
