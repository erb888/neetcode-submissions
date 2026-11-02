class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        So just implement the bottom up 2DP algo that i just learned

        define the previous
        prevRow = [0] * n

        for r in range(m - 1, -1, -1):
            currRow = [0] * n
            currRow[-1] = 1

            for c in range(n - 2, -1, -1):
                currRow[c] = prevRow[c] + currRow[c + 1]

            prevRow = currRow

        return prevRow[0]
        '''
        prevRow = [0] * n

        for r in range(m - 1, -1, -1):
            currRow = [0] * n
            currRow[-1] = 1

            for c in range(n - 2, -1, -1):
                currRow[c] = prevRow[c] + currRow[c + 1]

            prevRow = currRow

        return prevRow[0]