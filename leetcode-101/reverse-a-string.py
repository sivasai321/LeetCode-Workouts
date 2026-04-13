# https://leetcode.com/problems/reverse-string/


def reverse_string(s):
    return s[::-1]


def reverse_string_in_place(s):
    left, right = 0, len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

    return s

s = ["h","e","l","l","o"]

print(reverse_string(s))
print(reverse_string_in_place(s))
