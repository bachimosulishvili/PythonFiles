# სავარჯიშო1

# def division():
#     try:
#         a = int(input('გთხოვთ შეიყვანოთ პირველი რიცხვი: '))
#         b = int(input('გთხოვთ შეიყვანოთ მეორე რიცხვი: '))
#         print(a, '/', b, '=', a/b)
#     except ValueError:
#         print('\nთქვენს მიერ შეყვანილი სიმბოლო(ები) არ არის რიცხვი.\nსცადეთ ხელახლა!\n')
#         division()
#     except ZeroDivisionError:
#         print('\nცხოვრების წესი N1: არასდროს გაყო ნულზე!\nსცადეთ ხელახლა!\n')
#         division()
#
# division()

# სავარჯიშო2

# def trydivision(a, b):
#     try:
#         int(a)
#         int(b)
#         if a%b == 0: print(a, '/', b, '=', a/b)
#
#     except ValueError: print(a, '/', b, '\nთქვენს მიერ შეყვანილი სიმბოლო(ები) არ არის რიცხვი.\n')
#     except ZeroDivisionError: print(a, '/', b, '\nცხოვრების წესი N1: არასდროს გაყო ნულზე!\n')
#
# trydivision(5, 0)
# trydivision('a', 6)
# trydivision(81, 9)

# სავარჯიშო3

# list = ['Entrepreneurship', 'Digital Technologies', 'Calculus', 'Python', 'Mobile Applications', 'Network Basics']
#
# try:
#     num = int(input('რომელი ელემენტის ამოღება გსურთ სიიდან? (0-5)\n'))
#     print(list[num])
# except IndexError: print('ელემენტი ამ ნომრით არ არსებობს!')

# სავარჯიშო4

# try:
#     f = open('myresult.txt', 'r')
#     f.close()
# except FileNotFoundError:
#     print('ფაილი არ მოიძებნა!')

# სავარჯიშო5

# try:
#     a = int(input('a = '))
#     b = int(input('b = '))
#     c = int(input('c = '))
#     while True:
#         D = b**2 - 4*a*c
#         if D < 0:
#             print('განტოლებას არ აქვს ამონახსნი.')
#             break
#         x1 = (-b + (D**(1/2)))/(2*a)
#         x2 = (-b - (D**(1/2)))/(2*a)
#         if x1 == x2: print('x1 = x2 =', x1)
#         else:
#             print(' x1 =',x1, '\n', 'x2 =', x2)
#         break
#
# except ZeroDivisionError: print('განტოლების ამოხსნა ვერ მოხერხდა!\nამოხსნისას მოხდა 0-ზე გაყოფა, რაც მიუტევებელი ცოდვაა.')
# except ValueError: print('განტოლების ამოხსნა ვერ მოხერხდა!\nთქვენს მიერ შეყვანილი სიმბოლო არ არის რიცხვი!')


# სავარჯიშო6

# try:
#     side1 = int(input('პირველი გვერდის სიგრძე: '))
#     side2 = int(input('მეორე გვერდის სიგრძე: '))
#     side3 = int(input('მესამე გვერდის სიგრძე: '))
#     if side1 <= 0 or side2 <=0 or side3 <= 0: raise ValueError
#     else:
#         if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
#             print('სამკუთხედის გვერდების საშუალო არითმეტიკულია ', (side1 + side2 + side3)/3)
#         else: raise AssertionError
#
# except ValueError: print('სამკუთხედის გვერდის სიგრძე უნდა იყოს ნატურალური რიცხვი!')
# except AssertionError: print('შეყვანილი რიცხვები არ წარმოადგენს სამკუთხედის გვერდებს!')
