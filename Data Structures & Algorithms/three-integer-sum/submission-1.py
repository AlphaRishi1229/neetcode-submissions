from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ptr1 = 0
        seen_items = set()
        while ptr1 < len(nums) and nums[ptr1] <= 0:
            desired_target = nums[ptr1]
            ptr2 = ptr1 + 1
            ptr3 = len(nums) - 1
            while ptr2 < ptr3:
                first_num = nums[ptr2]
                second_num = nums[ptr3]
                total = desired_target + first_num + second_num
                if total < 0:
                    ptr2 += 1
                    continue
                if total > 0:
                    ptr3 -= 1
                    continue
                if total == 0:
                    seen_items.add((desired_target, first_num, second_num))
                    ptr2 += 1
                    ptr3 -= 1
            ptr1 += 1
        
        final_list = [list(comb) for comb in seen_items]
        return final_list
