# class Solution:
#     def minOperations(self, s: str) -> int:

#         if s==''.join(sorted(s)):
#             return 0

#         l=list(pairwise(s))
#         c=0
#         for i in l:
#             if i != sorted(i):
#                 c+=1
#         if c==1:
#             return -1
#         return c-1


from itertools import pairwise

class Solution:
    def minOperations(self, s: str) -> int:
        # 1. If already sorted, 0 operations needed
        if all(a <= b for a, b in pairwise(s)):
            return 0
            
        # 2. If length is 2 and not sorted, it's impossible to sort
        if len(s) == 2:
            return -1
            
        mn, mx = min(s), max(s)
        
        # 3. If the min is at the start or max is at the end, it takes 1 operation
        if s[0] == mn or s[-1] == mx:
            return 1
            
        # 4. If min or max are anywhere in the middle, it takes 2 operations
        if any(c in [mn, mx] for c in s[1:-1]):
            return 2
            
        # 5. Otherwise, it takes 3 operations
        return 3
