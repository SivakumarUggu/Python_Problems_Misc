def bin_search(arr,lower,upper,k):
    mid=lower+(upper-lower)//2
    if k==arr[mid]:
        return mid
    elif k<arr[mid]:
        return bin_search(arr,lower,mid-1,k)
    else:
        return bin_search(arr,mid+1,upper,k)

arr=[2,3,4,10,40]
k=int(input('Enter value you want to search in an array: '))
result=bin_search(arr,0,len(arr)-1,k)
print(f'index of {k} in given array is: {result}')

