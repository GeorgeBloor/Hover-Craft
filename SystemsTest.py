#-------------------------------------------------------------------------------
# Name:        Hover_Craft__SYSTEMS-TESTING-CODE
# Author:      Kyle Cotton
# Version:     1.2
#-------------------------------------------------------------------------------

"""
PASSING "HELP" WILL GIVE BASIC HELP AND STRUCTURE THEN EXIT THE PROGRAM
PASSING ANY VARIABLE PRGRAM WILL CHECK IF VALID THEN PREFROM THAT TEST
PASSING NO ARGUMENTS WILL PREFROM FULL CHECK
"""



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

def SystemsTest(SYSTEMS=["lift", "rudder", "thrust"]):
    if SYSTEMS == "help":
        print("Pass the systems you require in a list like [\"thrust\", \"lift\"], just pass no arguments to test all systems")
        return
    print("\nSYSTEMS TEST INITIATED\n")
    AllSystems = ["lift", "rudder", "thrust"]
    SystemNotTest = []
    SystemsToTest = SYSTEMS
    InvalidSystems = []

    #populates the lisf of systems that are invalid
    for i in range(len(SystemsToTest)):
        if SystemsToTest[i] not in AllSystems:
            InvalidSystems.append(SystemsToTest[i])
    #populates the list of systems that wont be tested
    for i in range(len(AllSystems)):
        if AllSystems[i] not in SystemsToTest:
            SystemNotTest.append(AllSystems[i])

    print("The following are invalid systems ==> {}".format(InvalidSystems))
    print("The following are systems that wont be tested==> {}".format(SystemNotTest))
    print("\n###    TESTING  ==>{}    ###\n".format(SystemsToTest))

#Looping through systems
    for i in range(len(SystemsToTest)):
        SystemSpecificTest(SystemsToTest[i])

#SystemsTest(["pedals","lift","seat","Ruddesr","rudder","thrust"])
