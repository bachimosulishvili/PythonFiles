# სავარჯიშო1

# n = 20
#
# while n <= 125:
#     print(n)
#     n += 5

# სავარჯიშო2

# n = 200
#
# while n >= 25:
#     if n % 8 == 0:
#         print(n)
#     n -=1

# სავარჯიშო3

# n = 1500
#
# while n <= 2100:
#     if n % 5 == 0 and n % 7 == 0:
#         print(n)
#     n += 1

# სავარჯიშო4

# n = 1500
# sum = 0
#
# while n < 2100:
#     if n % 5 == 0 and n % 7 == 0:
#         sum += n
#     n += 1
#
# print("1500-დან 2100-ის ჩათვლით 7-ისა და 5-ის ჯერადი რიცხვების ჯამი არის", sum, ".")

# სავარჯიშო5

# n = 1500
# sum = 0
#
# while n < 2100:
#     if n % 5 == 0 and n % 7 == 0: sum += n
#     elif sum >= 20000: break
#     n += 1
#
#
# print("თქვენი მოთხოვნილი რიცხვია", sum)

# სავარჯიშო6

# n = 1500
# total = 0
#
# while n < 2100:
#     if n % 5 == 0:
#         n += 5
#         total += 1
#
# print("1500-დან 2100-ის ჩათვლით 5-ის ჯერად რიცხვთა რაოდენობა არის", total)

# სავარჯიშო7

# total = 0
# sum = 0
#
# while total < 10:
#     sum += int(input("გთხოვთ შეიყვანოთ რიცხვი: "))
#     total += 1
#
# print("მოცემული რიცხვების საშუალო არის ", sum/10)

# სავარჯიშო8

# n = 1
# sum = 0
#
# while n <= 100:
#     if n % 2 == 0:
#         sum += n
#     n += 1
# print("1-დან 100-ის ჩათვლით ლუწი რიცხვების ჯამი არის", sum)

# სავარჯიშო9

# n = 10
#
# while n < 145:
#     n += 5
#     if n == 50 or n == 75 or n == 80: continue
#     print(n)

# სავარჯიშო10

# inp = int(input("გთხოვთ შეიყვანეთ სასურველი რიცხვი: "))
# fact = 1
#
# for each in range (1, inp+1): fact *= each
# print(fact)

# სავარჯიშო11

# inp = int(input("გთხოვთ შეიყვანეთ სასურველი რიცხვი: "))
#
# for each in range (1, inp+1):
#     if inp % each == 0: print(each)

# სავარჯიშო12

# inp0 = abs(int(input("შეიყვანეთ პირველი რიცხვი: ")))
# inp1 = abs(int(input("შეიყვანეთ მეორე რიცხვი: ")))
#
# print("მოცემული რიცხვების საერთო გამყოფებია: ")
# for each in range (1, inp0+1):
#     if inp0 % each == 0 and inp1 % each == 0: print(each)

# სავარჯიშო13

# inp0 = int(input("შეიყვანეთ პირველი დადებითი რიცხვი: "))
# inp1 = int(input("შეიყვანეთ მეორე დადებითი რიცხვი: "))
# div = 1
#
# if inp0 < 0 or inp1 < 0: print("თქვენს მიერ შეყვანილი რიცხვ(ებ)ი უარყოფითია.")
#
# else:
#     for each in range(1, inp0 + 1):
#         if inp0 % each == 0 and inp1 % each == 0 and each > div: div = each
#
#     print("მოცემული რიცხვების უდიდესი საერთო გამყოფია: ", div)

# სავარჯიშო14
#
# inp0 = int(input("შეიყვანეთ პირველი დადებითი რიცხვი: "))
# inp1 = int(input("შეიყვანეთ მეორე დადებითი რიცხვი: "))
# div = 1
#
# if inp0 <= 0 or inp1 <= 0:
#     print("თქვენს მიერ შეყვანილი რიცხვ(ებ)ი უარყოფითია ან ნულია.")
# else:
#     for each in range(1, inp0 + 1):
#         if inp0 % each == 0 and inp1 % each == 0 and each > div: div = each
#     print("მოცემული რიცხვების უმცირესი საერთო ჯერადი არის ", int((inp0/div) * (inp1/div) * div))

# სავარჯიშო15

