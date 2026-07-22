class UnionFind:
    def __init__(self,n):
        self.parent = [0]*n
        #rank is basically height of the group
        #Initially each element is in its own group 
        #rank is zero
        self.rank = [0]*n
        for i in range(n):
            #initially every node is parent and root to itself
            self.parent[i] = i
    
    #merges two groups
    def union(self,x,y):
        rx = self.find(x)
        ry = self.find(y)
        #same root node , same group , so no need of union
        if rx == ry:
            return
        #If thats not the case we set the parent of one root to 
        #the parent of other
        #We only do union for roots 
        if self.rank[rx] < self.rank[ry]:
            #we will merge 
            self.parent[rx] = ry
        elif self.rank[ry] < self.rank[rx]:
            self.parent[ry] = rx
        
        else:
            #both same height , does not matter , but rank
            #increases
            self.parent[rx] = ry
            self.rank[ry] += 1
    #returns the root of the group 
    def find(self,x):
        #x will be equal to parent(x) only if its root
        if x != self.parent[x]:
           self.parent[x] = self.find(self.parent[x])
        return self.parent[x] 
    
    
