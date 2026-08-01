def majorityEle(givennums):
    givennums.sort()
    majorityElement = givennums[0]
    maxcount = 1
    count = 1
    for i in range(len(givennums) -1):
        if givennums[i] != givennums[i+1]:
            if maxcount < count:
                majorityElement = givennums[i]
                maxcount = count
            count = 1
        else: 
            count +=1
    if maxcount < count:
        majorityElement = givennums[-1]
    return majorityElement

def majorityWin(nums):
    majorityWinner = -1
    votes =0
    for i in nums:
        if votes == 0:
            majorityWin=i
            votes =1
        elif i == majorityWin:
            votes+=1
        else:
            votes -= 1
    votes = 0

    for i in nums:
        if i == majorityWin:
            votes += 1
    if votes > len(nums)//2:
        return majorityWin
    return "Their is no majority element"


nums = [2,2,1,1]
givennums = [1,2,2,1,3,1,2,1,1,5,3,122,2,2,2,2,2]
print(majorityEle(givennums))
print(majorityWin(nums))