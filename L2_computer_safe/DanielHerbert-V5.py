#L2-Password-Safe



import time

#note add delays inbetween each print statement as to much info to read
#function for selecting mode
#passwordsafe

#This when run asks the user whether the want to run the program again

    
def select():
    while True:
        print("Hello,",name,". This is a password safe programed in python to store account information for websites or anything else you desire.\n There are several modes you can select within this password safe.")
        print("\nIncluding:\n('1')Find an existing account\n('2')Adding a new account\n('3')Changing an existing username or password\n('4')Exit this program")
        mode =(input("choose selected mode by entering one of the formentioned numbers which corespondes to the desired mode: "))
        #once user has entred mode is mode 1 runs this code
        if mode == '1':
            #runs the code when the user is wanting to check for a existing username and password
            mode1(allpass,usernames,passwords)
            break
        elif mode == '2':
            #this runs if the user is wanting to insert a new account to the program
            mode2(allpass,usernames,passwords)
            break
        elif mode == '3':
            #mode 3 is to change an existing username or password
            mode3(usernames,passwords,allpass,run)
            break    
        elif mode == '4':
            #mode 4 quits the program
            quit()
        else:
            #user has not entred a correct input tells them why and runs the loop again
            print("You have not entred a number, or it is out of range. Please read the question carefully and try again.")
            continue

#separate function for each mode as it separates code and looks cleaner, I have used a function because it will allow me to use this code infinite times
#this function ie: mode 1 allows the user to display exisisting account information
def mode1(allpass,usernames,passwords):
    #allpass in this print statement tells the user of all websites that have the account info all ready saved
    while True:
        print("Which account would you like to select out of")
        print(allpass)
        watpass = input(": ")
        #in this section I have added for loops. This is so the list will print out clean with only the contents and no square brackets
        #This part also compare watpass to the user input and see what password they would like to display
        if watpass in allpass:
            print(usernames[watpass])
            print(passwords[watpass])
            time.sleep(2)
            break

        else:
            print("Sorry",name," this account is not avalible within this program. Please try typing in the website again typing the letters exactly the same as it displays.")
            continue
    select()
    

#function envolving creating a new account for a new website.

def mode2(allpass,usernames,passwords):
    #variable so the program knows the name of the website you want to add
    addweb = input("What is the name of the website you would like to add?: ")
    #username added here
    adduse = input("What is the username you would like to add?: ")
    #password added here
    addpass = input("What is the name of the password you would like to add?: ")
    #addweb which is the website is being appended to the list allpass which holds all the websites
    allpass.append(addweb)
    
    
    #setting the new username and password inside their specific dictionaries
    usernames[addweb] = ('Username:'+adduse)
    passwords[addweb] = ('Password:'+addpass)
    #displays the new username and password
    print(usernames[addweb])
    print(passwords[addweb])
    while True:
        #checks user entred the corect and are happy with the values they have entred
        corect = input("Are you happy with what you have entred? 'yes' or 'no': ")
        if corect== 'yes':
            break
        elif corect== 'no':
            #starts mode 2 again so then the user can have another go at entering the website
            print("Ok",name,", we will start again.")
            print(allpass)
            del allpass[-1]
            del usernames[addweb]
            del passwords[addweb]
            mode2(allpass,usernames,passwords)
            break
        else:
            print("Please try again as that input was not 'yes' or 'no'.")
            continue
    select()

            

#mode 3 allows user to change a username or password for one of the websites
def mode3(usernames,passwords,allpass,run):
    while True:
        #asking whether the username or password wants to be changed
        change = input("would you like to change your username or password: ")
        if change == 'username':
            while run<=1:
                #displays all websites avilible to be changed
                print("What is the website you would like to change your username for? Out of",allpass)
                uchange = input(": ")
                if uchange in allpass:
                    newuse = input("What is the new username you would like to enter?: ")
                    #enters new username into the dictionary
                    usernames[uchange] = ('Username:'+newuse)
                    #shows the user that it has been changed
                    print(usernames[uchange],"is now set")
                    #changes run to run=2 so the loop will not be ran again
                    run=run+1
                    break
                else:
                    print("Sorry ",name," that is not a website or you have spelt it incorect, please try again and enter carefully.")
                    continue

        elif change == 'password':
            while run<=1:
                #displays all websites avilible to be changed
                print("What is the website you would like to change your password for? Out of",allpass)
                pchange = input(": ")
                if pchange in allpass:
                    newpass = input("What is the new password you would like to enter?: ")
                    #enters new password into the dictionary
                    passwords[pchange] = ('Password:'+newpass)
                    #shows the user that it has been changed
                    print(passwords[pchange],"is now set")
                    #changes run to run=2 so the loop will not be ran again
                    run=run+1
                    break
                else:
                    print("Sorry that is not a website or you have spelt it incorect, please try again and enter carefully.")
                    continue
        else:
            ("Try entering either 'username' or 'password'")
            continue
        while True:
            #checks user entred the corect values
            corect = input("Are you happy with what you have changed?. 'yes' or 'no': ")
            if corect== 'yes':
                break
            elif corect== 'no':
                #give the user another go at entering their new username or password
                
                print("Ok ",name,", we will start again.")
                #set run back to 1 so it does not run nested while loop again
                run=1
                mode3(usernames,passwords,allpass,run)
                break
                
            else:
                print(name,", please try again as that input was not 'yes' or 'no'.")
                continue
        select()

#very important varable, this lets me run nested loop and than quit them when corect input is recieved
run=1

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
MASPASS = 'simple01yes'


print("Daniel Herbert, 23rd March 2019, Version 8 of Password safe.")

#the code that prevents user from entering the rest of the program unless they have this info

while True:
    #just simple username and password to stop someone random using the program
    userid = input("Enter the Master id: ")
    passuser = input("Enter the Master password: ")
    if userid == MASID and passuser == MASPASS:
        #I have not error checked for name as I let anyone be called what ever they want to be called
        name = input("What is you'r name?: ")
        print ("Secusfully signed in.")
        select()

    else:
        print("Sorry you have either entred the username or password incorectly, you need to ener these corectly to access the rest of the program")
        continue

"""            

"""
