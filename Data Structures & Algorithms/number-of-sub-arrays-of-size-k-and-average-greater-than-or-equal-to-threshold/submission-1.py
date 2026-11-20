class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, t: int) -> int:
        '''
        ok let's refresh

        so this is a 2 pointer problem

        also kind of sliding window

        k is the size of the windows

        how many windows have avg >= t?

        let's implement de solution from last time and modify it

        res = 0
        tSum = t * 3
        L = 0
        weight = 0
        lent = len(arr)

        for R in range(lent):
            add to weight
            weight += arr[R]

            if R - L == k - 1:
                here we check if weight is >= tSum den res += 1
                if weight >= tSum:
                    res += 1

                weight -= arr[L]
                L += 1

        return res
        '''
        res = 0
        tSum = t * k
        L = 0
        weight = 0
        lent = len(arr)

        for R in range(lent):
            # add to weight
            weight += arr[R]

            if R - L == k - 1:
                # here we check if weight is >= tSum den res += 1
                if weight >= tSum:
                    res += 1

                weight -= arr[L]
                L += 1

        return res