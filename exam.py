print("---------------------Student entries by Faculties !!!--------------------------")
stud = 3
name = []

for i in range(stud):
    i = input("Enter Students name : ")
    name.append(i)

attendance = []
for i in range(stud):
    i = int(input("Out of 93 days, How many days do they have attended the classes? : "))
    if i > 93:
        print("Surpasing the total attendance! ")
    else:
        attendance.append(i)

fees = []
for i in range(stud):
    i = input("What is the status of fess payment? (Due/Done): ")
    fees.append(i)

assignment = []
for i in range(stud):
    i = input("What is the status of assignment sumbission? (Submitted/Pending): ")
    assignment.append(i)

min_attendance = 50 
print("-------------------------------------------------------------------------------")
print("----------------------- Students Eligibility Checking -------------------------")
print(name)
c_name = input("Enter your name acc. to the list : ")
flag = False

for i in range(len(name)):
    if c_name == name[i]:
        flag = True
        #Always remember that if you want to check list variable by its length then use len then if you want to check whats inside the list then run i so it will go through the indices then add condition if the name == name[i] (for first name[0]="NAME")

        print("Student Name: ",name[i])
        print("Student Total attendance: ",attendance[i])
        print("Student Fee status: ",fees[i])
        print("Student Assignment Submission Status: ",assignment[i])

        attendance_percentage = (attendance[i] / 93) * 100
        if attendance_percentage >= min_attendance:
            if fees[i] == "Done":
                if assignment[i] == "Submitted":
                    print(name[i],"is eligible for the exam ")
                else:
                    print(name[i],"is not eligible for exam because of assignment submission pending.")
            else:

                print(name[i],"is not eligible for exam because fees payment is still pending")
        else:

            print("Sorry",name[i],"Youre not eligible for the Exam because of low attendance ")
        break
if flag == False:
    print("No such students are in our record! kindly re-enter the name")