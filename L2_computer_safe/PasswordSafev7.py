#note add delays inbetween each print statement as to much info to read
#function for selecting mode
#passwordsafe
def select():
    while True:
        print("There are several modes you can select within this password safe.")
        print("Including:\n('1')Find an existing password\n('2')Add new new password\n('3')Change an existing password\n('4')Exit")
        mode = input("choose selected mode by entering one of the formentioned numbers: ")
        #once user has entred mode is mode 1 runs this code
        if mode == '1':
            mode1(allpass,usernames,passwords)
        elif mode == '2':
            mode2(allpass,usernames,passwords)
        elif mode == '3':
             mode3(usernames,passwords,allpass)
        elif mode == '4':
            quit()
        else:
            print("Sorry, you have entred an invalid input. Please read the question carefully and try again.")
            continue
        
        
#separate function for each mode as it separates code and looks cleaner, I have used a function because it will allow me to use this code infinite times
#this function ie: mode 1 allows the user to display exisisting account information
def mode1(allpass,usernames,passwords):
    #allpass in this print statement tells the user of all websites that have the account info all ready saved
    print("Which password would you like to select out of",allpass)
    watpass = input(": ")
    #in this section I have added for loops. This is so the list will print out clean with only the contents and no square brackets
    #This part also compare watpass to the user input and see what password they would like to display
    if watpass in allpass:
        print(usernames[watpass])
        print(passwords[watpass])

#function envolving creating a new account for a new website.

def mode2(allpass,usernames,passwords):
    addweb = input("What is the name of the website you would like to add?: ")
    adduse = input("What is the username you would like to add?: ")
    addpass = input("What is the name of the password you would like to add?: ")
    allpass.append(addweb)
    usernames[addweb] = adduse
    passwords[addweb] = addpass
    print("New username:",usernames[addweb])
    print("New password:",passwords[addweb])

def mode3(usernames,passwords,allpass):
    change = input("would you like to change your username or password")
    if change == 'username':
        uchange = input("What is the website you would like to change your username for?: ")
        if uchange == 'Amazon':
            newuse = input("What is the new username you would like to enter?: ")
            usernames['Amazon'] = newuse
            print(usernames['Amazon'],"is now your new username")
        elif uchange == 'Mightyape':
            newuse = input("What is the new username you would like to enter?: ")
            usernames['Mightyape'] = newuse
            print(usernames['Mightyape'],"is now your new username")
            
        elif uchange == 'Google':
            newuse = input("What is the new username you would like to enter?: ")
            usernames['Google'] = newuse
            print(usernames['Google'],"is now your new username")

            
    elif change == 'password':
        pchange = input("What is the website you would like to change your password for?: ")
        if pchange == 'Amazon':
            newpass = input("What is the new password you would like to enter?: ")
            passwords['Amazon'] = newpass
            print(passwords['Amazon'],"is now your new password")
        elif pchange == 'Mightyape':
            newpass = input("What is the new password you would like to enter?: ")
            passwords['Mightyape'] = newpass
            print(passwords['Mightyape'],"is now your new password")
        elif pchange == 'Google':
            newpass = input("What is the new password you would like to enter?: ")
            passwords['Google'] = newpass
            print(passwords['Google'],"is now your new password")


#lists for storing websites, usernames and passwords

#stores the diffrent names of the websites that you have saved
allpass = ['Amazon','Mightyape','Google']

#I have decided to use diticionaries he as it allows me to store multiple keys and call certain ones whenever I want
#stores the acount information for all the usernames
usernames = {'Amazon':'Username: Danny',
             'Mightyape':'Username: Danny89',
             'Google':'Username: Bobby'}

#stores the passwords for all the different websites
passwords = {'Amazon':'Password: Super01',
             'Mightyape':'Password: BOyshigh61',
             'Google':'Password: superduper33'}


#defining customers master id and master password. You have to enter these to acsess the rest of the program
MASID = 'daniel.h'
MASPASS = 'simple'

#the code that prevents user from entering the rest of the program unless they have this info
nameuser = input("Enter the Master id: ")
if nameuser == MASID:
    passuser = input("Enter the Master password: ")
    if passuser == MASPASS:
        print ("Secusfully signed in.")
        select()
"""            
#if the user does not have an account they can create one here            
elif returnuser == 'no':
    newuser = input("Enter your new username: ")
    newpass = input("Enter your new password: ")
    print("Secusfully created a new account")

    
"""
