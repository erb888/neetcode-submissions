class WordDictionary:
    '''
    ok i like this challenge

    so complete the same problem as Friday, i just want to
    add another level of work in terms of going beyond getting
    the node.children.keys() to also picking up where we left off.

    so i'm going to define a utility function that also takes in the
    node and start from the current node instead of starting from the
    beginning. 

        [root]
    ["d"]|["b"]|["m"]| ['.']
    ["a"]|["a"]|["a"]| ['.']
    ["y"]|["y"]|["y"]| ['.']
    '''
    class Node:
        def __init__(self):
            self.children = {}
            self.isWord = False

    def __init__(self):
        self.root = self.Node()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = self.Node()
                
            curr = curr.children[c]

        curr.isWord = True

    def search(self, word: str) -> bool:
        return self._search(word, self.root)

    def _search(self, word: str, node) -> bool:
        for i,c in enumerate(word):
            if (
                c not in node.children
                and c != '.'
            ):
                return False

            if c == '.':
                new_word = word[i+1:]

                for d in node.children.values():
                    res = self._search(new_word, d)
                    
                    if res == True:
                        return True

                return False
                
            node = node.children[c]

        return node.isWord