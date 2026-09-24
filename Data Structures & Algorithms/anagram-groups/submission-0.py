from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for word in strs:
            count = [0] * 26  # Array for a-z
            for c in word:
                count[ord(c) - ord('a')] += 1
            
            # Use the count tuple as the key
            result[tuple(count)].append(word)      
        
        return list(result.values())