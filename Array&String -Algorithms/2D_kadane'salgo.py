
import sys
def kadanealgo(givenNums):
    start=0
    end=0

    current_sum=0
    max_sum=-sys.maxsize -1

    n=len(givenNums)

    while end<n:
        while current_sum<0:
            current_sum-=givenNums[start]
            start+=1
        
        current_sum+=givenNums[end]
        end+=1
        
        max_sum=max(max_sum,current_sum) 
    return max_sum

matrix = [
    [1, 2, -1, -4, -20],
    [-8, -3, 4, 2, 1],
    [3, 8, 10, 1, 3]]

n= len(matrix)
m=len(matrix[0])
ans=-sys.maxsize -1

for i in range(m):
    temp=[]
    for j in range(n):
        temp.append(matrix[j][i])
    print(temp)
    ans =max(ans,kadanealgo(temp))
    print(ans)

    for j in range(i+1,m):
        for k in range(n):
            temp[k]+=matrix[k][j]
        print(temp)
        ans =max(ans,kadanealgo(temp))
        print(ans)
    print('---------------------------------------------------------------')

print(ans)
