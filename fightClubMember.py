'''
Melissa Brown

CSC 330 Language Design and Implementation

Session 5

Create a DSL
'''

class FightClubMember:
  
  #constructor, fight club member has a first name, last name, number of sessions they have 
  #attended so far, if they are banned or not, and a member Id
  def __init__(self, firstName, lastName, numberOfSessionsAttended, isBanned, memberId):
    self.firstName = firstName
    self.lastName = lastName
    self.numberOfSessionsAttended = numberOfSessionsAttended
    self.isBanned = isBanned
    self.memberId = memberId

# Lines 22 - 48 include getters and setters for all attributes
  def getFirstName(self):
    return self.firstName

  def setFirstName(self, newFirstName):
    self.firstName = newFirstName

  def getLastName(self):
    return self.lastName

  def setLastName(self, newLastName):
    self.lastName = newLastName

  def getMemberId(self):
    return self.memberId

  def getNumberOfSessionsAttended(self):
    return self.numberOfSessionsAttended

  def setNumberOfSessionsAttended(self, newSesionNumber):
    self.numberOfSessionsAttended = newSesionNumber

  def getIsBanned(self):
    return self.isBanned

  def setIsBanned(self, newBannedStatus):
    self.isBanned = newBannedStatus
