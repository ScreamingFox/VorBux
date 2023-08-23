##Created by Vortex for Ziinoe!##
import time 
import pyautogui





##Startup motd here 
##op = open('motd')
##for each_line in op:
  ##  print(each_line)


start = open('motd', 'r')
file_contents = start.read()
print(file_contents)




print("-------------------------------------------------------------------------")
print("Version 1.2.0 BETA")
print("--------------")
print("|DISCLAMER!!!|")
print("--------------- please note there is a possiblity that you may be banned")
print("for using this software! you must agree that you understand the risks of this ")
print("and im not resosable for acount lose!!!")

##first input:3
terms = input("y/n?")
if terms == "y":
    print("Thank you! you may countine")
    print("next you must select and use the wordlist of your choice")
    print("1# Majria")
    print("2# Fluke")
    print("3# Telephone")
    print("4# Odin")
    print("5# custom path")
    print("Yes i am a furry LOL")
    selct = input("Select list option ")
    if selct == "1":
        print("Majria")
        
        input("press enter when ready to start")
        for counter in range(1, 5):

            ##time
            print(counter)
            time.sleep(3)
            print("starting")
            #def sendmain():
        start1 = open('processMotd.txt', 'r')
        fc = start1.read()
        print(fc)
        text = open('Majria')
        for each_line in text:
            pyautogui.typewrite(each_line)
            pyautogui.press('enter')
            print("Atteiton!: VorBux sleep for 5 till next attempt....")
            time.sleep(5)

    if selct == "2":
        print("Fluke")
        
        input("press enter when ready to start")
        for counter in range(1, 5):

            ##time
            print(counter)
            time.sleep(3)
            print("starting")
            #def sendmain():
        text = open('Fluke')
        for each_line in text:
            pyautogui.typewrite(each_line)
            pyautogui.press('enter')
            print("Atteiton!: VorBux sleep for 5 till next attempt....")
            time.sleep(5)

    if selct == "3":

        print("Telephone")
    if selct == "4":
        print("odin")
    if selct == "5":
        inpt = input("Type file destnation:")
        import inpt


    

    
##else terms == "n":
 ##   print("i am sorry, you must agree have a nice day!")