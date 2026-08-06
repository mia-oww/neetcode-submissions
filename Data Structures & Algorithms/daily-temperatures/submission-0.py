class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures) # deals with if no warmer day
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                previous = stack.pop()  
                result[previous] = i - previous
            stack.append(i)

        return result 