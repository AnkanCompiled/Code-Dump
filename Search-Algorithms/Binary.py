def BinarySearch(arr, k, low, high):
    if high >= low:

        mid = low + (high - low)//2

        if arr[mid] == k:
            return mid

        elif arr[mid] > k:
            return BinarySearch(arr, k, low=low, high=mid-1)

        else:
            return BinarySearch(arr, k, low=mid + 1, high=high)
    else:
        return -1


arr = []
n = int(input("Enter number of elements: "))

av = ["st", "nd", "rd"]

print("Enter elements in sorted order..")
for i in range(0, n):
    ele = int(input(f"Enter {i+1}{av[i] if len(av) > i else "st"} element: "))
    arr.append(ele)

k = int(input("Enter element to search: "))

result = BinarySearch(arr, k, 0, len(arr)-1)

if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")