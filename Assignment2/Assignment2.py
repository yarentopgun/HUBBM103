f = open("doctors_aid_inputs", "r", encoding='utf-8')
patient_data_list = []
line = f.readline()


# saving to the output file function
def save_output(x):
    with open("doctors_aid_outputs", "a", encoding='utf-8') as f2:
        f2.write(x)


# create a new patient
def create():
    global patient_data_list
    linelist = line.strip("\n").split(", ")  # comma separated data in create line
    linelist[0] = linelist[0].lstrip("create ")  # obtaining only "name" from data in the form of "create name"
    if linelist in patient_data_list:  # if the person is already registered
        save_output("Patient " + format(linelist[0]))
        save_output(" cannot recorded due to duplication.\n")
    else:  # if the person is not registered
        patient_data_list.append(linelist)
        save_output("Patient " + format(linelist[0]) + " is recorded.\n")


# delete an existing patient
def remove():
    global patient_data_list
    removelist = line.strip("\n").split(" ")  # create a list to use the "name" on the line later
    i = 0
    while i < len(patient_data_list):
        if removelist[1] in patient_data_list[i]:  # if the patient to be deleted is in the patient list
            del patient_data_list[i]
            save_output("Patient " + format(removelist[1]) + " is removed.\n")
            break
        else:
            i += 1
    else:  # if the patient to be deleted is not in the list
        save_output("Patient " + format(removelist[1]))
        save_output(" cannot be removed due to absence.\n")


# patient's probability of having the disease
def probability():
    probability_list = line.strip("\n").split(" ")
    j = 0
    while j < len(patient_data_list):
        if probability_list[1] in patient_data_list[j]:
            list_x = patient_data_list[j][3].strip('').split("/")
            x = float(list_x[0]) / float(list_x[1])  # disease incidence (true positive)
            y = 1.0 - float(patient_data_list[j][1])  # 1 - diagnosis accuracy (false positive)
            p = x / (x + y)  # true positive / total positive = probability
            p = p * 100
            p = round(p, 2)
            p = format(p, "g")

            save_output("Patient " + format(probability_list[1]) + " has a probability of ")
            save_output(format(p) + "% of a having " + format(patient_data_list[j][2]) + ".\n")
            break
        else:
            j += 1
    else:
        save_output("Probability for " + format(probability_list[1]))
        save_output(" cannot be calculated due to absence.\n")


# a patient's recommendation for a particular treatment
def recommendation():
    recommendation_list = line.strip("\n").split(" ")
    k = 0
    while k < len(patient_data_list):
        if recommendation_list[1] in patient_data_list[k]:
            list_y = patient_data_list[k][3].strip('').split("/")
            x = float(list_y[0]) / float(list_y[1])  # disease incidence (true positive)
            y = 1.0 - float(patient_data_list[k][1])  # 1 - diagnosis accuracy (false positive)
            p = x / (x + y)  # true positive / total positive = probability
            p = p * 100
            p = round(p, 2)

            r = float(patient_data_list[k][5]) * 100

            if p < r:  # if probability is less than treatment risk
                save_output("System suggest " + format(recommendation_list[1]))
                save_output(" NOT to have the treatment.\n")
            else:  # if probability is greater than treatment risk
                save_output("System suggest " + format(recommendation_list[1]))
                save_output(" to have the treatment.\n")
            break
        else:
            k += 1
    else:  # no patient in this name, in the patient list
        save_output("Recommendation for " + format(recommendation_list[1]))
        save_output(" cannot be calculated for due to absence.\n")


# a listing function
def list():
    with open("doctors_aid_outputs", "a", encoding='utf-8') as f2:
        header1 = "%-17s%-17s%-17s%-17s%-17s%-9s" % ("Patient","Diagnosis","Disease","Disease","Treatment","Treatment")
        header2 = "%-17s%-17s%-17s%-17s%-17s%-9s" % ("Name", "Accuracy","Incidence","Name","Risk","Treatment")
        f2.write(header1 + "\n")
        f2.write(header2 + "\n")
        f2.write("-" * 94 + "\n")

        for patient in patient_data_list:
            formatted_line = "%-17s%-17s%-17s%-17s%-17s%-9s\n" % tuple(patient)
            f2.write(formatted_line)


# reading the input file function
def reading_file():
    global line
    while line:
        if "create" in line:
            create()
        if "remove" in line:
            remove()
        if "probability " in line:
            probability()
        if "recommendation " in line:
            recommendation()
        if "list" in line:
            list()
        line = f.readline()


reading_file()
f.close()

# Ayşe Yaren Topgün - 2220356141
