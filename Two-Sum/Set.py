def two_sum(arr, target):
    s = set()
    for num in arr:
        complement = target - num
        if complement in s:
            return True
        s.add(num)
    return False

arr = [0, -1, 2, -3, 1]
target = -2

if __name__ == "__main__":
    arr = [0, -1, 2, -3, 1]
    target = -2

    if two_sum(arr, target):
        print("Pair Found")
    else:
        print("No such pair found")
        
