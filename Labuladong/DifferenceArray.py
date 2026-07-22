#We can pass the nums array as input to construct the difference array
class Difference:
    def __init__(self,nums):
        assert len(nums)>0
        self.diff = [0]*len(nums)
        self.diff[0] = nums[0]
        for i in range(1,len(nums)):
            self.diff[i] = nums[i]-nums[i-1]

    #function handling range addition/subtraction
    def increment(self,i,j,val):
        self.diff[i] += val
        if j+1 < len(self.diff):
            self.diff[j+1] -= val
   
    #how do you compute original array from result array
    def result(self):
        res = [0]*len(self.diff)
        res[0] = self.diff[0]
        for i in range(1,len(self.diff)):
            res[i] = res[i-1]+self.diff[i]
        return res
        
        
        

        
            
        
