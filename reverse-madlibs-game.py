#UDACITY COURSE: INTRO TO PROGRAMMING
#Author: Constantin G. Bosse
#EMAIL: cgbosse@gmail.com
#-------------------------
#STAGE 2: Project - Build a reverse Mad Libs Game
# Summary of task:
# Create a game which:
# 	Has 3 levels of difficulty (easy, medium, hard).
# 	The game uses preset strings filled with several blancs.
# 	There must be at least 4 different types of blancs per level.
# 	The blancs are numbered within the text which is displayed in the beginning.
# 	It prompts the user to input the right answer to each of the blancs.
# 		If it is correct it proceeds and shows the text with the filled blanc
# 		If it is not it prompts the user again for new input
#

# Variable: Defining the list for the levels of difficulty:
level_list = [[1,"Easy","Basic knowledge"], [2,"Medium","Average knowledge"], [3,"Difficult","Advanced knoledge"]]


# Variable: Setting up the different texts per level as variables for easy change in the future.
# Texts taken from "Python for dummies" by John Paul Mueller
texts_w_gaps = ["Creating ___1___s requires that you have another ___1___, unless you really want to get low level and write ___1___s in machine ___4___ - a decidedly difficult experience that even true ___2___s avoid if at all possible. If you want to write an ___1___ using the ___3___ programming language, you need the ___1___s required to do so. These ___1___s help you work with ___3___ by creating ___3___ ___4___, providing help 2as you need it, and letting you run the ___4___ you write. This chapter helps you obtain a copy of the ___3___ ___1___, install it on your hard drive, locate the installed ___1___s so that you can use them, and test your installation so that you can see how it works." , "Python is a computer ___1___, not a human ___1___. As a result, you won't ___2___ it fluently at first. If you think about it for a moment, it makes sense that you won't ___2___ Python fluently (and as with most human ___1___s, you won't know every ___3___ even after you do become fluent). Having to discover Python ___3___s a little at a time is the same thing that happens when you learn to ___2___ another human ___1___. If you normally ___2___ English and try to say something in German, you find that you must have some sort of ___4___ to help you along. Otherwise, anything you say is gibberish and people will look at you quite oddly. Even if you manage to say something that makes sense, it may not be what you want. You might go to a restaurant and order hot hubcaps for dinner when what you really wanted was a steak." , "___1___ uses specialized variables to store ___2___ to make things easy for the programmer and to ensure that the ___2___ remains safe. However, ___3___s don't actually know about ___2___ types. All that the ___3___ knows about are 0s and 1s, which is the absence or presence of a voltage. At a higher level, ___3___s do work with ___4___s, but that's the extent of what ___3___s do. ___4___s, letters, dates, times, and any other kind of ___2___  you can think about all come down to 0s and 1s in the ___3___ system. For example, the letter A is actually stored as 01000001 or the ___4___ 65. The ___3___ has no concept of the letter A or of a date such as 8/31/2014."]

# Variable: Setting up the words for each level.
words4gaps = [["application" , "programmer" , "Python" ,"code" ] , ["language" , "speak" , "command" ,"guide" ] , ["Python" , "information" , "computer" ,"number" ]]

# Function purpose: Intro to game, I have set it up this way so that I can easily change the text and structure.
# Input: None
# Output: Printed intro to the game explaining the game.
def intro():
	welcome = "Welcome to the reverse MAD LIBS GAME"
	separator = ("-")*len(welcome)
	intro = """There are different levels of difficulty which can be selected by the user. Each level shows a text filled with gaps that test the users knowledge and memory."""
	print welcome
	print separator
	print intro
	return

# Function purpose: Lists the index of the available levels and their descriptions
# Input: None
# Output: prints the list of levels with their description
def level_list_display():
	for elements in level_list:
		print
		print " " * 4 , elements[0],"--",elements[1],"--",elements[2]
	return

# Function purpose: To prompt the user to select the level of difficulty he wants to play
# I have put in a maximum of three attempts to enter a valid level between.
# Input: user input at prompts
# Output: the selected level in integer format for use in another function

def level_select():
	level = raw_input("Please select your level of choice between 1 and 3: ")
	level = int(level)
	wrong_input_attempts = 3
	if level not in range(1,4):
		print "You have not selected a level between 1 and 3."
		while level not in range (1,4):
			level = raw_input("Please select a level between 1 and 3: ")
			level = int(level)
			if level in range(1,4):
				break
			else:
				wrong_input_attempts = wrong_input_attempts -1
				print "Attempts remaining: " + str(wrong_input_attempts)
				if wrong_input_attempts == 0:
					break
	return level

# Function purpose: Just used for uniform formatting to avoid duplication.
# Input: None
# Output: Text
def spacing():
	print
	print "-+-"*20
	print
	return

# Function purpose: Creating a message for the completion of a word.
# Input: None
# Output: Text
def correct_word_message():
	print "**"*20
	print "  " * 5 + "Very Good!!!"
	print "**"*20
	return

# Function purpose: Creating a message for the completion of the level, so that it can be changed in the future with ease.
# Input: None
# Output: Text
def completed_game_message():
	print "**"*20
	print "  " * 5 + "Great!!!"
	print "  " * 5 + "You completed this level!!!"
	print "**"*20
	return

# Function purpose: The runs the game core, using the correct text according to the level and asking
# for user input for the word gaps for each text depending on the level.
# I have set up the gap2replace in such a way that it could work for an unlimited list of words contained withing th word_list.
# Input: the level to start the game and further inputs for each choice of word from the user.
# Output: the texts with gaps and the requests for user input as well as messages when errors are committed
def enter_word(level):
	level = level - 1
	word_list = words4gaps[level]
	text2use = texts_w_gaps[level]
	print text2use
	print
	for word in word_list:
		correct_word = word
		gap2replace = "___"+str(word_list.index(word) + 1)+"___"
		word_choice = raw_input("Please enter your choice for " + gap2replace + ":")
		print
		while word_choice != correct_word:
			print "=="*30
			word_choice = raw_input("Please try again and enter another choice for" + gap2replace + ":")
		text2use = text2use.replace(gap2replace, word_choice)
		correct_word_message()
		print text2use
		print
	return

# Function purpose: putting it all together to form the reverse madlibs game.
def reverse_madlib():
	intro()
	spacing()
	level_list_display()
	spacing()
	level = level_select()
	spacing()
	enter_word(level)
	completed_game_message()
	return

reverse_madlib()
