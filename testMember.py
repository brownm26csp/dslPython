'''
Melissa Brown

CSC 330 Language Design and Implementation

Session 5

Create a DSL

I apologize for two files being named the same. By the time I got to it I was in too deep and renaming was 
causing errors, and I'd rather it worked.
'''

import sys
import importlib

# Ensures proper syntax to run the dsl
if len(sys.argv) != 2:
    print('usage: %s <src.dsl>' % sys.argv[0])
    sys.exit(1)

# ensures access to module files
sys.path.insert(0, '/Users/melis/Documents/CSC330/dslPython/modules')
with open(sys.argv[1], 'r') as file:

    # methods which exist in the testMember module
    acceptedMethods = ["memberIsCorrect","firstNameIsCorrect","lastNameIsCorrect","numberSessionsIsCorrect",\
                       "isBannedIsCorrect","memberIdIsCorrect","canSetFirstName","canSetLastName",\
                        "canSetNumberSessions","canSetIsBanned"]
    for line in file:
        line = line.strip()

        # will skip any "comment" lines or empty lines
        if not line or line[0] == "#":
            continue
        parts = line.split()

        print("line testing: ", line)
        # retrieves name of method and check it is in accepted methods
        findMethod = parts[1]
        methodExists = any(x for x in acceptedMethods if x == findMethod)

        # if user has entered an incorrect method in error, will continue in loop
        if not methodExists:
            print ("method does not exist")
            continue

        # module file in which to search for functions
        mod = importlib.import_module(parts[0])

        # memberIsCorrect has 5 arguments
        if (findMethod == acceptedMethods[0]):
            print(acceptedMethods[0])
            print(getattr(mod, parts[1])(parts[2], parts[3], parts[4], parts[5], parts[6]))

        # all other functions have 1 argument
        else:
            print(getattr(mod,parts[1])(parts[2]))
        
        # new line for readability
        print("\n")