import os


def studentInfo():
    course = input("What's your course? ")
    studentID = input("What's your ID number? ")
    print("Welcome to:\t" + course)
    print("\n" * 2 + "Your ID number is:\t" + studentID[2:])


def idFromEmail():
    email = input("What's your email? ")  # 'up1234567@myportacuk'
    parts = email.split("@")  # ['up1234567', 'myport.ac.uk']
    upNumber = parts[0]  # 'up1234567'
    print("Your ID is:\t" + upNumber[2:])  # '1234567'


def personalDetails():
    name = input("What's your name? ")
    age = int(input("What's your age? "))
    height = float(input("What's your height? "))
    # print("name:\t{:>10}\nage:\t{:>10}\nheight:\t{:>10.2f}".format(name, age, height))
    # print("name: {0:s} age: {1:d} height: {2:.2f}".format(name, age, height))
    print(f"name:\t{name:>10}\nage:\t{age:>10}\nheight:\t{height:>10.2f}")


def readQuote():
    print("Current directory:\t" + os.getcwd())
    print("Files in current directory:\t" + str(os.listdir()))

    # Change directory to the folder containing quotation.txt
    os.chdir("week-4/textFiles")
    # Checking if quotation.txt is in the current directory:
    print("Current directory:\t" + os.getcwd())

    inFile = open("quotation.txt", "r")

    # use read() to read the whole file into a single string
    content = inFile.read()
    print(content)

    # # use readLines() to read all lines into a list
    # lines = inFile.readlines()
    # for line in lines:
    #     print(line[:-1])

    # # use readLine() to read the first line
    # line = inFile.readline()
    # while line:
    #     print(line)
    #     line = inFile.readline()

    inFile.close()


def writeQuote():
    os.chdir("week-4/textFiles")
    outFile = open("myQuotation.txt", "w")
    # content = "I love Python!\n(Matthew Poole)"
    # outFile.write(content)
    print("I love Python!", file=outFile)
    print("(Matthew Poole)", file=outFile)
    outFile.close()
