# Menu program for Programming Final Project
# Used with Github to ensure that students know the GitHub process.

semester = "ITSE1479 - Spring 2023";

def main():
    #*****************************************************************
    # jumpTable for all functions
    # 
    # Modify your line to create a jumpTable entry for your 
    #   function.  Replace stub() with the name of your function that 
    #   you added to the end this code section.
    #
    # Notes:
    #    jumpTables hold the name of a function, not the variables
    #       that are passed to it.  See smileyFunction for a way
    #       to pass variables manually, 
    #       OR create your own inputs inside of your function to 
    #           collect user input.
    #   Use the following code at the end of your function to 
    #       pause the program
    #           print()
    #           print("Press ENTER to return to the menu")
    #           input()
    #   DO NOT TRASH THE CALL TO main() at the end.  Thanks.
    #*****************************************************************
    jumpTable = {}
    jumpTable['1'] = smileyFunction       # Smiley - call to function goes here
    jumpTable['2'] = stub                 # Becker - call to function goes here
    jumpTable['3'] = stub                 # Cantu - call to function goes here
    jumpTable['4'] = stub                 # Delgado - call to function goes here
    jumpTable['5'] = stub                 # Garcia Tadeo - call to function goes here
    jumpTable['6'] = gloriaFunction       # Gloria - call to function goes here
    jumpTable['7'] = stub                 # Menifee - call to function goes here
    jumpTable['8'] = stub                 # Rountree - call to function goes here
    jumpTable['9'] = stub                 # Stewart - call to function goes here
    jumpTable['10'] = stub                # Sylvester - call to function goes here

    chrChoice = ""      # To hold a menu choice

    # Constants for the menu choices
    EXIT = '0';

    while chrChoice != '0':
        # Display the menu and get the user's choice.
        showMenu();
        
        chrChoice = input("Enter your selection (0 to exit): ")
        
        if(chrChoice.isdigit() and int(chrChoice) < (len(jumpTable) + 1)):
            # Validate the menu selection.
            if chrChoice == EXIT:
                print()
                print("Thank for using the", semester, "Menu Program. ")
                print("Have a nice day.")
            else:
                jumpTable[chrChoice]()
        else:
            print("Please enter one of the numeric values from the menu.  Thanks")
            print("Press ENTER to continue.")
            input()    

            

#*****************************************************************
# Definition of function showMenu which displays the menu.       *
#*****************************************************************

def showMenu():
    print("*******************************************************************")
    print("*   Welcome to the ", semester, " Program!")
    print("*      Make a selection from the list below to see student output *")
    print("*                                                                 *")
    print("*      Enter 0 and press Enter to Quit.                           *")
    print("*******************************************************************")

    print("1.  Smiley")
    print("2.  Becker")
    print("3.  Cantu")
    print("4.  Delgado")
    print("5.  Garcia Tadeo")
    print("6.  Gloria")
    print("7.  Menifee")
    print("8.  Rountree")
    print("9.  Stewart")
    print("10. Sylvester")
    print()

# *****************************************************************************************
# Function Definitions Section
# *****************************************************************************************
# Add your function below.  
#  
# FunctionName:  lastnameFunction(your parameters)
# *****************************************************************************************

# *****************************************************************************************
# FUNCTION:         stub (default for menu)
# DESCRIPTION:      stub function created to print a single message: Not Implemented Yet
# OUTPUT EXAMPLE:   User enters any jumpTable entry that has not been created yet
# *****************************************************************************************
def gloriaFunction():


    import random
    play = str(input("Do you want to play rock, paper, scissors? y or n? "))
    while (play == "y"):
        choice = int(input("Make a choice! 1 for rock, 2 for paper, or 3 for scissors! "))
        compchoice = random.randint(1,3)
        if (choice == 1):
            if (compchoice == 1):
                print("Computer chose rock!")
                play = str(input("Draw! Play again? y or n? "))
            elif (compchoice == 2):
                print("Computer chose paper!")
                play = str(input("Computer wins! Play again? y or n? "))
            else:
                print("Computer chose scissors")
                play = str(input("Player wins! Play again? y or n?"))
        elif (choice == 2):
                if (compchoice == 1):
                    print("Computer chose rock!")
                    play = str(input("Player wins! Play again? y or n? "))
                elif (compchoice == 2):
                    print("Computer chose paper!")
                    play = str(input("Draw! Play again? y or n? "))
                else:
                    print("Comupter chose scissors")
                    play = str(input("Computer wins! Play again? y or n?"))
        else:
                if (compchoice == 1):
                    print("Computer chose rock!")
                    play = str(input("Computer wins! Play again? y or n? "))
                elif (compchoice == 2):
                    print("Computer chose paper!")
                    play = str(input("Player wins! Play again? y or n? "))
                else:
                    print("Compter chose scissors")
                    play = str(input("Draw! Play again? y or n? "))
    print("Thanks for playing!")
    
    print("Press ENTER to continue.")
    input()    

# *****************************************************************************************
# FUNCTION:         smileyFunction
# DESCRIPTION:      calls SmileyFib with a parameter of 11
#                   prints the Fibonacci series as defined by the input value
# OUTPUT EXAMPLE:   User enters 11
#                   Program outputs the following:
#                      Fibonacci Sequence (9 iterations): 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
# *****************************************************************************************
def smileyFunction():
    smileyFib(11)
    print("Press ENTER to continue.")
    input()    

def smileyFib(numberOfTimes):
    current = 0
    nextOne = 1
    nextTerm = 0

    print()
    print()
    print("Fibonacci Sequence (", str(numberOfTimes)," iterations)")

    for i in range(0, numberOfTimes):
        if (i == 1):                    # Prints the first term
            print(str(current), end= '')

        elif (i == 2):                 # Prints the second term
            print(str(nextOne), end = '')
        else:                          # Prints all subsequent terms
            nextTerm = current + nextOne;
            current = nextOne;
            nextOne = nextTerm;

            print(str(nextTerm), end = '')

        if (i + 1) < numberOfTimes:
            print(", ", end = '')

    print()
    print()

#*****************************************************************
# Please leave me alone,
#   Sincerely,
#       main()
#*****************************************************************
main()
