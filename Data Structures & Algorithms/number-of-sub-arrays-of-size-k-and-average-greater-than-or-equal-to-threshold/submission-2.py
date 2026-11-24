class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, t: int) -> int:
        '''
        boundaries:
            exclusive size k so if k = 3, window = [1,2,3], R = 2, L = 0

            constraint is avg. >= T

        vars:

            L,R,
            summ = t * k (so i know de min sum i need)
            hash = 0
            res = 0

        initialize de window
        for R,val in enumerate(arr):
            if R - L >= k:
                hash = (hash - arr[L])
                L += 1

            hash += val

            if hash >= summ:
                res += 1

        return res
        '''
        L = 0
        summ = t * k
        hash = 0
        res = 0

        for R,val in enumerate(arr):
            if R - L >= k:
                hash = (hash - arr[L])
                L += 1

            hash += val

            if hash >= summ and R - L == k - 1:
                res += 1

        return res