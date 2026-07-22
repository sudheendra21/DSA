class UnionFind:
    def __init__(self,n):
        self.parent = [0]*n
        for i in range(n):
            #initially every node is parent and root to itself
            self.parent[i] = i
    
    #merges two groups
    def union(self,x,y):
        #same root node , same group , so no need of union
        if self.find(x) == self.find(y):
            return
        #If thats not the case we set the parent of one root to 
        #the parent of other
        #We only do union for roots 
        else:
            self.parent[self.find(x)] = self.find(y)
    
    #returns the root of the group 
    def find(self,x):
        #x will be equal to parent(x) only if its root
        while x != self.parent[x]:
           return self.find(self.parent[x])
        return x 
    
    
