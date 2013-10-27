# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

# -*- coding:utf-8 -*-
import random
import simplegui


# initialize global variables used in your code
com_choice = 0
rest = 7
upper_bound = 100
max_count = 7

# helper function to start and restart the game
def new_game():
    global com_choice, rest
    com_choice = random.randrange(0, upper_bound)
    rest = max_count
    print "New game. Range is 0 to %d" % upper_bound
    print "Number of remaining guess is %d" % rest 
    print ""

# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global upper_bound, max_count
    max_count = 7
    upper_bound = 100
    new_game()

def range1000():
    # button that changes range to range [0,1000) and restarts
    global upper_bound, max_count
    max_count = 10
    upper_bound = 1000
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    global rest 
    guess_num = int(guess)
    print "Guess was %d" % guess_num 
    rest -= 1
    print "Number of remaining guess is %d" % rest 
    if com_choice == guess_num:
        print "Correct!\n"
        new_game()
        return
    elif com_choice > guess_num:
        print "Lower!"
    elif com_choice < guess_num:
        print "Higher!"

    if rest == 0:
        print "game is reset. guess a new number.\n"
        new_game()
    print ""
        
# create frame
frame = simplegui.create_frame("guess a number", 300, 300)

# register event handlers for control elements
frame.add_button("Range is (0, 100]", range100, 200 )
frame.add_button("Range is (0, 1000]", range1000, 200 )
frame.add_input("Enter a guess", input_guess, 200 )


# call new_game and start frame
frame.start()
new_game()


# always remember to check your completed program against the grading rubric
