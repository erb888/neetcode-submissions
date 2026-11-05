import string

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class WordDictionary:
    '''
    So this is similar to de algo i did yesterday
    de only diff is de '.' wrinkle
    should be legit

    can i implement a hashmap? yes
    will it support de '.'? maybe
    let's think through dis easily

    add a word
    same as yesterday
    den add '.at'
    what happens now?
    a dot has to be a special char dats a default like 'a-z'
    we can put it at the end??? or really anywhere when it shows up
    hmm what a/b if you match on 'c' and then it's 'ot' to make 'cot'?
    so you missed de chance to match on 'h' which goes down into 'hat' which is equivalent to '.at'?

    So let's solve de key: we consider all possible characters at the position of '.' and recursively check the rest of the word for each possibility

    so we can do recursive call on search for each child node to see if it matches w/ a given char

    so there's [cot, hat]
    word is '.at'

    for c in word:
        if c == '.':
            for letter in alphabet:
                res = search(letter + word) # somting like dat but i need to change de loop so i can easily splice it together
                if res == True:
                    return True

            return False

        if c not in curr.children:
            return False

        curr = curr.children

    return curr.isWord
    '''
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
        # print(f'word: {word}')
        # print(f'curr: {curr}\n')

        for i,c in enumerate(word):
            # print(f'{i}')
            # print(f'{c}\n')
            if (
                c not in curr.children
                and '.' not in curr.children
                and c != '.'
            ):
                return False

            if c == '.':
                # print(f'Here in dot')
                children = curr.children.keys()

                for child in children:
                    # splice de word together
                    word = f'{word[:i]}{child}{word[i+1:]}'
                    # print(f'{word}\n')
                    res = self.search(word)
                    if res == True:
                        return True

                return False

            curr = curr.children[c]

        return curr.isWord
        
