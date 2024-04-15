'''
Melissa Brown

CSC 330 Language Design and Implementation

Session 5

Create a DSL

Tests methods from fightClub class
'''

import fightClub
import fightClubSession
import datetime
from datetime import time

fakeDate = datetime.datetime(2024,1,1)

# tests that a fight club created is set correctly with values passed into parameters
def canCreateFightClub(maxMembers):
    fakeFightClub = fightClub.FightClub(maxMembers)
    return "Fight club was created correctly: ", fakeFightClub.getMaxGroupMembers() == maxMembers

# tests that max members put into constructor is returned correctly
def canGetMaxGroupMembers(maxMembers):
    return "Correctly gets max group members: ", canCreateFightClub(maxMembers)

# tests that user can set max group members correctly
def canSetMaxGroupMembers(maxMembers):
    fakeFightClub = fightClub.FightClub(300)
    fakeFightClub.setMaxGroupMembers(maxMembers)
    return "Correctly sets max group members: ", fakeFightClub.getMaxGroupMembers() == maxMembers

# tests that session list is returned correctly
def canGetSessionList():
    #creates test fight club
    fakeFightClub = fightClub.FightClub(20)

    # creates two test sessions
    myFakeSession1 = fightClubSession.FightClubSession(fakeDate, time(1,1,1), 120, 30)
    myFakeSession2 = fightClubSession.FightClubSession(fakeDate, time(2,2,2), 135, 35)

    # creates a comparison list with two test sessions
    myFakeList = [myFakeSession1, myFakeSession2]

    # add test sessions to test fight club
    fakeFightClub.addSession(myFakeSession1)
    fakeFightClub.addSession(myFakeSession2)

    myRealList = fakeFightClub.getSessionsList()
    return "Session list is returned correctly: ", myFakeList[0].__eq__(myRealList[0]) & myFakeList[1].__eq__(myRealList[1])

# test that a session can be added to a fight club as long as it is not already in the list
def canAddSessionIfNotInList():
    fakeFightClub = fightClub.FightClub(20)
    myFakeSession1 = fightClubSession.FightClubSession(fakeDate, time(1,1,1), 120, 30)
    return "Can add session to list if not in list: ", fakeFightClub.addSession(myFakeSession1)

# tests that a session cannot be added to a fight club if it is already in the list
def cannotAddSessionIfInList():
    fakeFightClub = fightClub.FightClub(20)
    myFakeSession1 = fightClubSession.FightClubSession(fakeDate, time(1,1,1), 120, 30)
    fakeFightClub.addSession(myFakeSession1)
    return "Can add session to list if already in list: ", fakeFightClub.addSession(myFakeSession1)

# tests that a session can be removed if it is already in the list
def canRemoveSessionIfInList():
    fakeFightClub = fightClub.FightClub(20)
    myFakeSession1 = fightClubSession.FightClubSession(fakeDate, time(1,1,1), 120, 30)

    # add to ensure it is in the fight club session list
    fakeFightClub.addSession(myFakeSession1)
    return "Can remove session from list if already in list: ", fakeFightClub.removeSession(myFakeSession1)

# test that a session cannot be removed if it is not already in the list
def cannotRemoveSessionIfNotInList():
    fakeFightClub = fightClub.FightClub(20)
    myFakeSession1 = fightClubSession.FightClubSession(fakeDate, time(1,1,1), 120, 30)
    return "Can remove session from list if not already in list: ", fakeFightClub.removeSession(myFakeSession1)
    