# Given an array of integers, find the sum of its elements.

# For example, if the array arr [1,2,3],[1+2+3]=6 , so return 6.

def simpleArraySum(arr):
    # Write your code here
    total = 0
    for num in arr:
        total += num
    return total

arr = [1, 2, 3]
result = simpleArraySum(arr)
print("Sum of array elements:", result)