import sys
#  opening files
file = ""
file = file + sys.argv[1]
f = open(file, "r")
f2 = open("output.txt", "a")

line = f.readline()

stadium = {}  # create an empty dictionary to add categories into

#  create a dictionary that converts letters to number indexes
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letter_to_number = {}
for i in letters:
    letter_to_number[i] = letters.index(i)

def createcategory():
    #  Making a list of what is written on the line
    #  taking the category name to be created from this list and searching in the dict
    #  adding it if it is not in the dict, or giving a warning if it is in the dict

    linelist = line.strip("\n").split(" ")
    linelist[2] = linelist[2].split("x")

    if linelist[1] in stadium:
        f2.write("Warning: Cannot create the category for the second time.")
        f2.write("The stadium has already {}.\n".format(linelist[1]))
    else:
        x = linelist[1]
        list1 = [["X" for row in range(int(linelist[2][0]))] for column in range(int(linelist[2][1]))]
        stadium[x] = list1
        f2.write("The category {} having ".format(linelist[1]))
        f2.write("{} seats has been created. \n".format(int(linelist[2][0]) * int(linelist[2][1])))


def sellticket():
    #  making a list of what is written on the line
    #  taking the seat numbers in the row from the list,
    #  warning if seats are sold
    #  changing their representation in dict if seats are empty
    #  error if there is no category or seat number to be sold
    global t, linelist, y, j, x
    linelist = line.strip("\n").split(" ")

    for j in range(4, len(linelist)):

        if "-" in linelist[j]:  # if the seat numbers to be sold are in the form of ranges
            try:
                seats = linelist[j].strip("\n").split("-")
                z = seats[0][:1]  # letter
                t = letter_to_number[z]  # letter to number
                x = int(seats[0][1:])  # first seat
                y = int(seats[1])  # last seat

                for _ in range(x, y + 1):
                    # if seats are sold
                    if stadium[linelist[3]][t][_] == "S" \
                            or stadium[linelist[3]][t][_] == "F" \
                            or stadium[linelist[3]][t][_] == "T":
                        f2.write("Warning: The seats {} cannot be sold to ".format(linelist[j]))
                        f2.write("{} due some of them have already been sold!\n".format(linelist[1]))
                        break

                    else:

                        if linelist[2] == "student":
                            for _ in range(x, y + 1):
                                stadium[linelist[3]][t][_] = "S"
                            f2.write("Success: {} has bought {}".format(linelist[1], z + str(x) + "-" + str(y)))
                            f2.write(" at {}\n".format(linelist[3]))
                            break

                        if linelist[2] == "full":
                            for _ in range(x, y + 1):
                                stadium[linelist[3]][t][_] = "F"
                            f2.write("Success: {} has bought {}".format(linelist[1], z + str(x) + "-" + str(y)))
                            f2.write(" at {}\n".format(linelist[3]))
                            break

                        if linelist[2] == "seasons":
                            for _ in range(x, y + 1):
                                stadium[linelist[3]][t][_] = "T"
                            f2.write("Success: {} has bought {}".format(linelist[1], z + str(x) + "-" + str(y)))
                            f2.write(" at {}\n".format(linelist[3]))
                            break

            except IndexError:
                if t > len(stadium[linelist[3]]) and y <= len(stadium[linelist[3]][t]):
                    f2.write("Error: The category \"{}\" has less row ".format(linelist[3]))
                    f2.write("than the specified index {}!\n".format(linelist[j]))
                if y > len(stadium[linelist[3]][t]) and t <= len(stadium[linelist[3]]):
                    f2.write("Error: The category \"{}\" has less column ".format(linelist[3]))
                    f2.write("than the specified index {}!\n".format(linelist[j]))
                if t > len(stadium[linelist[3]]) and y > len(stadium[linelist[3]][t]):
                    f2.write("Error: The category \"{}\" has less row and column ".format(linelist[3]))
                    f2.write("than the specified index {}!\n".format(linelist[j]))

        else:  # if the seat numbers to be sold are one by one
            try:
                z = linelist[j][:1]  # letter
                t = letter_to_number[z]  # letter to number
                x = int(linelist[j][1:])  # seat number
                if stadium[linelist[3]][t][x] == "S" \
                        or stadium[linelist[3]][t][x] == "T" \
                        or stadium[linelist[3]][t][x] == "F":

                    f2.write("Warning: The seat {} cannot be sold to ".format(linelist[j]))
                    f2.write("{} since it was already sold!\n".format(linelist[1]))
                else:

                    if linelist[2] == "student":
                        stadium[linelist[3]][t][x] = "S"
                        f2.write("Success: {} has bought {}".format(linelist[1], linelist[j]))
                        f2.write(" at {}\n".format(linelist[3]))

                    if linelist[2] == "full":
                        stadium[linelist[3]][t][x] = "F"
                        f2.write("Success: {} has bought {}".format(linelist[1], linelist[j]))
                        f2.write(" at {}\n".format(linelist[3]))

                    if linelist[2] == "seasons":
                        stadium[linelist[3]][t][x] = "T"
                        f2.write("Success: {} has bought {}".format(linelist[1], linelist[j]))
                        f2.write(" at {}\n".format(linelist[3]))

            except IndexError:
                if t > len(stadium[linelist[3]]):
                    f2.write("Error: The category \"{}\" has less row ".format(linelist[3]))
                    f2.write("than the specified index {}!\n".format(linelist[j]))
                if x > len(stadium[linelist[3]][t]):
                    f2.write("Error: The category \"{}\" has less column ".format(linelist[3]))
                    f2.write("than the specified index {}!\n".format(linelist[j]))


