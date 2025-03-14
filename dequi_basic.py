# tinh gia thua

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(5))

#tinh tong tu 1 den n
def sum_n(n):
    if n == 1: 
        return 1
    return n + sum_n(n-1)

print(sum_n(5))


# tim fibonacci
def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    memo[n] = fibonacci(n-1) + fibonacci(n-2)
    return memo[n]

print(fibonacci(6))

#GCD (a,b)

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)

print(gcd(48,18))

# tinh  a^b
def power_ab(a,b):
    if b == 0:
        return 1
    return a * power_ab(a,b-1)

print(power_ab(2,4))

# dao chieu chuoi bang dequi
def reverse_str(str):
    if len(str) == 0:
        return str
    return reverse_str(str[1:]) + str[0]

print(reverse_str('hello'))

# kiểm tra palindrome

def is_palindrome(str):
    if len(str) == 1 or str =='':
        return True
    if str[0] != str[-1]:
        return False
    return is_palindrome(str[1:-1])                                                                                                                                                                                                                                                                                                                                                                                                                         

print(is_palindrome('madam'))