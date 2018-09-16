# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 23:09:08 2018
@author: Snik
"""

import random
import os
import os.path
import pyperclip

print("\t\t\t\tWelcome to paswword generator\n\n")

#adding functionality of menu based operations
def menu():
    print("\n\n\t\t\t\tMENU\t\t\t\t")
    print("\t\t\t\t1. Generate password\n\t\t\t\t2. Delete password file\n\t\t\t\t3. Search for password\n\t\t\t\t4. Exit")
    
    option = int(input("Enter the number for operation : "))
    
    if option == 1:
        pw_gen()
    if option == 2:
        del_file()
    if option == 3:
        pw_search()
    if option == 4:
        print("Thanks for using Snapnab_N1 Password Generator")
        exit()
   
def del_file():
    ques1 = str(input("Are you sure :  "))
    if ques1 in ['Y','y', 'yes','YES']:
        if os.path.isfile("secured_pw.txt") == True:
            os.chmod("secured_pw.txt", 0o777)
            os.remove("secured_pw.txt")
            print("File has been sucessfully removed.\n")
            menu()
        else:
            print("The file does not exist\n")
            menu()
    else:
        menu()

def pw_gen():
        length = int(input("Enter minimum of 6 as length of password : "))  #taking input for the length of the password 

        while length < 6:       #checking for the valid input 
            print("Enter the valid input i.e greater than or equal to 6 ")
            length = int(input())
        lower = "qaplzmxnksowiedjncbvhfurytg"
        lower_l = list(lower)
        upper = "PQOWKSJDIEHFURZXGYCTMVNB"
        upper_l = list(upper)
        spl = "#@$&()+?#@$&()+?"
        spl_l = list(spl)
        fin = []
        # final addition to list and then converting to string
        for i in range(length):
        #shuffeling all the elements list in order to get the new password everytime 
            random.shuffle(lower_l)
            num = str(random.random())
            num = num[len(num)-4:]
            num = int(num)
            num = num%random.randint(1,9)
            
            fin.extend(lower_l[num])
            fin.extend(upper_l[num])
            fin.extend(spl_l[num])
            fin.append(num)
        final = fin[0:length]
        random.shuffle(final)
        count_l = 0
        count_u = 0
        count_n = 0
        count_spl = 0
        for i in range(length):
            if str(fin[i]).islower() == True:
                count_l += 1
            elif str(fin[i]).isupper() == True:
                count_u += 1
            elif  type(fin[i]) == int:
                count_n += 1
            else:
                count_spl += 1
        # Just a sanity check of the password strength
        
        if count_l != 0 and count_spl != 0 and count_u != 0 and count_n != 0:
            print("Great")
            print("Your password contains : ",count_spl, " special characters.")
            print("Your password contains : ",count_u, " uppercase characters.")
            print("Your password contains : ",count_n, " numbers.")
            print("Your password contains : ",count_l, " lowercase characters.")
        else:
            print("Unable to generate // Please try again later")
        fine= []

        for i in range(length):
            fine.append(str(final[i]))
        snap = "".join(fine)
        print("\nThe password is : ",snap)
        # adding functionality of cpoying the result to clipboard
        copy = str(input("Do you want to copy the password to the clipboard : "))
        if copy in ['Y','y', 'yes','YES']:
            pyperclip.copy(snap)
            pyperclip.paste()
        ques = str(input("Do you want to save the password : "))
        if ques in ['Y','y', 'yes','YES']:
            nab = str(input("\nEnter the name to identify your password in future : "))
            if os.path.isfile("secured_pw.txt") == True:
                os.chmod("secured_pw.txt", 0o777) # changing file permission to write using octal notation
            with open('secured_pw.txt', 'a') as f: # opening the file in access mode
                print(nab, "-", snap, file=f)
                os.chmod('secured_pw.txt', 0o444) # changing file permission to read only using octal notation
                f.close() # closing the file
            menu()
        else:
            menu()
            
   
# adding functionality of searching through the file created
def pw_search():
        if os.path.isfile("secured_pw.txt") == True:
            query = str(input("Search with the saved name for the password : "))
            os.chmod('secured_pw.txt', 0o777)
            searchfile = open("secured_pw.txt", "r")
            for line in searchfile:
                if query in line: 
                    print(line)
                    os.chmod('secured_pw.txt', 0o444) 
            searchfile.close()
            menu()
        else:
            print("File does not exist")
            menu()




menu()
 