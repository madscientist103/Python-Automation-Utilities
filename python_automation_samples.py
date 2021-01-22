# Clayton@RaezionSecurity
# Work-in-progress, this utility will serve as a demonstration of many of the powerful functions
# provided within built-in Python modules such as OS, to be be used for interaction with the host
# environment.


import os
from pathlib import Path

def main():

    menu()

def menu():

    while(True):

        print("\n**********Main Menu**********")
        print("\n1. OS Library Functions")
        print("\n9. Exit\n")

        Menu_Selection = int(input("\nChoose an option\n"))

        if Menu_Selection == 1:

            OS_Ops()

        elif Menu_Selection == 9:

            exit()

        else:

            print("\nSorry, not a valid selection, please try again :)\n")

def OS_Ops():

    OS_Ops_Run = 1

    while(OS_Ops_Run == 1):

        print("\n**********OS Library Functions Menu**********")
        print("\n1. Scan Items in Current Directory")
        print("\n2. Show Subdirectories Only")
        print("\n3. Show Files only")
        print("\n4. Show Relative Filepaths")
        print("\n5. Show Absolute Filepaths")
        print("\n9. Return to Main Menu\n")

        OS_Ops_Selection = int(input("\nPlease choose your OS library operation\n"))

        if OS_Ops_Selection == 1:

            print("\n**********Scanning Current Directory**********")

            for element in os.scandir():

                print(element)

        elif OS_Ops_Selection == 2:

            for element in os.scandir():

                if element.is_dir():

                    print(element)

        elif OS_Ops_Selection == 3:

            for element in os.scandir():

                if not element.is_dir():

                    print(element)

        elif OS_Ops_Selection == 4:

            for element in os.scandir():

                element_relative_file_path = Path(element)

                print(element_relative_file_path)

        elif OS_Ops_Selection == 5:

            for element in os.scandir():

                element_absolute_file_path = os.path.abspath(element)

                print(element_absolute_file_path)

        elif OS_Ops_Selection == 9:

            OS_Ops_Run = 0

        else:

            print("\nSorry, not a valid selection, please try again :)")

main()
