"""Binary search iterative.
Time: O(log N).
"""


def binary_search(arr, x):
    """Returns the index of x in a sorted list arr.
    Returns -1 if x is not present.
    """
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = int ((low+high) / 2)
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

if __name__ == '__main__':
    # Enter a space-separated list of numbers, followed by the number to search.
    arr = list(map(int, input().rstrip().split()))
    x = int(input())
    found = binary_search(arr, x)
    print("Found at index %d" %found) if found > -1 else print("Not found")
