#სავარჯიშო1

# file = open('example.txt', 'w')
# file.write('Hello World!\n')
# file.close()

#სავარჯიშო2

# raw = open('example.txt', 'r')
# file = raw.read()
#
# print(file)
# print(len(file))
#
# raw.close()

#სავარჯიშო3

# file = open('example.txt', 'a+')
# content = file.read()
# file.write('\nHello Again!')
# print(content)
# file.close()

#სავარჯიშო4

    #example2.txt-ის ჩაწერა

# with open('example2.txt', 'w') as example2Write:
#      example2Write.write('Hello, this is my homework.')

    #დავალება
# with open('example.txt', 'a') as file1open:
#     with open('example2.txt', 'r') as file2open:
#         file2Content = file2open.read()
#         file1open.write('\n' + file2Content)

#სავარჯიშო5

# with open('example.txt', 'r') as file1open:
#      with open('example2.txt', 'r') as file2open:
#           with open('example3.txt', 'w') as file3open:
#                file1content = file1open.read()
#                file2content = file2open.read()
#
#                file3open.write(file1content + '\n' + file2content)

#სავარჯიშო6

# with open('example.txt', 'r') as fileOpen:
#      fileContent = fileOpen.read()
#      print(fileContent.upper())

#სავარჯიშო7

# with open('data.txt', 'w') as dataFile:
#      while True:
#           dataInput = input('')
#           if dataInput == '0': break
#           dataFile.write(dataInput + '\n')

#სავარჯიშო8

# with open('example.txt', 'r') as sourceFile:
#      with open('newFile.txt', 'w') as newFile:
#           source = sourceFile.read()
#           source = source.replace('\n', ' ')
#           newFile.write(source)

#სავარჯიშო9

# with open('example.txt', 'r') as file:
#      fileRead = file.read()
#
#      print('words: ', len(fileRead.split()))
#      print('symbols: ', len(fileRead))
#      print('lines: ', fileRead.count('\n'))

#სავარჯიშო10

# with open('numbers.txt', 'w') as numbers:
#     numbers.write('6152\n49\n8498')

# with open('numbers.txt', 'r') as numbers:
#      with open('result.txt', 'w') as result:
#           numbersContent = numbers.read()
#############???????????????????#############


#სავარჯიშო11

# with open('oscars.txt', 'r') as oscars:
#      oscarsRead = oscars.read().upper()
#      inputYear = input("Enter Year: ")
