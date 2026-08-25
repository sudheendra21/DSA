#when we think of tree traversals we usually think recursively , but we can also do it iterative way 
#Iterative is not just for Level order traversals , even pre order , post order , in order can be done iteratively
class IterativePreOrder:
    def preorder(self, root):
        if not root:
            return []
        stk = [root]
        res = []
        while stk:
            curr = stk.pop()
            res.append(curr.val)
            #Notice in iterative approach we are pushing right first in our manual stack
            if curr.right:      
                stk.append(curr.right)
            if curr.left:       
                stk.append(curr.left)
        return res
        
            
            
        
        
        
        