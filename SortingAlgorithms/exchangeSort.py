
arr = [12,3,419,0,-1,16,8,2,1,8,9,110]

n = len(arr)



#lets try doing selection sort

for i in range(n-1):
    for j in range(i+1,n):
        if arr[i] > arr[j]:
            a = arr[i]
            arr[i] = arr[j]
            arr[j] = a
#after every pass the smallest comes at the first

print(arr)
        