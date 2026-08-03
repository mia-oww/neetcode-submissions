class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        left = [1] * length
        right = [1] * length
        output = [1] * length 

        curr_left = 1
        for i in range(length):
            left[i] = curr_left
            curr_left *= nums[i]

        curr_right = 1
        for i in reversed(range(length)): # right -> left
            right[i] = curr_right
            curr_right *= nums[i]

        for i in range(length): # left -> right
            output[i] = left[i] * right[i]
            
        return output


            
        