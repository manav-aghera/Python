password = 1475963
attempt = 4
temp_attempt = attempt
for i in range (attempt): # range(n) starts from 0 and repeats the loop exactly n times. // (start,stop) logic wouldnt be applicable 
    enter = int(input("Enter the password : "))
    if enter == password:
        print("Device Unlocked !!")
        temp_attempt = attempt
        
    else: 
        temp_attempt-=1
        if temp_attempt != 0:
            print("try again !you have only ",temp_attempt,"attempts left")
        else:
            print("total number of attempts failed your account is locked  ! ")
