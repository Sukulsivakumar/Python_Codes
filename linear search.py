def search(arr,x):
 
    for i in range(len(arr)):
 
        if arr[i] == x:
            return i
 
    return -1
arr=list(map(int,input("ENTER THE ELEMENTS: ").split(" ")))
x=int(input("Number:"))
r=search(arr,x)
if r==-1:
    print("Element Not Found")
else:
    print("Element at Index: ",r)