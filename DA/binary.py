def binary_search(arr, target, low, high):
    if high >= low:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binary_search(arr, target, low, mid - 1)
        else:
            return binary_search(arr, target, mid + 1, high)
    else:
        return -1


try:
    arr = list(map(int, input("Enter a sorted array of numbers (separated by spaces): ").split()))
    target = int(input("Enter the target number to search for: "))

    result = binary_search(arr, target, 0, len(arr) - 1)

    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found in array")
except ValueError:
    print("Invalid input! Please enter numbers only.")