def cancelticket():
    #  making a list of what is written on the line
    #  taking the seat numbers in the row from the list
    #  warning if the seat numbers to be canceled are already empty
    #  if the seat numbers to be canceled are full, changing their representation in the dict
    global linelist, j, t, x
    linelist = line.strip("\n").split(" ")

    for j in range(2, len(linelist)):
        try:
            z = linelist[j][:1]  # letter
            t = letter_to_number[z]  # letter to number
            x = int(linelist[j][1:])  # seat number

            if stadium[linelist[1]][t][x] == "X":
                f2.write("Error: The seat {} at \"{}\" ".format(linelist[j], linelist[1]))
                f2.write("has already been free! Nothing to cancel\n")

            else:
                stadium[linelist[1]][t][x] = "X"
                f2.write("Success: The seat {} at \"{}\" ".format(linelist[j], linelist[1]))
                f2.write("has been canceled and now ready to sell again\n")

        except IndexError:
            if t > len(stadium[linelist[1]]) and x <= len(stadium[linelist[1]][t]):
                f2.write("Error: The category \"{}\" has less row ".format(linelist[1]))
                f2.write("than the specified index {}!\n".format(linelist[j]))
            if x > len(stadium[linelist[1]][t]) and t <= len(stadium[linelist[1]]):
                f2.write("Error: The category \"{}\" has less column ".format(linelist[1]))
                f2.write("than the specified index {}!\n".format(linelist[j]))
            if t > len(stadium[linelist[1]]) and x > len(stadium[linelist[1]][t]):
                f2.write("Error: The category \"{}\" has less row and column ".format(linelist[1]))
                f2.write("than the specified index {}!\n".format(linelist[j]))


def balance():
    #  making a list of what is written on the line
    #  getting the name of the category whose revenue will be calculated from the list
    #  determining the number of student, full and seasons tickets
    #  calculation of revenue by multiplying the number of tickets and their prices in each ticket category

    linelist = line.strip("\n").split(" ")
    s = 0  # revenue of student tickets
    f = 0  # revenue of full tickets
    t = 0  # revenue of seasons tickets
    x = 0  # number of student
    y = 0  # number of full
    z = 0  # number of seasons

    for j in range(len(stadium[linelist[1]])):

        for k in range(len(stadium[linelist[1]][j])):

            if "S" == stadium[linelist[1]][j][k]:
                s += 10
                x += 1
            if "F" == stadium[linelist[1]][j][k]:
                f += 20
                y += 1
            if "T" == stadium[linelist[1]][j][k]:
                t += 250
                z += 1

    r = s + f + t  # revenue
    pline = "Category report of \"{}\" \n".format(linelist[1])  # first line to print
    a = len(pline)  # for the number of - to print
    f2.write(pline)
    f2.write("-" * a + "\n")
    f2.write("Sum of students = " + str(x) + ", Sum of full pay = " + str(y))
    f2.write(", Sum of season ticket = " + str(z) + ", and Revenues = " + str(r) + " Dollars \n")


def showcategory():
    #  making a list of what is written on the line
    #  getting category name from list
    #  printing seats in category with rows and columns
    global y
    linelist = line.strip("\n").split(" ")
    x = len(stadium[linelist[1]])
    f2.write("Printing category layout of {}\n\n".format(linelist[1]))

    for j in range(x - 1, -1, -1):
        #  printing letters
        f2.write(letters[j])
        f2.write(" ")
        y = len(stadium[linelist[1]][j])

        for k in range(y):
            # printing seats
            f2.write(stadium[linelist[1]][j][k])
            f2.write("  ")
        f2.write("\n")
    f2.write("  ")

    for i in range(y):
        # printing numbers
        if i < 9:
            f2.write(str(i) + "\t".expandtabs(2))

        else:
            f2.write(str(i) + "\t".expandtabs(1))
    f2.write("\n")


while line:

    if "CREATECATEGORY" in line:
        createcategory()
    if "SELLTICKET" in line:
        sellticket()
    if "CANCELTICKET" in line:
        cancelticket()
    if "BALANCE" in line:
        balance()
    if "SHOWCATEGORY" in line:
        showcategory()

    line = f.readline()

f.close()
f2.close()

#  Ayþe Yaren Topgün - 2220356141
