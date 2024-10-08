

class Trie:
    def __init__(self):
        self.arr = []
    
    def insert(self, word):
        self.arr.append(word)

    def search(self, word):
        if word in self.arr: return True
        return False

    def startsWith(self, prefix):
        for word in self.arr:
            if word.startswith(prefix):
                return True
        return False
obj = Trie()
word = 'hello'
parm2 = obj.insert('')
parm3 = obj.search('')

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)