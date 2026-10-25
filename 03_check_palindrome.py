def is_palindrome(n):
    s = str(abs(n))
    return s == s[::-1]

# Example
num = 121
print(f"{num} is palindrome: {is_palindrome(num)}")
