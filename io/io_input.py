def reverse(text):
    return text[::-1]


def tolower(text):
    t = ''
    for c in text:
        if 'A' <= c <= 'z':
            t = t + c.lower()
    return t


def is_palindrome(text):
    return tolower(text) == reverse(tolower(text))


something = input("Enter text:")
if is_palindrome(something):
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")
