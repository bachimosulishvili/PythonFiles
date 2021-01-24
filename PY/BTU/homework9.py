#                       სავარჯიშო1


# numb = [6, 64, 41, 9, 165]
#
# print('Numbers:\n \t', numb)
#
# print('Sum: ', sum(numb))
# print('Min: ', min(numb))
# print('Max: ', max(numb))
# print('Avg: ', sum(numb)/len(numb))
# print('\n')
#
# print('Appended 102:')
# numb.append(102)
# print(numb, '\n')
#
# print('Inserted 205 as 3-rd number:')
# numb.insert(2, 205)
# print(numb, '\n')
#
# print('Popped 4-th element:')
# numb.pop(3)
# print(numb, '\n')
#
# print('Sorted:')
# numb.sort()
# print(numb)

# -------------------------------------------------

#                       სავარჯიშო2


# numb = []
#
# for each in range(10): numb.append(int(input('Type number: ')))
#
# print(numb)

# --------------------------------------------------

#                       სავარჯიშო3

# fruits = ['Watermelon', 'Banana', 'Apple']
#
# print(fruits)
#
# fruits.sort()
# fruits.reverse()
#
# print('Sorted:\n', fruits)

# --------------------------------------------------

#                      სავარჯიშო4


# def multiply(arguments):
#     res = 1
#     for each in arguments:
#         res *= each
#     return res
#
#
# listExample = [64, 651, 49, 854, 84, 15, 849]
#
# print('List:', listExample, '\nProduct: ', multiply(listExample))

# --------------------------------------------------

#                      სავარჯიშო5

#
# numbers = [54, 845, 31, 96, 34, 546, 187]
# res = []
#
# for each in numbers:
#     if each % 2 == 0: res.append(each)
#
# print('Even numbers are:\n', res)

# --------------------------------------------------

#                      სავარჯიშო6


# numbers = [64, 26, 31, 356, 10]
# res = []
#
# for each in numbers:
#     each += 10
#     res.append(each)
#
# print('Result is:\n', res)

# --------------------------------------------------

#                      სავარჯიშო7


# import random
#
# numbers = []
#
# for each in range(10):
#     numbers.append(random.randint(25, 110))
#
# print('List:\n\t', numbers, '\nMin: ', min(numbers))

# --------------------------------------------------

#                      სავარჯიშო8


# def mutual(list1, list2):
#     for each1 in list1:
#         for each2 in list2:
#             if each1 == each2:
#                 return True
#             else:
#                 return False
#
#
# listExample1 = [132, 124, 513, 21, 42]
# listExample2 = [123, 15, 21, 245, 24]
#
# print('Returned value is: ', mutual(listExample1, listExample2))

# --------------------------------------------------

#                      სავარჯიშო9


# def removeodd(list):
#     res = []
#     for each in list:
#         if each % 2 == 0:
#             res.append(each)
#     return res
#
# listExample = [31, 516, 64, 99, 496, 856]
# print(removeodd(listExample))
