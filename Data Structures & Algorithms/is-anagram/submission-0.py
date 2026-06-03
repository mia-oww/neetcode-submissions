class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # use sorted -> make list of letters in string
        # both reverse, check if true. otherwise will be false
        return sorted(s, reverse=True) == sorted(t, reverse=True)
        