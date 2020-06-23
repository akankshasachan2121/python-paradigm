# Initializing array
array=[42,5,50,12,3,7,0,2,9,1,25,10]

#Swaping of two elements a and b
def swap(array,a,b):
    print("swaping", array[a],array[b])
    temp=array[a]
    array[a]=array[b]
    array[b]=temp

#SELECTION SORT
def selection(array):
    print("SELECTION SORT")
    n=len(array)
    for i in range(n):
        min_el=array[i]
        j=i+1
        while j<n:
            if array[j]<min_el:
                swap(array,i,j)
                min_el=array[i]
            j+=1   
        print("iteration: ",i+1)
        print(array)
        
#BUBBLE SORT
def bubble(array):
    print("BUBBLE SORT")
    n=len(array)-1
    for i in range(n):
        j=0
        while j!= n-i:
            if array[j]>array[j+1]:
                swap(array,j,j+1)
            j+=1
        print("iteration: ",i+1)
        print(array)  
    
#INSERTION SORT
def insertion(array):
    print("INSERTION SORT")
    n=len(array)
    for i in range(1,n):
        j=i-1                                   # considering the array to be sorted till jth index
        while j>=0:                             # finding the position where ith element is to be inserted
            
            if array[i]<array[j]:
                j-=1
            elif array[i]>array[j]:
                break
                
        if j<i-1:                              # if the ith element is not in ascending order then begin insertion
            key=array[i]
            k=i
            while k>j+1:                       #shifting all the elements from jth position to ith position
                print("shifting",array[k-1],end=" ")
                print("to poisition",k)
                array[k]=array[k-1]
                k-=1
                
            array[j+1]=key                     #replacing jth position with the ith element to complete insertion
        print("iteration: ",i)
        print(array) 
        
#MERGE SORT
def merge(arr):
    
    # splitting the array
    
    print("array to be split",arr)
    divide= len(arr)//2
    if divide==0:
         return arr                   # return the array when it cannot be further divided
    elif divide>0:
        left=arr[:divide]             #split the array and save the left
        if len(arr)!=3:               # for when array is odd([5,2,9]),do not split the left subarray further
            left= merge(left)         #recursively call merge() until further splitting of array is not possible
        right=arr[divide:]            #split the array and save the right
        right=merge(right)            #recursively call merge() until further splitting of array is not possible
    print("left array to be merged",left)
    print("right array to be merged",right)
    i=0
    j=0
    sorted_array=[]                       # assign all the sorted elements in a new array
    
    #merging two sorted arrays
    
    while  i<len(left) and j<len(right) : #appends elements to sorted array as long as the smaller array gets over
        
        if left[i]>right[j]:
            sorted_array.append(right[j])
            j+=1
        elif left[i]<right[j]:
            sorted_array.append(left[i])
            i+=1
    if i<len(left):                      # if there are remaining elements in the larger array,they get appended at the end
        sorted_array.extend(left[i:])
    elif j<len(right):
        sorted_array.extend(right[j:])
        
    print("merged aray",sorted_array)
    return sorted_array

#Creating divide method
def divide(arr,low,high):
    key=arr[high] 
    print("pivot", key)
    i=low
    j=low
    while j<=high:
        
        if arr[j]<=key :
            swap(arr,i,j)
            i+=1
            
        j+=1
    print("sorted array ",arr)
    return i-1

#QUICK SORT
def quick(array,low=0,high=(len(array)-1)):
    
        print("array to be sorted: ",array[low:high+1])
        if low>=high :
            return
        pivot= divide(array,low,high)
        quick(array,low,pivot-1)
        quick(array,pivot+1,high)
        
   
    
    
#main function
print(array)

print("\n1.Selection sort\n2.Bubble sort\n3.Insertion sort\n4.Merge sort\n5.Quick sort")

sort=int(input("Sorting method: "))

if sort ==1:
    selection(array)
elif sort==2:
    bubble(array)
elif sort==3:
    insertion(array)
elif sort==4:
    merge(array)
elif sort==5: 
    quick(array)
else:
    print("invalid entry")

