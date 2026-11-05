import string

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children and '.' not in curr.children:
                curr.children[c] = TrieNode()

            curr = curr.children[c]

        curr.isWord = True

    def search(self, word: str) -> bool:
        curr = self.root

        for i,c in enumerate(word):
            if (
                c not in curr.children
                and '.' not in curr.children
                and c != '.'
            ):
                return False

            if c == '.':
                children = curr.children.keys()

                for child in children:
                    # splice de word together
                    word = f'{word[:i]}{child}{word[i+1:]}'
                    res = self.search(word)
                    if res == True:
                        return True

                return False

            curr = curr.children[c]

        return curr.isWord
        
