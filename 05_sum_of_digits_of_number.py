def sum_of_digits(n):
    return sum(int(digit) for digit in str(abs(n)))

# Example
num = 12345
print(f"Sum of digits of {num}: {sum_of_digits(num)}")
