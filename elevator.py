print("0. Ground Floor")
print("1. 1st Floor")
print("2. 2nd Floor")
print("3. 3rd Floor")
print("4. 4th Floor")
print("5. 5th Floor")
print("6. 6th Floor")
print("7. 7th Floor")
print("8. 8th Floor")
print("9. 9th Floor")
print("10. 10th Floor")

print("------------------------------------------------------------")

curr = int(input("Enter current floor: "))
req = int(input("Enter requested floor: "))

if curr <0 or curr >10 or req <0 or req >10:
    print("Invalid floor! Please enter a floor between 1 and 10.")
elif curr <req:
    print("Elevator going UP...")
    for i in range(curr,req+ 1):
        print(i)

    print("------------------------------------------------------------")
    print("You have reached your destination.")
elif curr > req:
    print("Elevator going DOWN...")

    for i in range(curr,req-1, -1):
        print(i)
    print("You have reached your destination.")
else:
    print("Elevator is already on this floor.")