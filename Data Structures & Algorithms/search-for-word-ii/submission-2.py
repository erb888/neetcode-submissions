class Solution:
    class Node:
        def __init__(self):
            self.children = {}
            self.isWord = False
            self.word = ''

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        root = self.Node()
        lr = len(board)
        lc = len(board[0])

        for word in words:
            curr = root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = self.Node()
                    curr.children[c].word = curr.word + c

                curr = curr.children[c]

            curr.isWord = True

        print(f'root.children: {root.children}')

        def recurse(r,c,node, seen={}):
            key = f'{r},{c}'

            if (
                r == lr
                or r < 0
                or c == lc
                or c < 0
                or key in seen
            ):
                return 0

            seen[key] = 1
            val = board[r][c]

            if val in node.children:
                if node.children[val].isWord == True:
                    res.append(node.children[val].word)
                    node.children[val].isWord = False

                seen1 = seen.copy()
                seen2 = seen.copy()
                seen3 = seen.copy()
                seen4 = seen.copy()
                recurse(r+1,c, node.children[val], seen1)
                recurse(r-1,c, node.children[val], seen2)
                recurse(r,c+1, node.children[val], seen3)
                recurse(r,c-1, node.children[val], seen4)

            return

        for r in range(0, lr):
            for c in range(0, lc):
                seen = {}
                recurse(r,c,root,seen)

        return res