class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        for i in range(len(nums)):
            if i > max_reach:
                return False
            else:
                max_reach = max(max_reach,i+nums[i])
        return True
        
                    

''' 
Time Complexity : O(n)
Space Complexity : O(1)
The first thought that comes to mind is to use a top down backtracking approach using memoization, but that would be too expensive.
'''