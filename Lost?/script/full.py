import time
import os
import subprocess
from pyfiglet import Figlet

def greeting():
    R = "\033[1;31m"
    G = "\033[1;32m"
    Y = "\033[1;33m"
    C = "\033[1;36m"
    N = "\033[0m"

    f = Figlet(font='slant')

    print(R + f.renderText('Are you lost') + N)

    print(f"{G}[{Y}!{G}] {C}Welcome to the system{N}")

greeting()
time.sleep(2.5)
print("Loading...")

usr_name = subprocess.run(["whoami"] , capture_output=True).stdout.decode().strip()

def ask_the_person_what_he_want():
    print('''
    Here is the list you can choose from:
    [1] - show network status       [6] - show the date and time
    [2] - show disk usage           [7] - show the system information
    [3] - how to change directory   [8] - show the process list
    [4] - what is the current user   [9] - show the environment variables
    [5] - start the gui             [10] - show the help information        
''')
    

ask_the_person_what_he_want()
usr_choice = input(f'choose only valid number Mr {usr_name} : ')
def choices():

    if usr_choice == "1":
        subprocess.run(["ifconfig"])
    elif usr_choice == "2":
        subprocess.run(["df", "-h"])
    elif usr_choice == "3":
        print("To change directory, use the 'cd' command followed by the path of the directory you want to navigate to.")
    elif usr_choice == "4":
        subprocess.run(["whoami"])
    elif usr_choice == "5":
        subprocess.run(["startx"])
    elif usr_choice == "6":
        subprocess.run(["date"])
    elif usr_choice == "7":
        subprocess.run(["uname", "-a"])
    elif usr_choice == "8":
        subprocess.run(["ps", "aux"])
    elif usr_choice == "9":
        subprocess.run(["printenv"])
    elif usr_choice == "10":
        print("Help information: \n1 - show network status\n2 - show disk usage\n3 - how to change directory\n4 - what is the current user\n5 - start the gui\n6 - show the date and time\n7 - show the system information\n8 - show the process list\n9 - show the environment variables\n10 - show the help information")
    else:
        print("Invalid choice. Please choose a number from the list.")


choices()

if __name__ == "__main__":
    print(f'Thank you for using our system, Mr {subprocess.run(["whoami"], capture_output=True).stdout.decode().strip()}')

else:
    print("Exiting the program.")
