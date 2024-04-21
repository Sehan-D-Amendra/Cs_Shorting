def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort both halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    left_idx, right_idx = 0, 0

    # Merge the two halves while there are elements in both
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1

    # Add any remaining elements from the left and right halves
    merged.extend(left[left_idx:])
    merged.extend(right[right_idx:])

    return merged

# Example usage:
arr = [12, 6, 7, 8, 10, 2, 9]
print("Before sorting:", arr)

sorted_arr = merge_sort(arr)
print("After sorting:", sorted_arr)
