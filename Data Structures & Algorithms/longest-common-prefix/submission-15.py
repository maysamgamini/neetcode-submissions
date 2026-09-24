class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
            
        prefix = strs[0]
        for s in strs[1:]:
            # While the current string doesn't start with the prefix, shrink the prefix by 1
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
                    
        return prefix
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         # strs.sort()
#         # if not strs or not strs[0]:
#         #     return ""
#         if len(strs) == 1:
#             return strs[0]
#         # for i in range(min(len(strs[0]), len(strs[-1]))):
#         #     if not strs[0][i] == strs[-1][i]:
#         #         return strs[0][:i]
#         # return strs[0]     

#         mini = 0
#         for i in range(1, len(strs)):
#             if len(strs[mini]) > len(strs[i]):
#                 mini = i
#         tri = Trie()
#         tri.insert(strs[mini])
#         answeridx = len(strs[0])
#         for i in range(1, len(strs)):
#             answeridx = min(answeridx, tri.lcp(strs[i]))
#         return strs[0][:answeridx]
            
        

# class TrieNode:
#     def __init__(self):
#         self.children = {}

# class Trie:
#     def __init__(self):
#         self.root = TrieNode()   
    
#     def insert(self, word:str) -> None:
#         curr = self.root
#         for c in word:
#             if not c in curr.children:
#                 curr.children[c] = TrieNode()
#             curr = curr.children[c]
                

#     def lcp(self, word:str):
#         curr = self.root
#         prefixIdx = 0
#         for c in word:
#             if c in curr.children:
#                 curr = curr.children[c]
#                 prefixIdx += 1
#             else:
#                 break
#         return prefixIdx
            



                