class Solution:
# string length solution. instead of looking for a delimiter char
    def encode(self, strs: List[str]) -> str:
        # 'h' 'e' 'l' 'l' 'o' /0. dont look for a specific delimiter, use length instead (simulating byte length if we were to do this in C)
        #empty string as edge case
        if not strs: 
            return "" 
        # '000#' -> hello = 0005, world = 0004
        result = []
        for s in strs:
            length = len(s) # hello = 5
            prefix = f"{length:04d}" # 'hello' -> 0005hello
            encoded = prefix + s # -> 0005hello
            result.append(encoded) # -> 0005hello, 0005world
        return "".join(result) # ["0005hello", "0005world"]


    def decode(self, s: str) -> List[str]:
        if not str:
            return []

        i = 0
        result = []

        while i < len(s):
            length = int(s[i : i+4]) # grab '0005' -> 5
            i += 4 # -> pointer move by 4 characters
            word = s[i : i+length] # from 0005 -> start of hello grabbed by I=length(5)
            result.append(word) 
            
            i += length #place pointer at the start of the next prefix, '0005world'
        return result
