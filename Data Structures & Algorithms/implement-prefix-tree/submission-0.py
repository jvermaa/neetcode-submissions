class Node:
    def __init__(self):
        self.children = {}
        self.ending = False

class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        current_node = self.root
        for i in word:
            if i not in current_node.children:
                current_node.children[i] = Node()
            current_node = current_node.children[i]
        current_node.ending = True

    def search(self, word: str) -> bool:
        current_node = self.root
        for i in word:
            if i not in current_node.children:
                return False
            current_node = current_node.children[i]
        
        return current_node.ending

    def startsWith(self, prefix: str) -> bool:
        current_node = self.root
        for i in prefix:
            if i not in current_node.children:
                return False
            current_node = current_node.children[i]
        return True