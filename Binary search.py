def bS(arr, x, low, high):
    while low <= high:
        mid = low + (high - low)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1
arr=list(map(int,input("ENTER THE ELEMENTS: ").split(" ")))
x=int(input("Number:"))
r= bS(arr, x,0,len(arr)-1)
if r == -1:
    print("Not found")
else:
      print("Element is present at index " + str(r))
  