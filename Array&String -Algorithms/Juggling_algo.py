from math import gcd 

def rotate(arr,d):
    n=len(arr)
    gcdVal=gcd(n,d%n)

    for i in range(gcdVal):
        temp=arr[i]
        j=i
        while True:
            k=(j-d)%n
            if k==i:
                break
            
            arr[j]=arr[k]
            j=k
        arr[j]=temp
    return arr

arr=[1,2,3,4,5]
print(rotate(arr,3))