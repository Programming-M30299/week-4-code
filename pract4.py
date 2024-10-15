import os


def student_info():
    course = input("What's your course? ")
    student_id = input("What's your ID number? ")
    print("Welcome to:\t" + course)
    print("\n" * 2 + "Your ID number is:\t" + student_id[2:])


def personal_details():
    name = input("What's your name? ")
    age = int(input("What's your age? "))
    height = float(input("What's your height? "))
    # print("name:\t{:>10}\nage:\t{:>10}\nheight:\t{:>10.2f}".format(name, age, height))
    print(f"name:\t{name:>10}\nage:\t{age:>10}\nheight:\t{height:>10.2f}")


def read_quote():
    print("Current directory:\t" + os.getcwd())
    print("Files in current directory:\t" + str(os.listdir()))
    # Change directory to the folder containing quotation.txt
    os.chdir("text_files")
    # Checking if quotation.txt is in the current directory:
    print("Current directory:\t" + os.getcwd())
    print("Files in current directory:\t" + str(os.listdir()))

    input_file = open("quotation.txt", "r")

    # You can use `read()` to read the whole file into a single string
    content = input_file.read()
    print(content)


def write_quote():
    os.chdir("text_files")
    output_file = open("my_quotation.txt", "w")

    # You can use `write()` to write a single string
    print("I love Python!", file=output_file)
    print("(Matthew Poole)", file=output_file)

    # Or write both lines in one go separated by a newline character ('\n')
    # content = "I love Python!\n(Matthew Poole)"
    # output_file.write(content)


# Solutions below:
