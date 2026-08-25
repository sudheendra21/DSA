#when we think of tree traversals we usually think recursively , but we can also do it iterative way 
#Iterative is not just for Level order traversals , even pre order , post order , in order can be done iteratively
class IterativeInOrder:
    def IterativeInorder(self,root):
        stk = []
        curr = root
        res = []
        
        while curr or stk :
            while curr:
                stk.append(curr)
                curr = curr.left
            curr = stk.pop()
            res.append(curr.val)
            curr = curr.right
        
        return res
            
            
        
        
        
        