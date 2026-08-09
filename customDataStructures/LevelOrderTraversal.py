from collections import deque
class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        
    def levelOrderTraversal(self,node):
        if node == None:
            return []
        q = deque()
        #now how to populate the queue ?
        q.append(node)
        res = []
        
        while q:
            #something to do with length man , how do you differentiate each level?
            level = []
            for i in range(len(q)):
                n = q.popleft()
                level.append(n.val)
                l = n.left
                r = n.right
                if l is not None:
                    q.append(l)
                if r is not None:
                    q.append(r)
            res.append(level)
        return res
                
            
        
        
        




