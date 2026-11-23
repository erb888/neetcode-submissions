class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = 0
        minC = 0
        minT = nums[0]
        maxC = 0
        maxT = nums[0]

        for num in nums:
            total += num

            minC = min(minC, 0)
            minC += num

            if minC < minT:
                minT = minC

            maxC = max(maxC, 0)
            maxC += num

            if maxC > maxT:
                maxT = maxC

        if minT == total:
            return maxT

        return max(maxT, total - minT)