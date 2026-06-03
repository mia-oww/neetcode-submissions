class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # make a for loop that iterates through nums list
        # make another thing where we basically see if the index has been seen (dictionary)
        seen = set() # basically will store every previous index then if that number is within index true = more than once, false = not seen
        for i in nums:
            if i in seen:
                return True

            seen.add(i) # otherwise if not seen add to set
        return False
