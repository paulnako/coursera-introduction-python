# -*- coding:utf-8 -*-

# implementation of card game - Memory

import simplegui
import random

numbers = range(0, 8) + range(0, 8)
random.shuffle(numbers)

exposed = [ False ] * len(numbers)

# helper function to initialize globals
def new_game():
    pass  

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    exposed[ pos[0] // 50 ] = True
    print pos[0] // 50

    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for i in range(0, 16):
        canvas.draw_text(str(numbers[i]),( i * 50 + 5, 80), 80,  "black")
        canvas.draw_polygon( 
                            ( (0 + i * 50, 0), ( 0 + i * 50, 100 ), ( 50 + i * 50, 100 ), ( 50 + i * 50, 0 )) ,
                            1, 
                            "black", 
                            "green"
                            )


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
