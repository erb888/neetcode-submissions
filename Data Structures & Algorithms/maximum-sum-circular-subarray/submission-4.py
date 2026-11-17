class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = 0
        maxV = nums[0]
        minV = nums[0]
        minCurr = 0
        maxCurr = 0

        for num in nums:
            maxCurr = max(maxCurr, 0)
            maxCurr += num
            maxV = max(maxCurr, maxV)

            minCurr = min(minCurr, 0)
            minCurr += num
            minV = min(minCurr, minV)

            total += num
        
        if maxV < 0:
            return maxV
            
        return max(maxV, total - minV)