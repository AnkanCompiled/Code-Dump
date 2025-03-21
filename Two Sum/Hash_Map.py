def two_sum(arr, target):
    num_map = {}
    for i, num in enumerate(arr):
        complement = target - num
        if complement in num_map:
            return [complement, arr[i]]
        num_map[num] = i
    return False

if __name__ == "__main__":
    arr = [0, -1, 2, -3, 1]
    target = -2

    value = two_sum(arr, target)
    if value == False:
        print("No such pair found")
    else:
        print(f"Pair: {value}")