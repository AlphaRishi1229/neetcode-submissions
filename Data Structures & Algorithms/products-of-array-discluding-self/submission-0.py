from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_products = []
        post_products = []
        output = []

        # generate prefix products
        index = 0
        current_product = 1
        while index < len(nums):
            current_product *= nums[index]
            pre_products.append(current_product)
            index += 1
        
        # generate postfix products
        index = len(nums) - 1
        current_product = 1
        while index >= 0:
            current_product *= nums[index]
            post_products.append(current_product)
            index -= 1
        post_products = post_products[::-1]
        
        # Calculate output
        output.append(post_products[1])
        index = 1
        while index < len(nums) - 1:
            pre = pre_products[index-1]
            post = post_products[index+1]
            output.append(pre*post)
            index += 1
        output.append(pre_products[len(nums) - 2])

        return output
