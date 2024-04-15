'''
Melissa Brown

CSC 330 Language Design and Implementation

Session 5

Create a DSL

Creates FightClubSession class which defines a session that fight club members can attend
'''

import fightClubMember
import datetime
from datetime import time

class FightClubSession:
  
  # constructor, each session has a date, a time, a length of session, and max attendees.
  # empty attendee list is auto created with each session created
  def __init__(self, date, time, lengthInMinutes, maxAttendees):
    self.date = date
    self.time = time
    self.lengthInMinutes = lengthInMinutes
    self.maxAttendees = maxAttendees
    self.attendeeList = []

# Lines 28 - 54 are getter / setter methods
  def getDate(self):
    #date is formatted to not included time when it is retrieved
    return self.date.strftime("%x")

  def setDate(self, newDate):
    self.date = newDate

  def getTime(self):
    return self.time

  def setTime(self, newTime):
    self.time = newTime

  def getLength(self):
    return self.lengthInMinutes

  def setLength(self, newLength):
    self.lengthInMinutes = newLength

  def getMaxAttendees(self):
    return self.maxAttendees

  def setMaxAttendees(self, newMaxAttendees):
    self.maxAttendees = newMaxAttendees

  def getAttendeeList(self):
    return self.attendeeList

  # adds to list. fight club member can be added if they are not in the list, the session is not full, and 
  # they are not banned
  def addToAttendeeList(self, attendeeToAdd):
    wasAdded = True
    checkForAttendee = ""
    print(attendeeToAdd.getIsBanned())

    # attendee will already be in the list or not exist, therefore assigned the value of None
    checkForAttendee = next((x for x in self.attendeeList if x.getMemberId() == attendeeToAdd.getMemberId()), None)
    if not checkForAttendee is None:
        # attendee is in list
        wasAdded = False
    elif attendeeToAdd.getIsBanned() == True:
        # attendee is banned
        wasAdded = False
    elif len(self.attendeeList) == self.maxAttendees:
        # session is full
        wasAdded = False
    else:
        # member was successfully added
        self.attendeeList.append(attendeeToAdd)
    return wasAdded

  # attendee can be removed if they are in the list, otherwise they cannot be removed
  def removeFromAttenndeeList(self, attendeeToRemove):
    wasRemoved = True

    # attendee will already be in the list or not exist, therefore assigned the value of None
    checkForAttendee = next((x for x in self.attendeeList if x.getMemberId() == attendeeToRemove.getMemberId()), None)
    if checkForAttendee == None:
        # member is not in list, cannot be removed
        wasRemoved = False
    else:
        # member was removed
        self.attendeeList.remove(attendeeToRemove)
    return wasRemoved

  # prints a session with its date and time
  def __str__(self):
    return "%s %s"%(self.getDate(), self.getTime())

  # if a session has the same date, time, max attendees, attendee list, and length of session, it is the same
  def __eq__(self, other):

    # attendee list from other session
    otherAttendeeList = other.getAttendeeList()
    listIsSame = True

    # if length of attendee lists are not the same, sessions are not equal
    if len(otherAttendeeList) != len(self.attendeeList):
        print("is false")
        listIsSame = False
    else:
        for session in self.attendeeList:
            # checks of attendee exists in both lists
            checkForAttendee = next((x for x in otherAttendeeList if x.getMemberId() == session.getMemberId()), None)
            # if they do not then sessuibs are not the same, and the for loop can break
            if checkForAttendee is None:
               listIsSame = False
               break
    return ((self.getDate() == other.getDate()) & (self.getTime() == other.getTime())\
            & (self.getLength() == other.getLength()) & (self.getMaxAttendees() == other.getMaxAttendees()))\
            & listIsSame
        
