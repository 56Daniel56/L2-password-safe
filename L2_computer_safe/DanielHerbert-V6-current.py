#L2-Password-Safe: V6
#Daniel Herbert
#28th March 2019

import time


#functions
#I have used multiple functions in this program as I will need to run this code over and over again

#function used as a print to separate the code
#looks cleaner for the user
def line():
    print("-----------------------------------------")
    

#mode 1 function lets the user veiw a certain account which is stored with in the program
#Will be also able to veiw user added accounts once they are created
def mode1(sites_list,usernames,passwords):
    #sites_list in this print statement tells the user of all websites that have the account info all ready saved
    while True:
        print("Which account would you like to select out of")
        #in this section I have added a for loop. This is so the list will print out clean with only the content and no square brackets
        for web in sites_list:
            print(web)
        website = input("Please enter one of the listed options: ").capitalize()
        line()
        #This part also compare website to the user input and see what password they would like to display

        if website in sites_list:
            #This line envolves comparig wattpass to all the elements in sites_list
            #I have this way because it is signifcuntly more cleaner than hard coding it and it allows for more websites than what is already hard coded
            print(usernames[website])
            print(passwords[website])
            time.sleep(2)
            break

        else:
            print("Sorry",name," this account is not available within this program. Please try typing in the website again typing the letters exactly the same as it displays.")
            continue

    

#function envolving creating a user specified account for a new website.
#asks for all needed infomation for an account, apends and inserts that info into the matching lists and dictionaries
def mode2(sites_list,usernames,passwords):
    #variable so the program knows the name of the website you want to add
    addweb = input("What is the name of the website you would like to add?: ").capitalize()
    adduser = input("What is the username you would like to add?: ")
    addpass = input("What is the name of the password you would like to add?: ")
    #appends the users website they would like to add to the sites_variable
    #I have used append because it will add the new element onto the end of the list and that is exactly where I want It
    sites_list.append(addweb)
    
    while True:
        #checks user entred the correct and are happy with the values they have entred
        confirm = input("Are you happy with what you have entred? 'yes' or 'no': ").lower()
        if confirm.startswith('y'):
            usernames[addweb] = ('Username:'+adduser)
            passwords[addweb] = ('Password:'+addpass)
            print(usernames[addweb])
            print(passwords[addweb])
            break
        elif confirm.startswith('n'):
            #starts mode 2 again so then the user can have another go at entering the website
            #I have done this because it makes my program more flexible and able to handle more tasks
            print("Ok",name,", we will start again.")
            print(sites_list)
            mode2(sites_list,usernames,passwords)
            break
        else:
            print("Please try again as that input was not 'yes' or 'no'.")
            continue
    


            

#mode 3 allows user to change a username or password for one of the websites
#asks user whether they want to change username or password
#Than asks them what website they want to change
#Than asks them for the change and inserts it into dictionary
def mode3(usernames,passwords,sites_list,run):
    while True:
        #I have used a nested while loop here so I am able to have an exception so that my program want break.
        #I am able to check validness for to different inputs
        #asking whether the username or password wants to be changed
        change = input("would you like to change your username or password: ").lower()
        #user whishes to change username
        if change == 'username':
            while run<=1:
                #displays all websites avilible to be changed
                print("What is the website you would like to change your username for?\nOut of")
                for web in sites_list:
                    print(web)
                uchange = input(": ").capitalize()
                if uchange in sites_list:
                    line()
                    newuse = input("What is the new username you would like to enter?: ")
                    #enters new username into the dictionary
                    usernames[uchange] = ('Username:'+newuse)
                    #shows the user that it has been changed
                    print(usernames[uchange],"is now set")
                    #changes run to run=2 so the loop will not be ran again
                    run=run+1
                    break
                else:
                    print("Sorry ",name," that is not a website or you have spelt it in corectly, please try again and enter carefully.")
                    continue
        #user whishes to change password
        elif change == 'password':
            while run<=1:
                #displays all websites avilible to be changed
                print("What is the website you would like to change your password for?\nOut of")
                for web in sites_list:
                    print(web)
                pchange = input(": ").capitalize()
                if pchange in sites_list:
                    line()
                    newpass = input("What is the new password you would like to enter?: ")
                    #enters new password into the dictionary
                    passwords[pchange] = ('Password:'+newpass)
                    #shows the user that it has been changed
                    print(passwords[pchange],"is now set")
                    #changes run to run=2 so the loop will not be ran again
                    run=run+1
                    break
                else:
                    print("Sorry, that is not an available website or you have spelt it incorrectly, please try again and enter your answer carefully.")
                    continue
        else:
            print("Sorry," ,name, " that was not a valid input. Try entering either 'username' or 'password'")
            continue
        while True:
            #checks user entred the correct values
            confirm = input("Are you happy with what you have changed?. 'yes' or 'no': ").lower()
            if confirm.startswith('y'):
                break
            elif confirm.startswith('n'):
                #give the user another go at entering their new username or password
                print("Ok ",name,", we will start again.")
                #set run back to 1 so it does not run nested while loop again
                run=1
                mode3(usernames,passwords,sites_list,run)
                break
                
            else:
                print(name,", please try again as that input was not 'yes' or 'no'.")
                continue
        break


