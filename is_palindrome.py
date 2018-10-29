def is_palindrome(n):
    N = str(n)
    if N == N[::-1]:
        return n

it = range(200)

it = list(filter(is_palindrome,it))

print(it)
