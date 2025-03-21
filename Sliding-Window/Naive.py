def sum(arr, n, k):
    max_sum = 0
    for i in range(n - k + 1):
        current_sum = 0
        for j in range(k):
            current_sum += arr[i + j]
        max_sum = max(current_sum, max_sum)

    return max_sum

arr = [1, 4, 2, 10, 2,
       3, 1, 0, 20]
k = 4
print(sum(arr, len(arr), k))
