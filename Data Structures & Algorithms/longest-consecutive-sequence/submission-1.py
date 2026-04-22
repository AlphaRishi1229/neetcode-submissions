from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        visited_nums = set[int]()
        index = 0
        longest_consecutive = 0
        
        while index < len(nums):
            current_num = nums[index]
            pre_side = current_num
            post_side = current_num
            current_consecutive = 1
            visited_nums.add(current_num)
            while (pre_side - 1) in visited_nums:
                current_consecutive += 1
                pre_side -= 1
            while (post_side + 1) in visited_nums:
                current_consecutive += 1
                post_side += 1
            
            index += 1
            longest_consecutive = max(longest_consecutive, current_consecutive)
        
        return longest_consecutive
