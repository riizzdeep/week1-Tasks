def reverse_number(n):
    return int(str(abs(n))[::-1]) * (-1 if n < 0 else 1)

# Example
num = 12345
print(f"Reversed: {reverse_number(num)}")
