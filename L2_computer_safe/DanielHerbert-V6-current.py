#L2-Password-Safe: V6
#Daniel Herbert
#28th March 2019
#
# This program is the first stage of a password manager - which provides an interface to remember the multitude of passwords use across various web sites and/or applications
# which require a user name and password combination, to provide authentication access.
#
# There are three main functions, called from a main menu
# 1. View
# 2. Add
# 3. Modify (change)
#
# There are three hard coded websites, with respective username and passwords - this is not good practice for an actual
# password manager app ( storing passwords in application code is not good practice ) though used here for illustrative purposes.
#
# Note: This program contains no real passwords, I use.
#
# Limitations of this program
# 1. This version will not store the username/password combo, persistently, meaning a restart will lose any previous entries
# 2. Passwords entered, are displayed in plain text - no masking on the display or encrypting ( hash alogrithm )  the input.
# 


import time


#function used as a print to separate the code
#looks cleaner for the user
def print_dash_line():
    print("-----------------------------------------")
    

### view ### :  function lets the user view a certain account which is stored with in the program
#Will be also able to view user added accounts once they are created
def view(sites_list,usernames,passwords):
    #sites_list in this print statement tells the user of all websites that have the account info already saved
    print("Which account would you like to select out of")
    #in this section I have added a for loop. This is so the list will print out clean with only the content and no square brackets
    for web in sites_list:
        print(sites_list.index(web),web)

    while True:
        try:
            website = int(input("Please enter the corresponding number: "))
            print_dash_line()
            
            if website >= len(sites_list):
                print ("Sorry " +name+ ", that number is greater than the requested range. Look at the question carefully and try again.")
                continue
            elif website < 0:
                print("Sorry " +name+ ", that number is smaller than the requested range. Look at the question carefully and try again.")
                continue
            
            else:
                print(usernames.get(sites_list[website]))
                print(passwords.get(sites_list[website]))
                time.sleep(2)
                break

        except ValueError:
            print("That is not a number " +name+ ", try entering a number.")
            continue

    

            
 
### add ### function allowing creation of a user specified website.
#asks for all needed information for an account, apends and inserts that info into the matching lists and dictionaries
def add(sites_list,usernames,passwords):
    while True:
        #variable so the program knows the name of the website you want to add
        addweb = input("What is the name of the website you would like to add?: ").capitalize()
        if addweb in sites_list:
            print("Sorry " +name+ ",that is already an existing website. Please try again with a different website name.")
            continue
        #appends the users website they would like to add to the sites_variable
        #I have used append because it will add the new element onto the end of the list and that is exactly where I want It
        elif not addweb:
            print("A website name is required, please enter one")
            continue
        else:
            adduser = input("What is the username you would like to add?: ")
            addpass = input("What is the name of the password you would like to add?: ")
            sites_list.append(addweb)
            break
        
        
    while True:
        #checks user entered the correctly and are happy with the values they have entered
        confirm = input("Are you happy with what you have entered? 'yes' or 'no': ").lower()
        if confirm.startswith('y'):
            usernames[addweb] = ('Username:'+adduser)
            passwords[addweb] = ('Password:'+addpass)
            print(usernames[addweb])
            print(passwords[addweb])
            break
        elif confirm.startswith('n'):
            #starts mode 2 again so then the user can have another go at entering the website
            #I have done this because it makes my program more flexible and able to handle more tasks
            print("Ok " +name+ ", we will go back to the main menu.")
            break
        else:
            print("Please try again as that input was not 'yes' or 'no'.")
            continue
    


            

