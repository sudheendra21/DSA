class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    #Function to insert word into Trie
    def insert(self,word):
        node = self.root
        for ch in word:
            if ch in node.children:
                node = node.children[ch]
            else:
                node.children[ch] = TrieNode()
                node = node.children[ch]
        
        node.isEnd = True
        
        
    
    #Function to search the word in Trie and returns True if present
    #else returns False
    
    def search(self,word):
        
        node = self.root
        
        for ch in word:
            if ch not in node.children:
                return False
            else:
                node = node.children[ch]
        
        if node.isEnd == True:
            return True
        else:
            return False
            
    #Function to check if the trie has words starting with word
    
    def startswith(self,word):
        
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            else:
                node = node.children[ch]
        return True
    
    #Returns all the words starting with word
    
    def autocomplete(self,word):
        
        node = self.root
        if not self.startswith(word):
            return []
        else:
            for ch in word:
                node = node.children[ch]
            
            #by now we would be at node with children forming words
            
            # n-ary tree traversal , basically appending to answer if its the appending
            
            #starting dfs
            words = []
            self.dfs(node,word,words)
            return words
    
    def dfs(self,node,path,words):
        
       if node.isEnd == True:
           words.append(path)
          
       for ch,node1 in node.children.items():
           self.dfs(node1,path+ch,words)
         
         
           
        
        
        
            
        
        
        
        
        