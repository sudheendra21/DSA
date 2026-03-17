class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l = 0
        r = len(numbers)-1

        while l < r:
            if numbers[l]+numbers[r] == target:
                return [l+1,r+1]
            
            if numbers[l]+numbers[r] > target:
                r = r-1
            else:
                l = l+1
        return []

'''

Straight Forward Approach :
- Use two pointers, one at the start and one at the end
- If the sum is greater than target, move the right pointer to the left
- If the sum is less than target, move the left pointer to the right
- If the sum is equal to target, return the indices

Time Complexity : O(n)
Space Complexity : O(1)

'''
                

   


        