'''
Melissa Brown

CSC 330 Language Design and Implementation

Session 5

Create a DSL
'''

class FightClub:
  
  # creates a new Fight Club, with max group members and an empty sessions list
  def __init__(self, maxGroupMembers):
    self.maxGroupMembers = maxGroupMembers
    self.sessionsList = []

  # lines 18 - 26 are getters / setters
  def getMaxGroupMembers(self):
    return self.maxGroupMembers

  def setMaxGroupMembers(self, newMaxGroupMembers):
    self.maxGroupMembers = newMaxGroupMembers

  def getSessionsList(self):
    return self.sessionsList

  # adds a session to the session list if it is not already in the list
  def addSession(self, sessionToAdd):
    wasAdded = True

    # assumed that each fight club only uses one spot, so if a session with the same date / time already 
    # exists, then it cannot be added to its session list
    checkSession = next((x for x in self.sessionsList if (x.getDate() == sessionToAdd.getDate()) & (x.getTime() == sessionToAdd.getTime())), None)
    if not checkSession is None:
        print("Session already exists and cannot be added")
        wasAdded = False
    else:
        self.sessionsList.append(sessionToAdd)
        print("Session was added")
        wasAdded = True
    return wasAdded

  # if a session exists in the fight club, it can be removed. otherwise if it doesn't exist, it cannot be
  def removeSession(self, sessionToRemove):
    wasRemoved = True

    # checks to see if a session with the same date and time exists
    sessionToRemove = next((x for x in self.sessionsList if (x.getDate() == sessionToRemove.getDate()) & (x.getTime() == sessionToRemove.getTime())), None)
    if sessionToRemove is None:
        print("Session does not exist and cannot be removed")
        wasRemoved = False
    else:
        self.sessionsList.remove(sessionToRemove)
        print("Session was removed")
        wasRemoved = True
    return wasRemoved
  
  # checks if two fight clubs are equal to each other, meaning they have the same max members
  # and the same session list
  def __eq__(self, other):
        otherList = other.getSessionsList()
        isSameSessionsList = True

        # if the session lists in each fight club are not the same length, the fight clubs cannot be the same
        if len(self.sessionsList) != len(otherList):
           print("not same length")
           isSameSessionsList = False
        else:
           for session in self.sessionsList:
                checkForSession = next((x for x in otherList if (x.getDate() == session.getDate()) & (x.getTime() == session.getTime())), None)
                print("check for sessions in equals fight club: ", checkForSession)
                if checkForSession is None:
                    print("none")
                    isSameSessionsList = False
                    break
        print("right before return")
        return (self.maxGroupMembers == other.getMaxGroupMembers()) & isSameSessionsList
  
