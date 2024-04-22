def max_subarray(nums):
    max_sum = float('-inf')  # Initialize max_sum to negative infinity
    current_sum = 0  # Initialize current_sum to 0

    for num in nums:
        current_sum = max(num, current_sum + num)  # Update current_sum
        max_sum = max(max_sum, current_sum)  # Update max_sum

    return max_sum

# Example usage:
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = max_subarray(arr)
print(f"The maximum subarray sum is: {result}")
