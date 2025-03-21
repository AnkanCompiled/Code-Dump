def binary_search(arr, left, right, target):
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

def two_sum(arr, target):
    arr.sort()
    for i in range(len(arr)):
        # Find the complement of the current element, like for target 9, complement of 2 is 7 (9-2)
        complement = target - arr[i]
        if binary_search(arr, i + 1, len(arr) - 1, complement):
            return [arr[i], complement]
    return False
      
if __name__ == "__main__":
    arr = [0, -1, 2, -3, 1]
    target = -2

    value = two_sum(arr, target)
    if value == False:
        print("No such pair found")
    else:
        print(f"Pair: {value}")

