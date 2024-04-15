'''
Melissa Brown

CSC 330 Language Design and Implementation

Session 5

Create a DSL
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

    # methods which exist in the testMemberSession module
    acceptedMethods = ["canCreateSession","canGetDate","canGetTime","canGetLength","canGetMaxAttendees",\
                       "canGetAttendeeList","canSetDate","canSetTime","canSetLength","canSetMaxAttendees",\
                        "canAddToList","cannotAddAlreadyJoined","cannotAddMemberBanned","cannotAddSessionFull",\
                        "canRemoveIfInList","cannotRemoveIfNotInList","cannotRemoveIfNotInList"]
    for line in file:
        line = line.strip()

        # will skip any "comment" lines or empty lines
        if not line or line[0] == "#":
            continue
        print("line: ", line)
        parts = line.split()

        # retrieves name of method and check it is in accepted methods
        findMethod = parts[1]
        methodExists = any(x for x in acceptedMethods if x == findMethod)

        # if user has entered an incorrect method in error, will continue in loop
        if not methodExists:
            print ("method does not exist")
            continue

        # module file in which to search for functions
        mod = importlib.import_module(parts[0])

        # canCreateSession has 8 arguments
        if (findMethod == acceptedMethods[0]):
            print(acceptedMethods[0])
            print(getattr(mod, parts[1])(parts[2], parts[3], parts[4], parts[5], parts[6], parts[7], parts[8], parts[9]))

        # cannotAddAlreadyJoined, cannotAddMemberBanned, cannotAddSessionFull,
        # canRemoveIfInList, and cannotRemoveIfNotInList have 7 arguments
        elif len(parts) == 7:
            print(getattr(mod,parts[1])(parts[2],parts[3],parts[4],parts[5],parts[6]))

        # canGetDate, canGetTime, canSetDate, and canSetTime have 3 arguments
        elif len(parts) == 5:
            print("we are testing: ", findMethod)
            print(getattr(mod,parts[1])(parts[2], parts[3], parts[4]))

        # I don't think anything has 2 arguments but I'm too afraid to change anything at this point
        elif len(parts) == 4:
            print(getattr(mod,parts[1])(parts[2], parts[3]))

        # canGetLength, canGetMaxAttendees, canGetAttendeeList, canSetLength and canSetMaxAttendees
        # have 1 argument
        elif len(parts) == 3:
            print(getattr(mod,parts[1])(parts[2]))
        # all others have no arguments
        else:
            print(getattr(mod,parts[1]))
        # new line for readability
        print("\n")