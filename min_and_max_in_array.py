#finding the minimum and maximum element in the array
arr= [3, 2, 1, 56, 10000, 167]
mini=float("inf")
maxi=float("-inf")
for i in range(0,len(arr)):
    if arr[i]>maxi:
        maxi=arr[i]
    if arr[i]<mini:
        mini=arr[i]
print(mini,maxi)
        
    