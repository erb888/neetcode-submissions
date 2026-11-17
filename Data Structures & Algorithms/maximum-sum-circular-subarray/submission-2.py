class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # print(f'3 % 3: {3 % 3}')
        # print(f'nums[(2 + 1) % 3]: {nums[(2 + 1) % 3]}')
        # print(f'4 % 3]: {4 % 3}')
        # print(f'nums[(2 - 1 + 3) % 3]: {nums[(2 - 1 + 3) % 3]}')
        
        L = 0
        maxV = nums[0]
        n = len(nums)
        lent = (2 * n) - 1

        for k in range(n):
            curr = 0
            for i in range(k, lent):
                cr = i % n

                if L == cr and i > 0:
                    break

                if curr < 0:
                    curr = 0
                    L = cr

                curr += nums[cr]
                maxV = max(curr, maxV)
        
        return maxV