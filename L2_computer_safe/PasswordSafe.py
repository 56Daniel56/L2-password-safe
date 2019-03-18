#company password safe
#different




#defining customer id and password
cusid = 'daniel.h'
cuspass = 'secrect'

#pre entred usernames and passwords


#checking whether returning user or new
returnuser = input("Are you a returing user?: ")
if returnuser == 'yes':
    nameuser = input("Enter your customer id: ")
    if nameuser == cusid:
        passuser = input("Enter yout customer password: ")
        if passuser == cuspass:
            print ("Secusfully signed in.")
            
elif returnuser == 'no':
    newuser = input("Enter your new username: ")
    newpass = input("Enter your new password: ")
    print("Secusfully created a new account")

    

