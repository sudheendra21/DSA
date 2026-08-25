class IterativePostOrder:
    def postorder(self, root):
        if not root:
            return []
        stk = [root]
        res = []
        while stk:
            curr = stk.pop()
            res.append(curr.val)
            if curr.left:        # left first
                stk.append(curr.left)
            if curr.right:       # right pops first
                stk.append(curr.right)
        return res[::-1]

#so  basically we are doing root right left and reversal of which is left right root - which is postorder