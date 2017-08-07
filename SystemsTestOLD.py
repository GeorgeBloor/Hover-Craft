#-------------------------------------------------------------------------------
# Name:        Hover_Craft__SYSTEMS-TESTING-CODE
# Author:      Kyle Cotton
# Version:     1.2
#-------------------------------------------------------------------------------

def SystemsTest(SYSTEMS="All"):
    print("\nSYSTEMS TEST INITIATED\n")
#Defining Structures
    SystemsToTest = []
    SystemNotTest = []
    AllSystems = ["lift", "rudder", "thrust"]

#Function for testing specific systems
    def SystemSpecificTest(System):
        #Print Statemants placeholders for code
        if System=="lift":
            print("LIFT CODE HERE")
            return
        if System=="rudder":
            print("RUDDER CODE HERE")
            return
        if System=="thrust":
            print("THRUST CODE HERE")
            return
        return


    #Simple bypass if you want to test all systems without further input
    if SYSTEMS.lower() == "all":
        SystemsToTest = AllSystems
    else:
        for i in range(len(AllSystems)):
            options = input("Do you want to test [ {} ] (Y/N)".format(AllSystems[i].upper()))

            if options == "Y" or len(options) == 0:
                SystemsToTest.append(AllSystems[i])
            else:
                SystemNotTest.append(AllSystems[i])

#Printing to aid user
    if len(SystemsToTest) != 0:
        print("\n###    Testing    ###")
        for i in range(len(SystemsToTest)):
            print(SystemsToTest[i])
    if len(SystemNotTest) != 0:
        print("\n###    Not Testing    ###")
        for i in range(len(SystemNotTest)):
            print(SystemNotTest[i])
            print
#Looping through systems
    for i in range(len(SystemsToTest)):
        SystemSpecificTest(SystemsToTest[i])

#BEFORE PUSHING CODE COMMENT OUT BELOW LINE
#SystemsTest(SYSTEMS="ALL")