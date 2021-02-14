## Author:  Danessa Yip
# Date:    01/17/2021
# Purpose: CS119-PJ11 Sudoku Game Check - to check four Sudoku game boards.

#Pre-set Sudoku Games
# Nice to show row index 0 to 8 and column index 0 to 8 for readability of your code 
S1 = [                                            # Game 1
#  column index:         0 1 2 3 4 5 6 7 8     
[1,2,3,4,5,6,7,8,9],    # row index 0     ||  User’s row  1
[2,3,4,5,6,7,8,9,1],    #                  1                            2
[3,4,5,6,7,8,9,1,2],    #                  2                            3
[4,5,6,7,8,9,1,2,3],    #                  3                            4
[5,6,7,8,9,1,2,3,4],     #                 4                            5
[6,7,8,9,1,2,3,4,5],     #                 5                            6
[7,8,9,1,2,3,4,5,6],     #                 6                            7
[8,9,1,2,3,4,5,6,7],     #                 7                            8
[9,1,2,3,4,5,6,7,8]   ]  #                 8                            9
S2 = [                                            # Game 1
#  column index:         0 1 2 3 4 5 6 7 8     
[1,2,3,4,5,6,7,8,9],    # row index 0     ||  User’s row  1
[4,5,6,7,8,9,1,2,3],    #                  1                            2
[7,8,9,1,2,3,4,5,6],    #                  2                            3
[2,3,4,5,6,7,8,9,1],    #                  3                            4
[5,6,7,8,9,1,2,3,4],     #                 4                            5
[8,9,1,2,3,4,5,6,7],     #                 5                            6
[3,4,5,6,7,8,9,1,2],     #                 6                            7
[6,7,8,9,1,2,3,4,5],     #                 7                            8
[9,1,2,3,4,5,6,7,8]   ]  #                 8                            9

S2 = [                                            # Game 1
#  column index:         0 1 2 3 4 5 6 7 8     
[1,2,3,4,5,6,7,8,9],    # row index 0     ||  User’s row  1
[4,5,6,7,8,9,1,2,3],    #                  1                            2
[7,8,9,1,2,3,4,5,6],    #                  2                            3
[2,3,4,5,6,7,8,9,1],    #                  3                            4
[5,6,7,8,9,1,2,3,4],     #                 4                            5
[8,9,1,2,3,4,5,6,7],     #                 5                            6
[3,4,5,6,7,8,9,1,2],     #                 6                            7
[6,7,8,9,1,2,3,4,5],     #                 7                            8
[9,1,2,3,4,5,6,7,8]   ]  #                 8                            9

S3 = [                                            # Game 1
#  column index:         0 1 2 3 4 5 6 7 8     
[1,2,3,4,5,6,7,8,2],    # row index 0     ||  User’s row  1
[4,5,6,7,8,9,1,2,3],    #                  1                            2
[7,8,9,1,2,3,4,5,6],    #                  2                            3
[2,3,4,5,6,7,8,9,1],    #                  3                            4
[5,6,7,8,9,1,2,3,4],     #                 4                            5
[8,9,1,2,3,4,5,6,7],     #                 5                            6
[3,4,5,6,7,8,9,1,2],     #                 6                            7
[6,7,8,9,1,2,3,4,5],     #                 7                            8
[9,1,2,3,4,5,6,7,8]   ]  #                 8                            9

S4 = [                                            # Game 1
#  column index:         0 1 2 3 4 5 6 7 8     
[1,2,3,4,5,6,7,8,9],    # row index 0     ||  User’s row  1
[4,5,6,7,8,9,1,2,3],    #                  1                            2
[7,8,9,1,2,3,4,5,6],    #                  2                            3
[2,3,4,5,6,7,8,9,1],    #                  3                            4
[5,6,7,8,9,1,2,3,4],     #                 4                            5
[8,9,1,2,3,4,5,6,7],     #                 5                            6
[3,4,5,6,7,8,9,1,2],     #                 6                            7
[6,7,8,9,1,8,3,4,5],     #                 7                            8
[9,1,2,3,4,5,6,7,8]   ]  #                 8                            9
#====================RowOK Function==========================================
def RowOK(S, r):  # check Row r in S board is OK or not
	goodlist = [1,2,3,4,5,6,7,8,9]   # a perfect list of 1 thru 9 sorted order
	slist = S[r]     # get row r, which can be 0, 1, …, or 8
	clist = [ ]        # We must make a real copy of the original source list to avoid changing it here.
	for element in slist:
		clist.append(element)   # make a real copy to avoid side effect to the original 9x9 array
	clist.sort( )    # sort the list before comparing with goodlist
	return (clist == goodlist)    # true means OK since they are equal
	# end of RowOK( )
