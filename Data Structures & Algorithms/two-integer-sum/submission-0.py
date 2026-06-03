class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        #example: [3, 4, 5, 6], target = 7
        for i in range(len(nums)):
            diff = target - nums[i] #  4 = 7 - 3, 3 = 7 - 4, 2 = 7 - 5, 1 = 7 - 6
            if diff in seen: # if difference is in set, there must be 2 indices that = 7. 
                return [seen[diff], i] # return the indices i + j = 7
            seen[nums[i]] = i # store indices of nums as keys into seen