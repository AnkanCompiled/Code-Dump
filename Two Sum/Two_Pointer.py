def two_sum(arr, target):
    arr.sort()
    left, right = 0, len(arr) - 1
    while left < right:
        sum = arr[left] + arr[right]
        if sum == target:
            return [arr[left], arr[right]]
        elif sum < target: 
            left += 1
        else:
            right -= 1
    return False

if __name__ == "__main__":
    arr = [0, -1, 2, -3, 1]
    target = -2
    value = two_sum(arr, target)
    if value == False:
        print("No such pair found")
    else:
        print(f"Pair: {value}")

