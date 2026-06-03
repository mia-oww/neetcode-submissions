class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # make a seen, then do check if anagram sorted(strs, reverse=True) == sorted(strs, reverse=False)
        # note: lists cant be used in dictionary, use tuple instead
        seen = {}
        
        for word in strs:
            key = tuple(sorted(word, reverse=True))  
            if key not in seen:
                seen[key] = [] #not seen add to list
            seen[key].append(word)#if seen add to new anagram sublist
        
        return list(seen.values())#return list of all updated seen values

