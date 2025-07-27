PI = 3.14159

def circle_area(r):
    return PI * r * r

def rect_area(w, h):
    return w * h

def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a