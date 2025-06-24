class Solution:
    def twoSum(self, nums, target):
        num_map = {}  # This is like a notebook where we remember numbers we've seen

        for i, num in enumerate(nums):  # Look at each number and its position
            difference = target - num  # What number do we need to reach the target?
 
            if difference in num_map:
                return [num_map[difference], i]  # We found the pair! 
 
            num_map[num] = i  # Remember this number and where we saw it     
