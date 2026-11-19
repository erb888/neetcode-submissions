class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        '''
        so look for duplicates in the window

        go through nums

        if num is in set return true

        if window is too big, remove the first elem from set
        and increment up

        add num to set

        return false
        '''
        win = {}
        L = 0

        for R in range(len(nums)):
            if R - L > k:
                del win[nums[L]]
                L += 1

            if nums[R] in win:
                return True

            win[nums[R]] = 1

        return False