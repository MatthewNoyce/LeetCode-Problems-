from typing import List


class Solution:
    def singleNumber(nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        else: 
            #Should add to a list and then remove from said list when its pair is found 
            pair = []
            for i in nums:
                if i in pair:
                    pair.remove(i)
                else:
                    pair.append(i)
            return pair[0]