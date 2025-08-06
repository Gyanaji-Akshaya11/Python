arr=[2,-3,4,1,1,7]
arr.sort()
res=1
for i in range(0,len(arr)):
    if arr[i]==res:
        res+=1
    if arr[i]<res:
        continue
    elif arr[i]>res:
        print(res)
        break
