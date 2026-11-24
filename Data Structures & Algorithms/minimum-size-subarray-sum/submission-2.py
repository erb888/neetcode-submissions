class Solution:
    def minSubArrayLen(self, t: int, nums: List[int]) -> int:
        '''
        sliding window morph

        boundaries:
            len of subarray so R = 2 and L = 0, R - L + 1 = 3, exclusive
            sum >= t
            all positive integers

        vars:
            L = 0
            cache = 0
            lent = len(nums)
            mint = 0

        for R,num in enumerate(nums):
            cache += num

            while cache >= t:
                mint = min(mint, R - L + 1)
                cache -= nums[L]
                L -= 1

        return mint
        '''
        L = 0
        cache = 0
        mint = float('inf')

        for R,num in enumerate(nums):
            cache += num

            while cache >= t:
                mint = min(mint, R - L + 1)
                cache -= nums[L]
                L += 1

        return mint if mint < float('inf') else 0