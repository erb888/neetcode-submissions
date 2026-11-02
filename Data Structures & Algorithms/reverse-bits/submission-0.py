class Solution:
    def reverseBits(self, n: int) -> int:
        i = 0
        res = 0

        while i < 32:
            bit = ((n >> i) & 1)

            if bit:
                res |= (1 << (31 - i))

            i += 1

        return res