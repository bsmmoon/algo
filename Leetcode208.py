class Trie(object):
    def __init__(self):
        self.start = {}
        self.words = set()

    def insert(self, word):
        following = self.start
        for c in word:
            following = self.findOrInsert(c, following)
        self.words.add(word)

    def findOrInsert(self, val, following):
        following[val] = following.get(val, {})
        return following[val]

    def search(self, word):
        return word in self.words

    def startsWith(self, prefix):
        following = self.start
        for c in prefix:
            following = following.get(c, None)
            if following == None: return False
        return True

trie = Trie();
trie.insert("apple")
print(trie.search("apple"), True)
print(trie.search("app"), False)
print(trie.startsWith("app"), True)
trie.insert("app")
print(trie.search("app"), True)
trie.insert("leetcode")
print(trie.search("leetcode"), True)
print(trie.startsWith("leet"), True)
print(trie.startsWith("code"), False)
trie.insert("leeshienlong")
print(trie.startsWith("leesh"), True)
trie.insert("z")
print(trie.search("z"), True)
print(trie.startsWith("z"), True)
