n=int(input())
arr1=[int(x) for m in input().split()]
m=int(input())
arr2=[int(x) for n in input().split()]

for i in range(len(arr1)):
    for j in range (len(arr2)):
        if arr1[i]==arr2[j]:
            print(arr[i])
            arr2[j]=-1
            break
        