#====================ColumnOK Function==========================================
def ColumnOK(S, c):  # check Column c in S board is OK or not
	goodlist = [1,2,3,4,5,6,7,8,9]   # a perfect list of 1 thru 9 sorted order
	slist = []
	for i in range(0,9):
		slist.append(S[i][c])     # get column c, which can be 0, 1, …, or 8
	clist = [ ]        # We must make a real copy of the original source list to avoid changing it here.
	for element in slist:
		clist.append(element)   # make a real copy to avoid side effect to the original 9x9 array
	clist.sort( )    # sort the list before comparing with goodlist
	return (clist == goodlist)    # true means OK since they are equal
	# end of ColumnOK( )
	return (clist == goodlist)    # true means OK since they are equal
	# end of RowOK( )
#====================SquareOK Function==========================================
def SquareOK(S, q):  # check Square q in S board is OK or not
	goodlist = [1,2,3,4,5,6,7,8,9]   # a perfect list of 1 thru 9 sorted order
	slist = []
	if (q >= 0 and q <=2):
		for i in range(0,3):
			for j in range(3*(q),3*(q)+3):
				slist.append(S[i][j])
	elif (q >= 3 and q <=5):
		for i in range(3,6):
			for j in range(3*((q)%3),3*((q)%3)+3):
				slist.append(S[i][j])
	elif (q >= 6 and q <=8):
		for i in range(6,9):
			for j in range(3*((q)%3),3*((q)%3)+3):
				slist.append(S[i][j])     # get square 1, which can be 0, 1, …, or 8
	clist = [ ]        # We must make a real copy of the original source list to avoid changing it here.
	for element in slist:
		clist.append(element)   # make a real copy to avoid side effect to the original 9x9 array
	clist.sort( )    # sort the list before comparing with goodlist
	return (clist == goodlist)    # true means OK since they are equal
	# end of SquareOK( )
#=================== Check Game =============================================
def checkGame(S):   # check game board S for 9 rows, 9 columns, 9 squares
	countBad = 0   # count how many problems being detected 
	for r in range(9):  # 9 rows check with r = 0 to 8
		if (not RowOK(S, r) ):     # r = 0 to 8 from computer’s view
			print("Row ", r + 1 , " has a problem.")               # Row 1 to 9 from user’s view
			countBad += 1   # increment countBad by 1
	for c in range(9):  #  9 columns check: 0 to 8, actually they mean column 1 to 9 for user.
		if (not ColumnOK(S, c) ):     # c = 0 to 8 from computer’s view
			print("Column ", c + 1 , " has a problem.")               # Row 1 to 9 from user’s view
			countBad += 1   # increment countBad by 1
	for q in range(9):  #  9 squares check: 0 to 8, actually they mean square 1 to 9 for user.
		if (not SquareOK(S, q) ):     # r = 0 to 8 from computer’s view
			print("Square ", q + 1 , " has a problem.")               # Row 1 to 9 from user’s view
			countBad += 1   # increment countBad by 1
	if countBad == 0:  # perfect game since nothing is bad 
		print("Congratulations! You won the game.")
#=================== Show Game ==============================================
def showGame(S):
	for i in range(0,9):
		print(S[i])
#=================== Main Program ===========================================
n = 1  # line number for each separation line for readability
print('Welcome to play the Sudoku Game Check of "Danessa Yip"!')
print(n,"=============================================================");n=n+1;
print("Your game 1 is as follows: " )
showGame(S1)   # to print 9x9 game board
print( )
print("Your game 1: ")  # show the check result
checkGame(S1)  # to check 9 rows/columns/squares
print( )
print(n,"=============================================================");n=n+1;
print("Your game 2 is as follows: " )
showGame(S2)   # to print 9x9 game board
print( )
print("Your game 2: ")  # show the check result
checkGame(S2)  # to check 9 rows/columns/squares
print( )
print(n,"=============================================================");n=n+1;
print("Your game 3 is as follows: " )
showGame(S3)   # to print 9x9 game board
print( )
print("Your game 3: ")  # show the check result
checkGame(S3)  # to check 9 rows/columns/squares
print( )
print(n,"=============================================================");n=n+1;
print("Your game 4 is as follows: " )
showGame(S4)   # to print 9x9 game board
print( )
print("Your game 4: ")  # show the check result
checkGame(S4)  # to check 9 rows/columns/squares
print( )
print(n,"=============================================================");n=n+1;
print ('Thank you for playing this Sudoku Game Check of "Danessa Yip"!')
print(n,"=============================================================");n=n+1;