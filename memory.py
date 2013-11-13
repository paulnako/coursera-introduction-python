# -*- coding:utf-8 -*-

# implementation of card game - Memory

import simplegui
import random

state = 0

one_previous = 0
two_previous = 0

numbers = range(0, 8) + range(0, 8)
random.shuffle(numbers)

exposed = [ False ] * len(numbers)

# helper function to initialize globals
def new_game():
    pass  

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    selected = pos[0] // 50
    if not exposed[ selected ]:
        two_previous = one_previous
        one_previous = selected
        if state == 0:
            state = 1
            exposed[ pos[0] // 50 ] = True
        elif state == 1:
            state = 2
            exposed[ pos[0] // 50 ] = True
        elif state == 2:
            if numbers[one_previous] != numbers[two_previous]:
                exposed[one_previous] = False
                exposed[one_previous] = False

                     
            state = 1

    
                        
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

    [ canvas.draw_text( str(numbers[i]), ( i * 50 + 5, 80), 80,  "black" ) for i in range( len( numbers ) ) if exposed[i] ]


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
