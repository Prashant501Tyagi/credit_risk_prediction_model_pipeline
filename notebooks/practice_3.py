def max_element_subarray(arr) -> list:
    count_dict = {}  # Dictionary to store the count of each element
    max_count = 0  # Variable to store the maximum count
    max_elements = []  # List to store elements with the maximum count

    for i in arr:
        count_dict[i] = count_dict.get(i,0) + 1
        max_count = max(count_dict[i],max_count)
    for num, count in count_dict.items():
        if max_count == count:
            max_elements.append(num)
    return max_elements
    
# Input array
arr = [int(input("Enter the number: ")) for _ in range(int(input("Enter the length of the array: ")))]

# Call the function to find the most repeated number(s) in the array
result = max_element_subarray(arr)
print("The most repeated number(s) in the array:", result)
