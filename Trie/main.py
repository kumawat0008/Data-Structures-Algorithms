class TrieNode:

    def __init__(self):
        self.children = [None]*26
        self.is_end_of_word = False


class Trie:

    def __init__(self):

        self.root = self.get_trie_node()


    def get_trie_node(self):
        return TrieNode()

    def char_to_index(self, ch):
        return ord(ch)-ord('a')

    def insert_word(self,word):

        crawl = self.root

        for level in range(len(word)):
            index = self.char_to_index(word[level])

            if crawl.children[index] is None:
                crawl.children[index] = self.get_trie_node()
            crawl = crawl.children[index]

        crawl.is_end_of_word = True

    def search_word(self,word):
    
        crawl = self.root

        for level in range(len(word)):
            index = self.char_to_index(word[level])

            if crawl.children[index] is None:
                return False
            crawl = crawl.children[index]

        return crawl != None and crawl.is_end_of_word


if __name__ == '__main__': 
    
    keys = ["the","a","there","anaswe","any", 
            "by","their"] 
    output = ["Not present in trie", 
              "Present in trie"] 
  
    t = Trie() 
  
    for key in keys: 
        t.insert_word(key) 
  
    print("the",t.search_word("the")) 
    print("these",t.search_word("these")) 
    print("their",t.search_word("their")) 
    print("thaw",t.search_word("thaw")) 
