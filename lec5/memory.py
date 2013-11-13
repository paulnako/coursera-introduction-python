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
counter = 0

# helper function to initialize globals
def new_game():
    global counter, exposed, numbers
    exposed = [ False ] * len(numbers)
    counter = 0
    random.shuffle(numbers)

     
# define event handlers
def mouseclick(pos):
    global one_previous, two_previous, state, counter
    # add game state logic here
    selected = pos[0] // 50
    if not exposed[ selected ]:
        counter += 1
        if state == 0:
            state = 1
            exposed[ selected ] = True
        elif state == 1:
            state = 2
            exposed[ selected ] = True
        elif state == 2:
            if numbers[one_previous] != numbers[two_previous]:
                exposed[one_previous] = False
                exposed[two_previous] = False
            exposed[ selected ] = True
            state = 1
        two_previous = one_previous
        one_previous = selected
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global counter
    for i in range(0, 16):
        canvas.draw_polygon( 
                            ( (0 + i * 50, 0), ( 0 + i * 50, 100 ), ( 50 + i * 50, 100 ), ( 50 + i * 50, 0 )) ,
                            1, 
                            "black", 
                            "green"
                            )

    [ canvas.draw_text( str(numbers[i]), ( i * 50 + 2, 80), 80,  "black" ) for i in range( len( numbers ) ) if exposed[i] ]
    label.set_text("Turns = %d" % counter )


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
