#სავარჯიშო1

# average = lambda a, b: (a+b)/2
#
#
# print("Average of those numbers is", average(float(input("Please type the first number: ")), float(input("Please type the second number: "))))

#სავარჯიშო2

# average = lambda a, b: print("Average of", a, "and", b, "is", (a+b)/2, ".")
#
# average(5, 9)
# average(16, 5)
# average(705, 546)

#სავარჯიშო3

# def cube(a): return pow(a, 3)
#
# print("3-rd power of 4 is", cube(4))
# print("3-rd power of 18 is", cube(18))
# print("3-rd power of 43 is", cube(43))
# print("3-rd power of 161 is", cube(161))

#სავარჯიშო4

# def minimal(a, b):
#     if a > b: return b, "is lower."
#     elif b > a: return a, "is lower."
#     elif a == b: return "Those numbers are the same."
#
# print(minimal(4, 7))
# print(minimal(9, 9))
# print(minimal(96, 40))

#სავარჯიშო5

# def isOdd(a):
#     if a % 2 == 0: return False
#     elif a % 2 == 1: return True
#
# print("4:", isOdd(4))
# print("9:", isOdd(9))
# print("0:", isOdd(0))

#სავარჯიშო6

# def fact(a):
#     fact = 1
#     for each in range (1, a+1):
#         fact *= each
#     return fact
#
# print("8!=", fact(8))
# print("12!=", fact(12))
# print("3!=", fact(3))

#სავარჯიშო7

# -----------

#სავარჯიშო8

# def printhw():
#     print("Hello World!")
#
# print(hw())

#სავარჯიშო9

# cube = lambda a: pow(a, 3)
#
# print("3-rd power of 4 is", cube(4))
# print("3-rd power of 12 is", cube(12))
# print("3-rd power of 162 is", cube(162))

#სავარჯიშო10

# def isPrime(a):
#     n = 0
#     for each in range(2, a):
#         if a % each == 0:
#             n += 1
#     if n == 0: return "is Prime Number."
#     else: return "is Composite Number."
#
# print("9", isPrime(9))
# print("5", isPrime(5))
# print("81", isPrime(81))

from random import uniform
print(round(uniform(100, 120), 1))