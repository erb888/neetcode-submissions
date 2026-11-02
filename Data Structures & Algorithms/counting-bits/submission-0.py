class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        n = n + 1
        i = 0

        while i < n:
            count = 0
            k = i

            while k:
                if k & 1 == 1:
                    count += 1

                k = k >> 1

            res.append(count)
            i += 1

        return res