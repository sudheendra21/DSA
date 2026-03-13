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


"""Okay
March 12 2026

I did solve it on my own , but its not optimal 
and I solved it after correcting multiple times

Ideal Case - solving 

key concepts:
Duplicate Check while traversing towards right

Two crucial concepts involved :
Duplicate check while traversing right , Duplicate check while traversing left 

you get really confused for i == i+1 and i-1 == i -> practice this a bit


March 12 2026 :

With great help , I came up 
Important Observations - how while inside for loop does not make it O(n2)  Automatically

"""




        


        