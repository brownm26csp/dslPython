'''
Melissa Brown

CSC 330 Language Design and Implementation

Session 5

Create a DSL

Creates functions which test the fightClubMember class. This one could also be named better and I meant to 
name it "testMemberModule.py" but then I already had it named and again, re-naming it broke everything
'''

import fightClubSession
import fightClubMember
import datetime
from datetime import time

fakeDate = datetime.datetime(2024,1,1)

# tests if user can create a session where the get methods return everything which was put in the parameters
def canCreateSession(hr, min, sec, attendeeCap, year, month, day, lengthMinutes):
    myDate = datetime.datetime(int(year),int(month),int(day))
    myTime = time(int(hr),int(min),int(sec))
    myNewSession = fightClubSession.FightClubSession(myDate, myTime, lengthMinutes, attendeeCap)
    return "Session is the same: ", (myNewSession.getDate() == myDate.strftime("%x")) & (myNewSession.getTime() == myTime)\
                                    & (myNewSession.getLength() == lengthMinutes)\
                                    & (myNewSession.getMaxAttendees() == attendeeCap)\
                                    & (myNewSession.getAttendeeList() == [])

# tests that date put into constructor is returned properly
def canGetDate(year, month, day):
    myDate = datetime.datetime(int(year),int(month),int(day))
    myFakeSession = fightClubSession.FightClubSession(myDate, time(1,1,1), 0, 0)
    return "Date is correct: ", myFakeSession.getDate() == myDate.strftime("%x")

# tests that time put into constructor is returned properly
def canGetTime(hr, min, sec):
    myTime = time(int(hr), int(min), int(sec))
    myFakeSession = fightClubSession.FightClubSession(fakeDate, myTime, 0, 0)
    return "Time is correct: ", myFakeSession.getTime() == myTime

# tests that session length in minutes put into constructor is returned properly
def canGetLength(lengthInMinutes):
    myFakeSession = fightClubSession.FightClubSession(fakeDate, time(1,1,1), lengthInMinutes, 0)
    return "Length in minutes is correct: ", myFakeSession.getLength() == lengthInMinutes

# tests that max attendees put into constructor is returned properly
def canGetMaxAttendees(attendeeCap):
    myFakeSession = fightClubSession.FightClubSession(fakeDate, time(1,1,1), 0, attendeeCap)
    return "Max attendees is correct: ", myFakeSession.getMaxAttendees() == attendeeCap

# tests that attendee list is returned properly
def canGetAttendeeList(fake):
    myFakeSession = fightClubSession.FightClubSession(fakeDate, time(1,1,1), 0, 30)

    # creates two members
    fakeMember1 = fightClubMember.FightClubMember("Melissa","Brown",30,False,"mb12345")
    fakeMember2 = fightClubMember.FightClubMember("Shannon","Retuer",20,False,"sr89076")

    # list to compare to stored list
    myFakeList = []
    myFakeList.append(fakeMember1)
    myFakeList.append(fakeMember2)

    # members are added to test session
    myFakeSession.addToAttendeeList(fakeMember1)
    myFakeSession.addToAttendeeList(fakeMember2)

    # list is set to attendee list from test session
    myRealList = myFakeSession.getAttendeeList()

    # uses __eq__ method of fight club session class to ensure both lists are the same at both indices
    return "Attendee list is correct: ", (myRealList[0] == myFakeList[0])\
                                         & (myRealList[1] == myFakeList[1])

# tests that date can be set
def canSetDate(year, month, day):
    myDate = datetime.datetime(int(year),int(month),int(day))
    myFakeSession = fightClubSession.FightClubSession(fakeDate, time(1,1,1), 0, 0)
    myFakeSession.setDate(myDate)
    return "Can set date: ", myFakeSession.getDate() == myDate.strftime("%x")

# tests that time can be set
def canSetTime(hr, min, sec):
    myTime = time(int(hr), int(min), int(sec))
    myFakeSession = fightClubSession.FightClubSession(fakeDate, time(1,1,1), 0, 0)
    myFakeSession.setTime(myTime)
    return "Can set time: ", myFakeSession.getTime() == myTime

# tests that length of session can be set
def canSetLength(newLength):
    myFakeSession = fightClubSession.FightClubSession(fakeDate, time(1,1,1), 0, 0)
    myFakeSession.setLength(newLength)
    return "Can set length: ", myFakeSession.getLength() == newLength

# tests that max attendees can be set
def canSetMaxAttendees(newMax):
    myFakeSession = fightClubSession.FightClubSession(fakeDate, time(1,1,1), 0, 0)
    myFakeSession.setMaxAttendees(newMax)
    return "Can set max attendees: ", myFakeSession.getMaxAttendees() == newMax

# tests that fight club member can be added to list if they are not banned, session isn't full,
# and they aren't already in the list
def canAddToList(fName, lName, fightsAttended, isBanned, memberId):
    myFakeMember = fightClubMember.FightClubMember(fName, lName, fightsAttended, isBanned, memberId)
    myFakeSession = fightClubSession.FightClubSession(fakeDate, time(1,1,1), 120, 30)
    result = myFakeSession.addToAttendeeList(myFakeMember)
    return "can add to list: ", result

# tests that fight club member cannot be added if they are already in the session
def cannotAddAlreadyJoined(fName, lName, fightsAttended, isBanned, memberId):
    myFakeMember = fightClubMember.FightClubMember(fName, lName, fightsAttended, isBanned, memberId)
    myFakeSession = fightClubSession.FightClubSession(fakeDate, time(1,1,1), 120, 30)
    myFakeSession.addToAttendeeList(myFakeMember)
    return "can add to list if already joined", myFakeSession.addToAttendeeList(myFakeMember)

# tests that member cannot be added if they are banned
def cannotAddMemberBanned(fName, lName, fightsAttended, isBanned, memberId):
    if isBanned == "True":
        isBanned = True
    else:
        isBanned = False
    myFakeMember = fightClubMember.FightClubMember(fName, lName, fightsAttended, isBanned, memberId)
    myFakeSession = fightClubSession.FightClubSession(fakeDate, time(1,1,1), 120, 30)
    return "can add to list if banned", myFakeSession.addToAttendeeList(myFakeMember)

# tests that member cannot be added if session is full
def cannotAddSessionFull(fName, lName, fightsAttended, isBanned, memberId):
    myFakeMember = fightClubMember.FightClubMember(fName, lName, fightsAttended, isBanned, memberId)
    myFakeSession = fightClubSession.FightClubSession(fakeDate, time(1,1,1), 120, 0)
    return "can add to list if session full: ", myFakeSession.addToAttendeeList(myFakeMember)

# tests member can be removed if in list
def canRemoveIfInList(fName, lName, fightsAttended, isBanned, memberId):
    myFakeMember = fightClubMember.FightClubMember(fName, lName, fightsAttended, isBanned, memberId)
    myFakeSession = fightClubSession.FightClubSession(fakeDate, time(1,1,1), 120, 100)
    myFakeSession.addToAttendeeList(myFakeMember)
    return "can remove from list if in session already:", myFakeSession.removeFromAttenndeeList(myFakeMember)

# tests member cannot be removed if not in list
def cannotRemoveIfNotInList(fName, lName, fightsAttended, isBanned, memberId):
    myFakeMember = fightClubMember.FightClubMember(fName, lName, fightsAttended, isBanned, memberId)
    myFakeSession = fightClubSession.FightClubSession(fakeDate, time(1,1,1), 120, 0)
    return "can remove from list if in session already:", myFakeSession.removeFromAttenndeeList(myFakeMember)