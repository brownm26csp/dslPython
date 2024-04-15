'''
Melissa Brown

CSC 330 Language Design and Implementation

Session 5

Create a DSL
'''

import fightClubMember
import fightClubSession
import fightClub
import datetime
from datetime import time

class Main:
    # creates two fight club members
    fightClubMember1 = fightClubMember.FightClubMember("Melissa","Brown",50,False,"mb12345")
    fightClubMember2 = fightClubMember.FightClubMember("Shannon","Reuter",25,True,"sr12346")

    # creates two different dates and times
    session1Date = datetime.datetime(2024,5,1)
    session2Date = datetime.datetime(2024,6,12)
    session2Time = time(17,45,00)
    session1Time = time(16,30,00)

    # creates three sessions, session3 is purposefully the same as session 1
    session1 = fightClubSession.FightClubSession(session1Date, session1Time,120,5)
    session2 = fightClubSession.FightClubSession(session2Date, session2Time,40,7)
    session3 = fightClubSession.FightClubSession(session1Date, session1Time,120,5)

    #creates an empty session list and adds session1 to the list
    sessionsList = []
    sessionsList.append(session1)

    # adds members to to different sessions, session 3 is purposefully again the same as session1
    session1.addToAttendeeList(fightClubMember1)
    session1.addToAttendeeList(fightClubMember2)

    session3.addToAttendeeList(fightClubMember1)
    session3.addToAttendeeList(fightClubMember2)
    session2.addToAttendeeList(fightClubMember1)

    # session 1 should be equal to session 3
    print("session 1 equal session 2", session1.__eq__(session2))
    print("session 2 equal session 3", session2.__eq__(session3))
    print("session 1 equals session 3", session1.__eq__(session3))
    
    # creates three different fight clubs
    fightClub1 = fightClub.FightClub(50)
    fightClub2 = fightClub.FightClub(40)
    fightClub3 = fightClub.FightClub(50)

    # adds the same session 2 all three fight clubs, fightClub2 is different as it has fewer max members
    fightClub1.addSession(session1)
    fightClub2.addSession(session1)
    fightClub3.addSession(session1)

    # false
    print(fightClub1.__eq__(fightClub2))

    #true
    print(fightClub1.__eq__(fightClub3))
