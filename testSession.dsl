testMemberSession canCreateSession 13 30 45 30 2024 6 3 120
testMemberSession canGetDate 2024 7 10
testMemberSession canGetTime 21 30 00
testMemberSession canGetLength 250
testMemberSession canGetMaxAttendees 50
testMemberSession canGetAttendeeList list
testMemberSession canSetDate 2024 8 12
testMemberSession canSetTime 17 18 22
testMemberSession canSetLength 45
testMemberSession canSetMaxAttendees 150
testMemberSession canAddToList tim brown 30 False tb56789
testMemberSession cannotAddAlreadyJoined tim brown 30 False tb56789
testMemberSession cannotAddMemberBanned tim brown 30 True tb56789
testMemberSession cannotAddSessionFull tim brown 30 False tb56789
testMemberSession canRemoveIfInList tim brown 30 False tb56789
testMemberSession cannotRemoveIfNotInList tim brown 30 False tb56789