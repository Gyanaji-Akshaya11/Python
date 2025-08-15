#Sort 0s, 1s and 2s
arr=[0, 1, 2, 0, 1, 2]
lst=[]
mini=min(arr)
maxi=max(arr)
for i in range(0,len(arr)):
    if arr[i]==mini:
        lst.append(arr[i])
for i in range(0,len(arr)):
    if arr[i]!=mini and arr[i]!=maxi:
        lst.append(arr[i])
for i in range(0,len(arr)):
    if arr[i]==maxi:
        lst.append(arr[i])
print(lst)

        

    