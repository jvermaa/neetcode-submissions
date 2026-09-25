class TrieNode:
    def __init__(self):
        self.collections = {}
        self.end_of_word = False

class WordDictionary:

    def __init__(self):
        self.head = TrieNode()

    def addWord(self, word: str) -> None:
        current = self.head

        for c in word:
            if c not in current.collections:
                current.collections[c] = TrieNode()

            current = current.collections[c]
        
        current.end_of_word = True

    def search(self, word: str) -> bool:
        
        def dfs(starting_index, node):

            current = node
            for i in range(starting_index, len(word)):
                c = word[i]
                if c == '.':
                    # Call some function which checks all 26 possibilites
                    for child in current.collections.values():
                        # call the recursive shit from next index
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if c not in current.collections:
                        return False
                    current = current.collections[c]
            
            return current.end_of_word
        
        return dfs(0,self.head)
            
        
