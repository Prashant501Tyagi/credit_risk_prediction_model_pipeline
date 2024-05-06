def subarrays_with_sum(arr, target_sum):
    result = []  # Initialize an empty list to store subarrays with the target sum
    window_sum = arr[0]  # Initialize the window sum with the first element of the array
    start = 0  # Initialize the start pointer of the sliding window

    # Iterate through the array using a sliding window approach
    for end in range(1, len(arr)):
        # Add the current element to the window sum
        window_sum += arr[end]

        # If the window sum equals or exceeds the target sum, add the subarray to the result
        while window_sum >= target_sum:
            if window_sum == target_sum:
                result.append(arr[start:end + 1])  # Add the subarray from start to end to the result

            # Move the window's start to the right and adjust the window sum
            window_sum -= arr[start]
            start += 1

    return result  # Return the list of subarrays with the target sum

# Example usage
arr = [2, 3, 1, 2, 4, 3]
target_sum = 7
print("Subarrays with sum 7:", subarrays_with_sum(arr, target_sum))