### modify ### allows user to change a username or password for one of the websites
#asks user whether they want to change username or password
#Than asks them what website they want to change
#Than asks them for the change and inserts it into dictionary
def modify(usernames,passwords,sites_list,run):
    while True:
        #I have used a nested while loop here so I am able to have an exception so that my program want break.
        #I am able to check validness for to different inputs
        #asking whether the username or password wants to be changed
        change = input("would you like to change your username or password: ").lower()
        #user wishes to change username
        if change.startswith('u'):
            while run<=1:
                try:
                    #displays all websites available  to be changed
                    print("What is the website you would like to change your password for?\nOut of")
                    for web in sites_list:
                        print(sites_list.index(web),web)
                    uchange = int(input("Please enter the site number you wish to change: "))
                    
                    if uchange >= len(sites_list):
                        print("Sorry " +name+ ", that number is greater than the requested range. Look at the question carefully and try again.")


                    elif uchange < 0:
                        print("Sorry " +name+ ", that number is smaller than the requested range. Look at the question carefully and try again.")

                    else:
                        site_change = sites_list[uchange]
                        print_dash_line()
                        newuse = input("What is the new username you would like to enter?: ")
                        #enters new username into the dictionary
                        usernames[site_change] = ('Username: '+newuse)
                        #shows the user that it has been changed
                        print(usernames[site_change],"is now set")
                        #changes run to run=2 so the loop will not be ran again
                        run=run+1
                        break
                except ValueError:
                    print("I can not accept the value you have entered " +name+ ", try entering a whole number.")
                    continue

                
        #user wishes to change password
        elif change.startswith('p'):
            while run<=1:
                try:
                    #displays all websites available  to be changed
                    print("What is the website you would like to change your password for?\nOut of")
                    for web in sites_list:
                        print(sites_list.index(web),web)
                    pchange = int(input("Please enter the site number you wish to change: "))

                    
                    if uchange >= len(sites_list):
                        print("Sorry " +name+ ", that number is greater than the requested range. Look at the question carefully and try again.")


                    elif uchange < 0:
                        print("Sorry " +name+ ", that number is smaller than the requested range. Look at the question carefully and try again.")


                    

            
                    
                    else:
                        site_change = sites_list[pchange]
                        print_dash_line()
                        newpass = input("What is the new password you would like to enter?: ")
                        #enters new password into the dictionary
                        passwords[site_change] = ('Password: '+newpass)
                        #shows the user that it has been changed
                        print(passwords[site_change],"is now set")
                        #changes run to run=2 so the loop will not be ran again
                        run=run+1
                        break

                except ValueError:
                    print("Sorry," +name+ " that was not a valid input. Try entering either 'username' or 'password'")
                    continue


        else:
            print("Sorry," +name+ " that was not a valid input. Try entering either username or password")
            continue
            
    while True:
        #checks user entered the correct values
        confirm = input("Are you happy with what you have changed?. 'yes' or 'no': ").lower()
        if confirm.startswith('y'):
            break
        elif confirm.startswith('n'):
            #give the user another go at entering their new username or password
            print("Ok " +name+ ", we will go back to the main menu.")
            #set run back to 1 so it does not run nested while loop again
            run=1
            break
            
        else:
            print(name,", please try again as that input was not 'yes' or 'no'.")
            continue
        break


#Variables

# run is used to break out of nested loops
run=1
# amount of attempts to enter the password safe app
# if you exceed three, the app will exit
tries=0


#lists for storing websites, usernames and passwords
#stores the different names of the websites that you have saved

sites_list = ['Amazon','Mightyape','Google']

#I have decided to use dictionaries as it allows me to store multiple keys and retrieve certain ones
usernames = {'Amazon':'Username: Danny',
             'Mightyape':'Username: Danny89',
             'Google':'Username: Bobby'}

passwords = {'Amazon':'Password: Super01',
             'Mightyape':'Password: BOyshigh61',
             'Google':'Password: superduper33'}


#defines master id and master password. You have to enter these to access the program
MASID = 'daniel.h'
MASPASS = 'simple01yes'

VERSION = 'Version 6'
DATE = '26th March 2019'

# printinfo on program
print("Daniel Herbert, " + DATE + " , " + VERSION + " Password safe.")

# check user has access to run this program
print_dash_line()
name = input("What is your name?: ")
while True:
    #This line represents the amount of tries user can attempt before being kicked out of the program
    #I have done this to prevent people from entering a password 10000 times then eventually getting it correct.
    if tries<3:
        #just simple username and password to stop someone random using the program + welcome message
        userid = input("Enter Master id: ")
        passuser = input("Enter Master password: ")
        if userid == MASID and passuser == MASPASS:
            #I have not error checked for name as I let anyone be called whatever they want to be called
            print ("Successfully signed in.")
            print_dash_line()
            print("Hello " +name+ ". This is a password safe programed in python to store account information for websites or anything else you desire.")
            print("There are several modes you can select within this password safe.")
            enter = input("Press enter when ready to start this program: ")
        else:
            tries = tries+1
            print("Sorry you have either entered the username or password incorrectly, you need to enter these correctly to access the rest of the program")
            continue
    else:
        print("Sorry you have reached the maximum amount of tries, goodbye.")
        quit()
    
    while True:
        print_dash_line()
        print("\nYou can choose one of the following modes:\n('1')Find an existing account\n('2')Add a new account\n('3')Change an existing username or password\n('4')Exit the program")
        try:
            mode = int(input("Choose selected mode by entering one of the aforementioned numbers which corresponds to the desired selection: "))
            print_dash_line()
            #once user has entered mode is mode 1 runs this code
            if mode == 1:
                #runs the code when the user is wanting to check for a existing username and password
                view(sites_list,usernames,passwords)
                continue
            elif mode == 2:
                #this runs if the user is wanting to insert a new account to the program
                add(sites_list,usernames,passwords)
                continue
            elif mode == 3:
                #mode 3 is to change an existing username or password
                modify(usernames,passwords,sites_list,run)
                continue    
            elif mode == 4:
                #mode 4 quits the program
                print("Good bye")
                quit()

            #user has not entered a correct input tells them why and runs the loop again
            #here I have gone through and coded so that it tells the user exactly what they have done wrong
            #I have done this because next time the user tries a input they will know exactly how to fix it
            elif mode <1:
                #either too low
                print("Sorry " +name+ "That number is below the range of the requested values")
                continue

            elif mode >=5:
                #too high
                print("Sorry " +name+ ", that number is above the range of requested values")
                continue

            
        except ValueError:
        #or not A number or float
            print("You have not entered a number or you have entered a float, Please read the question carefully and try again.")
            continue


