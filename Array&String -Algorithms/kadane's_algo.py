def kadane(arr):
    current_sum = 0
    max_sum = float('-inf')

    for x in arr:
        current_sum += x

        max_sum = max(max_sum, current_sum)

        if current_sum < 0:
            current_sum = 0

    return max_sum

# Test
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(kadane(arr))  