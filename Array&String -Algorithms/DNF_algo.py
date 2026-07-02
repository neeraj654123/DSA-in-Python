def DNF_sort(given_nums):
    low=0
    mid=0
    high=len(given_nums)-1

    while mid<=high:
        if given_nums[mid]==0:
            given_nums[low],given_nums[mid]=given_nums[mid],given_nums[low]
            low+=1
            mid+=1
        elif given_nums[mid]==1:
            mid+=1
        else:
            given_nums[high],given_nums[mid]=given_nums[mid],given_nums[high]
            high-=1
    return given_nums

print(DNF_sort([2,0,1,0,1,2]))
