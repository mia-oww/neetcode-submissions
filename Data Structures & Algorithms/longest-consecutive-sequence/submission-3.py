class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #sorted_nums = sorted(list(set(nums))) too slow..
        # create hashmap then check if i+1 exists
# if i-1 not in set, must be starter num. ex {2, 20, 4} 2-1 ? -> no -> must be first num
        nums_set = set(nums)
        longest = 0
        for num in nums_set:
            if num-1 not in nums_set:
                current = num # need to preserve
                count = 1
                while current+1 in nums_set:
                    current+=1 # increase length
                    count += 1
                longest = max(longest, count)

        return longest



        