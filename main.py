# Write your pseudocode first!

# imports
import random
import pyperclip
# Welcome them

print("~~~~ Welcome to the Password Generator ~~~~~")
print()

# dictionary to save the passwords
passwords = {}
# variables
y = True
n = False
characters = "abcdefghijklmnopqrstuvwxyz1234567890"
# while loop
while True:
        website = input("what website will the password be used for? ")
        password = ""
        for i in range(10):
            password = password + random.choice(characters)
 # show pass word to user
        print("Your password is: ", password)
 #  add password to dictionary
        passwords[website] = password
 # copy password to the clipboard
        pyperclip.copy(passwords)
    # Reset password 
       # print all passwords from the dictionary
        print(passwords)
        answer = input("Would you like to create another password? y/n ")
        break    
if answer == "y":
    answer = y       
while answer == y:
         website = input("what website will the password be used for? ")
         print()
         password = ""

         for i in range(10):
            password = password + random.choice(characters)
            
         print("Your password is: ", password)
         passwords[website] = password
         pyperclip.copy(passwords)
         ans_dictionary = input("would you like to see all your passwords? ")
         if ans_dictionary == "yes":
               print()
               print(passwords)
               answer = input("Would you like to create another password? y/n ")
               if answer == "y":
                answer = y       
                while answer == y:
                 website = input("what website will the password be used for? ")
                 print()
                 password = ""

                 for i in range(10):
                  password = password + random.choice(characters)
            
                print("Your password is: ", password)
                passwords[website] = password
                pyperclip.copy(passwords)
                if answer == "n":
                  answer = y
                while answer == n:
                     break
 # ask if user wants to enter another password for a different website   


# make another password for a different website if the user wants 