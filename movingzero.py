#Moving zeros to the end
arr=[1,0,2,0,3]
i=0
for j in range(0,len(arr)):
    if arr[j]==0:
        i=j
        break
for j in range(i+1,len(arr)):
    if arr[j]!=0:
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
print(arr)
