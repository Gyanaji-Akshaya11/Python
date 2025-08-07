#second largest element in the array
arr=[12,35,1,34,1]
sec_largest=float("-inf")
largest=float("-inf")
for i in range(0,len(arr)):
    if arr[i]>largest:
        sec_largest=largest
        largest=arr[i]
    elif arr[i]<largest and arr[i]>sec_largest:
        sec_largest=arr[i]
print(sec_largest)

