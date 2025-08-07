#reverse an array
arr=[1,2,3,4,5,6,7,8,9,0]
n=len(arr)
m=n//2
j=0
for i in range(n-1,m-1,-1):
    arr[i],arr[j]=arr[j],arr[i]
    j+=1
print(arr) 