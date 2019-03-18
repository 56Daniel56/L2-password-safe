#note add delays inbetween each print statement as to much info to read
#function for selecting mode
#passwordsafe
def select():
    print("There are several modes you can select within this password safe.")
    print("Including:\n('1')Find an existing password\n('2')Add new new password\n('3')Change an existing password\n('4')Exit")
    mode = input("choose selected mode by entering one of the formentioned numbers: ")
    #once user has entred mode is mode 1 runs this code
    if mode == '1':
        mode1(allpass,amazon,mightyape,google)
    elif mode == '2':
        mode2()
    elif mode == '3':
         mode3()
    elif mode == '4':
        quit()
        
        
#separate function for each mode as it separates code and looks cleaner
def mode1(allpass,amazon,mightyape,google):
    #allpass in this print statement tells the user of all websites that have the account info all ready saved
    print("Which password would you like to select out of",allpass)
    watpass = input(": ")
    #in this section I have added for loops. This is so the list will print out clean with only the contents and no square brackets
    #This part also compare watpass to there input and see what password they would like to display
    if watpass == 'Amazon':
        for x in amazon:
            print(x)
    elif watpass == 'Mightyape':
        for i in mightyape:
            print(i)
    elif watpass == 'Google':
        for y in google:
            print(y)

def mode2():
    addweb = input("What is the name of the website you would like to add?: ")
    adduse = input("What is the username you would like to add?: ")
    addpass = input("What is the name of the password you would like to add?: ")
    allpass.append(addweb)

def mode3():
    change = input("would you like to change your username or password")
    if change == 'username':
        uchange = input("What is the website you would like to change your username for?: ")
        if uchange == 'Amazon':
            del amazon [1]
            newu = input("What is the new username you would like to enter?: ")
            amazon.insert(1,'Username: '+newu)
            print(amazon)
    elif change == 'password':
        pchange = input("What is the website you would like to change your password for?: ")
        if pchange == 'Amazon':
            del amazon [2]
            newp = input("What is the new password you would like to enter?: ")
            amazon.append('Password: '+newp)
            print(amazon)


#lists for storing websites, usernames and passwords

#stores the diffrent name of the websites that you have saved
allpass = ['Amazon','Mightyape','Google']
#stores the acount information for amazon
amazon = [
    'Amazon','Username: Danny',
    'Password: Superduper01'
]
#stores the acount information for mightyape
mightyape = [
    'Mightyape','Username: Danny89',
    'Password: Super01'
]
#stores the acount information for google
google = [
    'Google','Username: Bobby',
    'Password: BOyshigh61'
]

#defining customers master id and password
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
            select()
            
#if the user does not have an account they can create one here            
elif returnuser == 'no':
    newuser = input("Enter your new username: ")
    newpass = input("Enter your new password: ")
    print("Secusfully created a new account")

    

