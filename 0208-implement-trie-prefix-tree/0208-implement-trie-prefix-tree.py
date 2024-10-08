'''
- Trie (aka prefix tree)는 startswith에 쓰기 좋은 Data Structure. 
- arr[1,000,000]에서 startswith('b')하는데 startswith('a')가 1,000,000이면 array같은 DS쓰면 최악은 1,000,000임. 
- 이럴땐 Trie가 효율적임. 알파벳은 26개밖에 없어서 layer 1에서 찾는데 최대 O(26)임. (i.e. O(1))   
- 

'''
'''
children을 {} 쓰는 이유
: insert&search O(1) in hashmap. 
insert: 캐릭터 하나가 노드 하나. 끝단어 mark하기. 
search: 끝단어가 올바른지. 
startswith: insert&search O(1) in hashmap. 
To search a word starting with b among 1,000,000 words, list can take 1,000,000 in worst. Trie(prefix tree) takes O(26) = O(1) in worst. So, time O(1)
'''

#Trie를 사용하기 위해 TrieNode필요함. 멤버 variable로는 self.children & endOfword
class TrieNode:
    def __init__(self):
        self.children = {}
        self.EndOfWord = False

class Trie:
    #root는 Trie에서 아무것도 없는 꼭대기 Node임. 첫 알파벳들은 이 root노드 밑에서부터 시작. 
    # 강의 그림 참고
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root #현재 노드의 위치는 맨 꼭대기 노드.
        for c in word: # root부터 시작해서 word의 캐릭터 하나하나들을 넣을거임. 
            if c not in cur.children: #없으면 넣어주고
                cur.children[c] = TrieNode()
            cur = cur.children[c] #있으면 다음 노드로 이동
        cur.EndOfWord = True            

    #insert랑 비슷함. 단지 cur.childen에 c없거나 cur.EndOfWord가 맞지 않으면 return False
    def search(self, word: str) -> bool: 
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False 
            cur = cur.children[c]
        return cur.EndOfWord
        
    #얘도 insert랑 비슷함. 
    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)