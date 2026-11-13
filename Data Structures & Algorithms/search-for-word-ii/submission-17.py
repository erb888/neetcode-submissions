class Solution:
    class Node:
        def __init__(self):
            self.children = {}
            self.isWord = False
            self.word = ''
            self.refs = 0

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
                curr.refs += 1

            curr.isWord = True

        def recurse(r,c,node, seen):
            key = (r,c)

            if (
                r == lr
                or r < 0
                or c == lc
                or c < 0
                or key in seen
                or board[r][c] not in node.children
                or node.children[board[r][c]].refs < 1
            ):
                return 0

            seen.add(key)
            val = board[r][c]

            if node.children[val].isWord == True:
                res.append(node.children[val].word)
                node.children[val].isWord = False

            recurse(r+1,c, node.children[val], seen)
            recurse(r-1,c, node.children[val], seen)
            recurse(r,c+1, node.children[val], seen)
            recurse(r,c-1, node.children[val], seen)

            seen.remove(key)
            return

        for r in range(0, lr):
            for c in range(0, lc):
                seen = set()
                recurse(r,c,root,seen)

        return res