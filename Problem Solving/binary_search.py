def binary_search(arr,target):
    left =0
    right = len(arr)-1
    while left<=right:
        mid = (left+right)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid+1
        else:
            right = mid -1
    return -1

if __name__ == '__main__':
    arr = list(map(int,input().split()))
    target = int(input())
    print(binary_search(arr,target))

"""
output:
10 20 25 33 34 35 48 52 61
35
5

=== Code Execution Successful ===
"""