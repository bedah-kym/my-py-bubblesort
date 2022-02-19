''' here we make a marker with an outer loop to split into sorted and unsorted
then an inner loop to sort the arry on the left after each iteration'''

lst=[25,4,56,7,5,4,3,1,20]
def insertion_sort(lst):
    for x in range(1,len(lst)):
        i=x
        while lst[i] < lst[i-1] and i>0:# this loops swaps untill the left array is sorted
            lst[i],lst[i-1]=lst[i-1],lst[i]
            i-=1
    return lst        
print("insertion_sort",insertion_sort(lst))        


"""
its simple just run a loop to find the smallest then
add the smallest to a NEW list and remove it from the 
old list and loop again untill the old list is empty
"""
lst=[25,4,56,7,5,4,3,1,20]
new=[]

def selection_sort(nums,new):
    n= len(nums)
    for y in range(0,n):#outer loop runs (n) times 'n' is no of elements in the list
        smallest=lst[0]
        
        for x in nums:#iterate nums[] to find the smallest each time the outer runs once
            if x < smallest:
                smallest=x
                
        nums.remove(smallest)
        print(lst,'.......->',new)
        new.append(smallest)
    return new
        
print("this is selection_sort",selection_sort(lst,new),'\n')

            #space
            
lst=[25,4,56,7,5,4,3,1,20]

def bubble_sort(nums):
    n= len(nums)
    for x in range(0,n):
        for i in range (1,n):
            print (nums)
            if nums[i-1] > nums[i]:
                temp=nums[i]
                nums[i]=nums[i-1]
                nums[i-1]=temp
                
            elif nums[i-1] <= nums[i]:
                pass
    return nums
        
print(" this is bubble",bubble_sort(lst))
        
    
    
    