#Variables

run=1
tries=0
#lists for storing websites, usernames and passwords

#stores the diffrent names of the websites that you have saved

sites_list = ['Amazon','Mightyape','Google']
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


#Code
#info on program to help marking
print("Daniel Herbert, 26th March 2019, Version 9 of Password safe.")
#the code that prevents user from entering the rest of the program unless they have this info
line()
name = input("What is you'r name?: ")
while True:
    #This line represents the amount of tries user can atempt before being kicked out of the program
    #I have done this to prevent people from entering a password 10000 times than eventuly getting it correct.
    if tries<3:
        #just simple username and password to stop someone random using the program + welcome message
        userid = input("Enter Master id: ")
        passuser = input("Enter Master password: ")
        if userid == MASID and passuser == MASPASS:
            #I have not error checked for name as I let anyone be called what ever they want to be called
            print ("Secusfully signed in.")
            line()
            print("Hello,",name,". This is a password safe programed in python to store account information for websites or anything else you desire.")
            print("There are several modes you can select within this password safe.")
            enter = input("Press enter when ready to start this program: ")
        else:
            tries = tries+1
            print("Sorry you have either entered the username or password incorrectly, you need to enter these correctly to access the rest of the program")
            continue
    else:
        print("Sorry you have reached the maximun amount of tries, goodbye.")
        quit()
    
    while True:
        line()
        print("\nYou can choose one of the following modes:\n('1')Find an existing account\n('2')Add a new account\n('3')Change an existing username or password\n('4')Exit the program")
        try:
            mode = int(input("Choose selected mode by entering one of the aforementioned numbers which corresponds to the desired selection: "))
            line()
            #once user has entred mode is mode 1 runs this code
            if mode == 1:
                #runs the code when the user is wanting to check for a existing username and password
                mode1(sites_list,usernames,passwords)
                continue
            elif mode == 2:
                #this runs if the user is wanting to insert a new account to the program
                mode2(sites_list,usernames,passwords)
                continue
            elif mode == 3:
                #mode 3 is to change an existing username or password
                mode3(usernames,passwords,sites_list,run)
                continue    
            elif mode == 4:
                #mode 4 quits the program
                print("Good bye")
                quit()

            #user has not entred a correct input tells them why and runs the loop again
            #here I have gone through and coded so that it tells the user exactly what they have done wrong
            #I have done this because next time the user tries a input they will know exactly how to fix it
            elif mode <1:
                #either too low
                print("Sorry",name,"That number is below the range of the requested values")
                continue

            elif mode >=5:
                #too high
                print("Sorry",name,"That number is above the range of requested values")
                continue

            
        except ValueError:
            #or not A number or float
            print("You have not entered a number or you have entered a float, Please read the question carefully and try again.")
            continue


