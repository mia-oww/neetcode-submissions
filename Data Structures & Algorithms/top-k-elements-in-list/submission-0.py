class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # make hash map/dict then add each i to then count frequencies using max, append to new list then return output of max keys. delete after appending to list to not repeat
        frequent = {}
        for i in nums:
            frequent[(i)] = frequent.get((i), 0) + 1
        # then extract keys using max_key, add to result list
        result = []  
        for i in range(k):
            max_key = max(frequent, key=frequent.get)
            result.append(max_key)
            del frequent[max_key] 
        return result

# time complexity of O(n) since 



        