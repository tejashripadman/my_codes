class Solution:
    def MissingNumber(self,array,n):
        l = set(list(range(1,n+1)))
        l1 = set(array)
        return l.difference(l1).pop()
