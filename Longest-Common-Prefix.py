class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        strs.sort()
        first = strs[0]
        last = strs[-1]
        result =""
        for i in range(len(first)):
            if i >= len(last) or first[i] != last[i]:
                 return result          
            result = result+first[i]
        return result
    
      
