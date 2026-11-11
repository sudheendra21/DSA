#Insertion sort


#Insertion Sort works on idea that there is a sorted bytearray
#and there is unsorted array 
#we take each element from unsorted array 
# and place it in sorted array

#so we always start with 1 assuming , element at 
#0th index is sorted

#And remember how insertion  actually works ?

#It kind of copies the same element 

array = [-1,2,4,0,6,2,-1,9,19,-99]

#insertion sort

n = len(array)

for i in range(1,n):
    #array is sorted till i(inclusive)
    key = array[i]
    
        #we need to insert element j 
        #here we get boundary issue 
    j = i-1   
    while j>=0 and array[j] > key:
        array[j+1] = array[j]
        j = j-1
    array[j+1] = key
print(array)
            
        
        
    