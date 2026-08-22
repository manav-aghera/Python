name=(input("Enter your name : "))
book=(input("Enter the name of a book : "))

print("--------------------------------------------------------")

days=int(input("For how many days does an individual want to keep the book to himself/herself? : "))
print(book + " is given to " + name + " for " + str(days) + " days")

print("--------------------------------------------------------")
charge=20

for i in range(1,days+1):
    print("Day ",i)
s="Did " +name+" Submitted the book? : "
submition=(input(s))
if (submition == "Yes"):
    subday=int(input("When did you submitted the book? : "))
print("--------------------------------------------------------")
if(subday<days):
    print("Thank you ! Have a nice day ")
else:
    overdue=subday-days
    fine=charge*overdue
    print("You have to pay the fine ! overdue days are",overdue)
    print("Your total fine is",fine)

pay=int(input("Pay the total fine by entering the total amount of fine: "))
if(pay==fine):
    print("Payment Successful ! Have a nice day :)")