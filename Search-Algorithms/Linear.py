def LinearSearch(array, n, k):
    for j in range(0, n):
        if (array[j] == k):
            return j
    return -1

array = []
n = int(input("Enter number of elements: "))

av = ["st", "nd", "rd"]

for i in range(0, n):
    ele = int(input(f"Enter {i+1}{av[i] if len(av) > i else "st"} element: "))
    array.append(ele)

k = int(input("Enter element to search: "))


result = LinearSearch(array, n, k)

if(result == -1):
    print("Element not found")
else:
    print("Element found at index: ", result)