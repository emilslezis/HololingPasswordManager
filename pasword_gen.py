#Password generator
#Made by Emil Sležis


# Import needed modules

import string
import random

# Generate lists with symbols 

letters = list(string.ascii_letters)
digits = list(string.digits)
symbols = list(string.punctuation)

Characters = (letters, digits, symbols) 

# Whole program


def main(): # Main function

    action = input("Enter your action (s - see, c - create new - m - modify)")

    if action == "s":

        needed = str(input("Enter profile, which you want to see: "))
        readPassword(needed)
        continueProg()
        
    elif action == "c":       

        new_profile()
        continueProg()
  
    elif action == "m":

        modify = (input("Enter in which way you want to modify(c - change data d - delete data profile)"))

        if modify == "d":

            delitable = (input("Enter profile you want to delete"))
            deleteProfile(delitable)

        elif modify == "c":

            modifyProfile()
            continueProg()

        else:

            invalidCharacter()
            continueProg()

    else:

        invalidCharacter()
        
    
def new_profile(): #Function which gets needed data from user

    key = (input("Enter key of your password: "))
    email = (input("Enter your email: "))
    nick = (input("Enter your nickname: "))
    
    password = generatePassword()
    
    data = [key, email, nick, password]

    writeData(data)

def generatePassword(): # Function which generates password
    
    passwordList = []

    for i in range(20):

        charType = random.choice(Characters)
        newChar = random.choice(charType)
        passwordList.append(newChar)    

    password = ''.join([str(elem) for elem in passwordList])
    
    print(password)
    return(password)
    
def writeData(data): #Write data on document
    

    text_file = open("passwords.txt", "a") 
    text_file.write(data[0])
    text_file.write(" ")
    text_file.write(data[1])
    text_file.write(" ")
    text_file.write(data[2])
    text_file.write(" ")
    text_file.write(data[3])
    text_file.write("\n")

    text_file.close()


def readPassword(needed): # Read data from document
    
    with open('passwords.txt', 'r') as document:
        answer = {}
        for line in document:
            line = line.split()
            if not line:  # empty line?
                continue
            answer[line[0]] = line[1:]

    allData = (answer[needed])

    print("Email: " + allData[0])
    print("Nickname: " + allData[1])
    print("Password: " + allData[2])

def deleteProfile(nProfile): # Delete profile from document
    
    with open("passwords.txt", "r") as document: 
        
        #Make profile

        answer = {}
        for line in document:
            line = line.split()
            if not line:  # empty line?
                continue
            answer[line[0]] = line[1:]

        allData = (answer[nProfile])

        cprofile = (nProfile, " ", allData[0], " ", allData[1], " ", allData[2])

        # read data line by line  
        data = document.readlines() 
      
    # open file in write mode 
    with open("passwords.txt", "w") as f: 
      
        for line in data : 
          
            # condition for data to be deleted 
            if line.strip("\n") != cprofile :  
                f.write(line) 

def modifyProfile(): # Modify profile

    profile = (input("Enter profile you want to modify"))
    changes = (input("Enter what you want to change(l - login, e - email, p - password)"))
    
    with open('passwords.txt', 'r') as document:
        answer = {}
        for line in document:
            line = line.split()
            if not line:  # empty line?
                continue
            answer[line[0]] = line[1:]

    allData = (answer[profile])
    
    email = (allData[0])
    nickname = (allData[1])
    password = (allData[2])

    if changes == "l": # change login data

        nickname = (input("Enter your new nickname: "))
        deleteProfile(profile)
        data = [profile, email, nickname, password] 
        writeData(data)
   
    elif changes == "e": # change email data

        email = (input("Enter your new email: "))
        deleteProfile(profile)
        data = [profile, email, nickname, password] 
        writeData(data)

    elif changes == "p": # change password

        password = generatePassword()
        deleteProfile(profile)
        data = [profile, email, nickname, password] 
        writeData(data)

    else:

        invalidCharacter()
    

def invalidCharacter(): 

    print("wrong character")
        
    tryAgain = input("Do you want to try again?(y - yes, n - no)")

    if tryAgain == "y":
        main()

def continueProg(): # continue program after action

    answer = (input("Do you want to do something else?(y - yes, n - no)"))

    if answer == "y" or answer == "yes":

        main()
    
if __name__ == "__main__":
    
    main()
