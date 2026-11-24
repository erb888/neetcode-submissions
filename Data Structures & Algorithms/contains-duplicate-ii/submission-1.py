class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        '''
        boundaries: abs(i - j) <= k, so this is inclusive

        vars:
        left
        right
        cache

        for right, num in enumerate(nums):
            initialize de window
            if right - left > k:
                increment left
                del left from cache

            check if val in cache
            if not then just add to cache
            else return true
            
        return False
        '''
        L = 0
        cache = set()

        for R,num in enumerate(nums):
            if R - L > k:
                cache.remove(nums[L])
                L += 1

            if num in cache:
                return True

            cache.add(num)

        return False