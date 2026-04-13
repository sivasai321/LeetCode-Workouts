# https://leetcode.com/problems/palindrome-number/description/

def isPalindrome_string(x):
    if x < 0:
        return False

    return str(x) == str(x)[::-1]

def isPalindrome_integer(x):
    if x < 0:
        return False

    original = x
    reversed = 0

    while x > 0:
        reversed = reversed * 10 + x % 10
        x //= 10

    return original == reversed

x=int(input("Enter a number: "))

print(isPalindrome_string(x))
print(isPalindrome_integer(x))