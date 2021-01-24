# დავალება 1


with open('students.txt', 'r') as StudentsFile:
    StudentsLines = StudentsFile.readlines()
    Emails = []

    with open('Business.txt', 'w') as business:

        for student in StudentsLines:
            StudentsSplit = student.split(',')

            LastName = StudentsSplit[1]
            Faculty = StudentsSplit[2]
            BDay = StudentsSplit[3]
            Email = StudentsSplit[4]


            if(int(BDay[-4:]) == 2001 or int(BDay[-4:]) == 2002): print(Email)
            if (Faculty == "Business"): business.write(LastName)