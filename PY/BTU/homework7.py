#სავარჯიშო1

# print("1 n 2")
# print("1 \n 2")

#სავარჯიშო3

# print(len(str(input("შეიყვანეთ ტექსტი ქვემოთ \/ \n"))))

#სავარჯიშო4

# first_str = str(input(""))
# second_str = str(input(""))
#
# print(first_str + second_str)

#სავარჯიშო5

# print(str.upper(str(input(""))))

#სავარჯიშო6

# print(str(input("")).count('a'))

#სავარჯიშო7

# banana = "Banana"
# apple = "Apple"
# watermelon = "Watermelon"
# list = (apple, banana, watermelon)
#
# print(sorted(list))

#სავარჯიშო8

# text = 'სწავლის ძირი მწარე არის, კენწეროში გატკბილდების.'
#
# print(text[:20])
# print(text.count('ს'))

#სავარჯიშო9

# input = str(input(''))
# text = ''
#
# for letter in input:
#     if letter.isupper() == True:
#         letter = letter.lower()
#     elif letter.islower() == True:
#         letter = letter.upper()
#     text += letter
#
# print(text)

#სავარჯიშო10

# text = "Hello, this is example of string. Please, write this text and do some exercises."
# print(text.replace(' is', ' were'))

#სავარჯიშო11

# text = "Hello, this is example of string. Please, write this text and do some exercises."
# print(text.count(' ') + 1)

# სავარჯოშო12
#
# text = 'Have a nice day!'
#
# while True:
#     for each in range(1, len(text) + 1):
#         print(text[-each])
#     if each == len(text): break

#სავარჯიშო13

# text = str(input(''))
# text = text.lower()
#
# print(text.count('a') + text.count('e') + text.count('i') + text.count('o') + text.count('u'))

#სავარჯიშო14

# print(len(str(237645)))

#სავარჯიშო15

# print(len(str(pow(2, 132))))

#სავარჯიშო16

# text = 'bachana.mosulishvili.1@btu.edu.ge'
#
# print(text.find('@') + 1)

#სავარჯიშო17

# name = input(str('გთხოვთ შეიყვანოთ თქვენი სახელი ლათინურად: '))
# surname = input(str('გთხოვთ შეიყვანოთ თქვენი გვარი ლათინურად: '))
#
# print("თქვენი მეილი არის: ", name.lower() + '.' + surname.lower()+'@btu.edu.ge')

#სავარჯიშო18

input = str(input(''))
lower = 0
upper = 0
digit = 0
special = 0

for character in input:
    if character.isalpha() == False and character.isdigit() == False: special += 1
    if character.isalpha() and character.islower(): lower += 1
    if character.isalpha() and character.isupper(): upper += 1
    if character.isdigit(): digit += 1

print('lower: ', lower)
print('upper: ', upper)
print('digit: ', digit)
print('special: ', special)

#სავარჯიშო19

# input = str(input(''))
# lower = 0
# upper = 0
# digit = 0
# special = 0
#
# for character in input:
#     if character.isalpha() == False and character.isdigit() == False: special += 1
#     if character.isalpha() and character.islower(): lower += 1
#     if character.isalpha() and character.isupper(): upper += 1
#     if character.isdigit(): digit += 1
#
# if lower > 0 and upper > 0 and digit > 0 and special > 0: print('This password can be used!')
# else: print('This password CAN\'T be used!')

#სავარჯიშო20

# text = str(input(''))
# finaltext = ''
#
# for letter in text:
#     if letter.isalpha(): finaltext += letter
#
# print(finaltext)

#სავარჯიშო21

# text = str(input(''))
# number = 0
# common = 0
#
# for character in text:
#     number = text.count(character)
#     if number > common:
#         common = number
#         letter = character
#
# print(common, letter)

#სავარჯიშო22

# text = str(input(''))
#
# text = text.replace(' ', '')
#
# if text == text[::-1]: print("YES")
# else: print('NO')
