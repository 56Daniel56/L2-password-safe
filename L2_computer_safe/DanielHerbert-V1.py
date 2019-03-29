#company password safe
#different




#defining customer id and password
cusid = 'daniel.h'
cuspass = 'secrect'

#pre entred usernames and passwords
print("Daniel Herbert, 15th March 2019, Version 1 of Password safe.")

#checking whether returning user or new
returnuser = input("Are you a returing user?: ")
if returnuser == 'yes':
    nameuser = input("Enter your customer id: ")
    if nameuser == cusid:
        passuser = input("Enter yout customer password: ")
        if passuser == cuspass:
            print ("Secusfully signed in.")
            
    

