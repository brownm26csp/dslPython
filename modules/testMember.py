'''
Melissa Brown

CSC 330 Language Design and Implementation

Session 5

Create a DSL

Test methods for FightClubmember class
'''

import fightClubMember

# should return true if a member can be created, that is, all the getter methods return the values put into the constructor
def memberIsCorrect(fName, lName, numSessions, isBanned, id):
    myNewMember = fightClubMember.FightClubMember(fName, lName, numSessions, isBanned, id)
    return "Member is the same: ", (myNewMember.getFirstName() == fName) & (myNewMember.getLastName() == lName)\
           & (myNewMember.getNumberOfSessionsAttended() == numSessions) & (myNewMember.getIsBanned() == isBanned)\
           & (myNewMember.getMemberId() == id)

# testing getter for firstName attribute
def firstNameIsCorrect(fName):
    myFakeMember = fightClubMember.FightClubMember(fName, "fake", 0, True, "fakeId")
    return "first name is correct: ", myFakeMember.getFirstName() == fName

# testing getter for lastName attribute
def lastNameIsCorrect(lName):
    myFakeMember = fightClubMember.FightClubMember("fake", lName, 0, True, "fakeId")
    return "last name is correct: ", myFakeMember.getLastName() == lName

# testing getter for number of sessions attended attribute
def numberSessionsIsCorrect(numSessions):
    myFakeMember = fightClubMember.FightClubMember("fake", "fake", numSessions, True, "fakeId")
    return "number of sessions attended is correct: ", myFakeMember.getNumberOfSessionsAttended() == numSessions

# testing getter for isBanned attribute
def isBannedIsCorrect(isBanned):
    myFakeMember = fightClubMember.FightClubMember("fake", "fake", 0, isBanned, "fakeId")
    return "isBanned is correct: ", myFakeMember.getIsBanned() == isBanned

# testing getter for memberId attribute
def memberIdIsCorrect(memberId):
    myFakeMember = fightClubMember.FightClubMember("fake", "fake", 0, "fake", memberId)
    return "memberId is correct: ", myFakeMember.getMemberId() == memberId

#testing setter for firstName attribute
def canSetFirstName(fName):
    myFakeMember = fightClubMember.FightClubMember("fake", "fake", 0, "fake", "fm89076")
    myFakeMember.setFirstName(fName)
    return "set first name is correct: ", myFakeMember.getFirstName() == fName

#testing setter for lastName attribute
def canSetLastName(lName):
    myFakeMember = fightClubMember.FightClubMember("fake", "fake", 0, "fake", "fm89076")
    myFakeMember.setLastName(lName)
    return "set last name is correct: ", myFakeMember.getLastName() == lName

#testing setter for number of sessions attended attribute
def canSetNumberSessions(numSessions):
    myFakeMember = fightClubMember.FightClubMember("fake", "fake", 0, "fake", "fm89076")
    myFakeMember.setNumberOfSessionsAttended(numSessions)
    return "set number of sessions is correct: ", myFakeMember.getNumberOfSessionsAttended() == numSessions

#testing setter for isBanned attribute
def canSetIsBanned(isBanned):
    myFakeMember = fightClubMember.FightClubMember("fake", "fake", 0, "fake", "fm89076")
    myFakeMember.setIsBanned(isBanned)
    return "set is banned is correct: ", myFakeMember.getIsBanned() == isBanned