#note add delays inbetween each print statement as to much info to read
#function for selecting mode
def select(allpass,amazon,mightyape,google):
    print("There are several modes you can select within this password safe.")
    print("Including:\n('1')Find an existing password\n('2')Add new new password\n('3')Change an existing password\n('4')Exit")
    mode = input("choose selected mode by entering one of the formentioned numbers: ")
    if mode == '1':
        print("Which password would you like to select out of",allpass)
        watpass = input(": ")
        if watpass == 'Amazon':
            for x in amazon:
                print(x)
        elif watpass == 'Mightyape':
            for i in mightyape:
                print(i)
        elif watpass == 'Google':
            for y in google:
                print(y)

#lists for storing websites, usernames and passwords
allpass = ['Amazon','Mightyape','Google']
amazon = [
    'Amazon','Username: Danny',
    'Password: Superduper01'
]
mightyape = [
    'Mightyape','Username: Danny89',
    'Password: Super01'
]
google = [
    'Google','Username: Bobby',
    'Password: BOyshigh61'
]

#defining customer id and password
cusid = 'daniel.h'
cuspass = 'simple'

#checking whether returning user or new
returnuser = input("Are you a returing user?: ")
if returnuser == 'yes':
    nameuser = input("Enter your customer id: ")
    if nameuser == cusid:
        passuser = input("Enter yout customer password: ")
        if passuser == cuspass:
            print ("Secusfully signed in.")
            select(allpass,amazon,mightyape,google)
            
            
elif returnuser == 'no':
    newuser = input("Enter your new username: ")
    newpass = input("Enter your new password: ")
    print("Secusfully created a new account")

    

