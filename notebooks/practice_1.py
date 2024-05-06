def multiple(number_output: int) -> int:
    result = 0  # Initialize result with 1
    for i in range(1, 11):
        sum_output = number_output * i # Multiply the current result with the next number_output
        result += sum_output
    return result

print(multiple(2))




