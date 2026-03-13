class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        #Have a set
        nums_set = set(nums)
        max_count = 1
        running_max = 1

        for a in nums_set:
            
            if a-1 not in nums_set:
                while a+1 in nums_set:
                   running_max = running_max+1
                   
                   a = a+1
                max_count = max(running_max,max_count)



                   
           
            
            running_max = 1
        return max_count







        


        