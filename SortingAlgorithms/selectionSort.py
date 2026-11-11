'''Selection Sort Algorithm
Time complexity - 
Space complexity - 
In-place - 
'''

#selection sort is an optimization over exchange sort
arr = [12,3,419,0,-1,16,8,2,1,8,9,1111]

n = len(arr)



#lets try doing selection sort

for i in range(n-1):
    min_index = i
    for j in range(i+1,n):
        if arr[min_index] > arr[j]:
           min_index = j 
    arr[i],arr[min_index] = arr[min_index],arr[i]
#after every pass the smallest comes at the first

print(arr)
            


