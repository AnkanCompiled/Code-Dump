def two_sum(arr, target):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
                return [arr[i], arr[j]]
    return False

arr = [0, -1, 2, -3, 3]
target = 9

value = two_sum(arr, target)

if value == False:
    print("No such pair found")
else:
    print(f"Pair: {value}")
