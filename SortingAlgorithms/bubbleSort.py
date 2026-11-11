
arr = [12,3,419,0,-1,16,8,2,1,8,9,110]

n = len(arr)



for j in range(n-1):
#Bubble sort for ascending order
    for i in range(n-1-j):
    
        if arr[i] > arr[i+1]:
            #Now we did the swap though
            a = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = a
print(arr)
        
        
#Notes on bubble sort: 
#Time Complexity: O(n^2)
#Space Complexity: O(1)

#In bubble sort after every pass we place the largest element at its correct position
#so we do only comparisions till the remaining