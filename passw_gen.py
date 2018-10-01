
import random
import os
import os.path
import pyperclip

import time

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
    
print("\t\t\t\tWelcome to paswword generator\n")


#adding drive upload functionality
def drive():
    drive_q = str(input("Do you want to save the password to your Google Drive : "))

    if os.path.isfile("secured_pw.txt") == True:
        if drive_q in ['Y','y', 'yes','YES', 'Yes']:
            gauth = GoogleAuth()  # Authentication
            gauth.LocalWebserverAuth()
            drive = GoogleDrive(gauth)
            
            if os.path.isfile("dup.txt") == True:
                ls = open('dup.txt','r+')
                ls.truncate(0)
                ls.close()
            
            os.chmod("secured_pw.txt", 0o777)
            #copying the file content to another file
            with open("secured_pw.txt") as f:
                with open("dup.txt", "a") as f1:
                    for line in f:
                        f1.write(line)
            f1.close()
            os.chmod('secured_pw.txt', 0o444) # changing file permission to read only using octal notation
            f.close()
            # file upload procedure
            
            file_n = str(input("Enter the filename to be save in Google Drive : "))
            file1 = drive.CreateFile({'title': file_n + ' ' +  time.ctime()})
            file1.SetContentFile('dup.txt')
            file1.Upload()
            print("File sucessfully uploaded !")
            menu()
        else:
            menu()
    else:
        print("File to be uploaded does not exist !")
        menu()

        
        
#adding functionality of menu based operations
def menu():
    print("\n\t\t\t\tMENU\t\t\t\t")
    print("\t\t\t\t1. Generate password\n\t\t\t\t2. Delete password file\n\t\t\t\t3. Search for password\n\t\t\t\t4. Display saved p/w name\n\t\t\t\t5. Save to Drive\n\t\t\t\t6. Exit")
    option = int(input("Enter the number for operation : "))
    
    if option == 1:
        pw_gen()
    if option == 2:
        del_file()
    if option == 3:
        pw_search()
    if option == 4:
        disp_pw_name()
    if option == 5:
        drive()
    if option == 6:
        print("Thanks for using N1 Password Generator")
        exit()
    
def del_file():
    ques1 = str(input("Are you sure :  "))
    if ques1 in ['Y','y', 'yes','YES', 'Yes']:
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
        spl = "#@$&()+?#@$&()+?"# whenever change this string keep its length at least 10`
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
            print("Generating...")
            time.sleep(1)
            print("\n")
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
        if copy in ['Y','y', 'yes','YES', 'Yes']:
            pyperclip.copy(snap)
            pyperclip.paste()
        ques = str(input("Do you want to save the password : "))
        if ques in ['Y','y', 'yes','YES', 'Yes']:
            nn = str(input("\nEnter the name to identify your password in future : "))
            if os.path.isfile("secured_pw.txt") == True:
                os.chmod("secured_pw.txt", 0o777) # changing file permission to write using octal notation
            with open('secured_pw.txt', 'a') as f: # opening the file in access mode
                print(nn, "-", snap , file=f)
                os.chmod('secured_pw.txt', 0o444) # changing file permission to read only using octal notation
                f.close() # closing the file
            print("\nPassword was sucessfully saved.\n")
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


def disp_pw_name():
    if os.path.isfile("secured_pw.txt") == True:
        os.chmod('secured_pw.txt', 0o777)
        with open("secured_pw.txt") as f:
            pw_name = [line.split(None, 1) for line in f] # split the line one time only
            display = []
            l_pw_name = len(pw_name)
            for i in range(l_pw_name):
                display.append(pw_name[i][0])
            display = sorted(display)
            l_display = len(display)
            for i in range(l_display):
                print(i+1, "->",display[i])
            os.chmod('secured_pw.txt', 0o444)
            f.close()
            menu()
            
    else:
        print("\nNo saved file found. Please generate the password and save it.\n")
        menu()
            

menu()
