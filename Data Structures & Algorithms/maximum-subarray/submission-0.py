class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        alright let's go

        so this is finding the sum

        what if it's all negative? that's the only part i'm still hazy on

        let's run thru what i know

        go through
        initialize the vars

        for each num in nums
            check if it's negative or curr
            add to curr the val
            check the max
        '''
        maxValue = nums[0]
        curr = 0

        for num in nums:
            curr = max(curr, 0)
            curr += num
            maxValue = max(curr, maxValue)

        return maxValue