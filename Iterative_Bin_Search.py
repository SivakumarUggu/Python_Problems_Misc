def bin_search(arr,lower,upper,k):
    while lower<=upper:
         mid=lower+(upper-lower)//2
         if k==arr[mid]:
               return mid
         elif k>arr[mid]:
                lower=mid+1
         else:
                upper=mid-1


arr=[2,3,4,10,40]
k=int(input('Enter value you want to search in an array: '))
result=bin_search(arr,0,len(arr)-1,k)
print(f'index of {k} in given array is: {result}')