# inpCount = 1
# number = 0
#
# for each in range (1,11):
#     inp = int(input("გთხოვთ შეიყვანოთ რიცხვი: "))
#     if inp % 2 == 1 and inp > number:
#         inpCount += 1
#         number = number * 0 + inp
#
# if number == 0: print("თქვენს მიერ შეყვანილი რიცხვები ლუწია!")
# else: print("მოცემულ რიცხვებს შორის ყველაზე დიდი კენტი რიცხვია", int(number))

# სავარჯიშო16

# inp = int(input("გთხოვთ შეიყვანოთ რიცხვი: "))
# total = 0
#
# if inp > 1:
#     for each in range (2, inp):
#         if inp % each == 0: total += 1
#     if total == 0: print("ეს რიცხვი მარტივია.")
#     else: print("ეს რიცხვი შედგენილია.")
# else: print("მოცემული რიცხვი არც მარტივია და არც შედგენილი.")

# სავარჯიშო17

# for eachNum in range(2, 1000):
#     for each in range(2, eachNum):
#         if eachNum % each == 0:
#             break
#     else:
#         print(eachNum)

# სავარჯიშო18

# temp0 = 0
# temp1 = 1
#
# while temp0 < 100 and temp1 < 100:
#     if temp1 >= 100: break
#     else:
#         print(temp1)
#         temp0 += temp1
#         if temp0 >= 100: break
#         else:
#             print(temp0)
#             temp1 += temp0

#სავარჯიშო19

# num = int(input("შეიყვანეთ მთელი რიცხვი: "))
# Total = 0
#
# while True:
#     num = num // 10
#     Total += 1
#     if num == 0 or num == -1 : break
#
# print("ამ რიცხვში ციფრთა რაოდენობაა", Total)

#სავარჯიშო20

# num = abs(int(input("შეიყვანეთ მთელი რიცხვი: ")))
# x = 0
#
# while True:
#     x += num % 10
#     num = num // 10
#     if num == 0 or num == -1: break
# print("ამ რიცხვში ციფრთა ჯამია", x)

#სავარჯიშო21

# num = abs(int(input("შეიყვანეთ მთელი რიცხვი: ")))
# x = 0
#
# while True:
#     x = num % 10
#     num = num // 10
#     if num == 0 or num == -1: break
# print("ამ რიცხვში პირველი ციფრია", x)

#სავარჯიშო22

### შენიშვნა: როდესაც 0-ით დაწყებული რიცხვი შემყავს, მაგალითად 0166, წერს 661 ნაცვლად 6610-ისა. გთხოვთ შეამოწმოთ და მითხრათ რამდენად სწორია. ###

# num = abs(int(input("შეიყვანეთ მთელი რიცხვი: ")))
# x = 0
# y = 0
#
# while True:
#     x = num % 10
#     num = num // 10
#     y = y * 10 + x
#     if num == 0 or num == -1: break
# print("მოცემული რიცხვის შებრუნებული სახე არის", y)

#სავარჯიშო23

# inp = abs(int(input("შეიყვანეთ მთელი რიცხვი: ")))
# num = inp
# x = 0
# y = 0
#
# while True:
#     x = num % 10
#     num = num // 10
#     y = y * 10 + x
#     if num == 0 or num == -1: break
#
# if y == inp: print("+")
# else: print("-")

#სავარჯიშო24-ა

# print("* * * * *")
# print("*       *")
# print("*       *")
# print("* * * * *")
# print("*       *")
# print("*       *")
# print("* * * * *")

#სავარჯიშო24-ბ

# for each0 in range (1,5+1):
#     print(each0 * "*")
# for each1 in range(4, 0, -1):
#     print(each1 * "*")

#სავარჯიშო25

### შენიშვნა: წესით ყველაფერი სწორად გავაკეთე და სად გამომეპარა შეცდომა არ ვიცი :((((( ###

# xMax = int(input("1: "))
# xMin = int(input("2: "))
#
# if xMax < xMin:
#     temp = xMax
#     xMax = xMin
#     xMin = temp
#
# x = xMin
#
# for each0 in range (xMin, xMax+1):
#     for each1 in range (2, each0):
#         if each0 % each1 != 0:
#             y = 0
#             while True:
#                 z = each0 % 10
#                 each0 = each0 // 10
#                 y = y * 10 + z
#                 if each0 == 0 or each0 == -1: continue
#                 if xMin < y < xMax:
#                     for each3 in range (2, y):
#                         if y % each3 != 0:
#                             print(x)
#     x += 1