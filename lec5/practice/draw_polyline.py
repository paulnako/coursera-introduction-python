# -*- coding:utf-8 -*-


# Polyline drawing problem

###################################################
# Student should enter code below

import simplegui
import math

polyline = []


# define mouseclick handler
def click(pos):
    global polyline
    polyline.append(pos)
          
# button to clear canvas
def clear():
    global polyline
    polyline = []

# define draw
def draw(canvas):
    global polyline
    if len(polyline) == 1:
        canvas.draw_circle(polyline[0], 10, 1,  "red")
    elif polyline:
        canvas.draw_polyline(polyline, 1, "red")
                   
# create frame and register handlers
frame = simplegui.create_frame("Echo click", 300, 200)
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)
frame.add_button("Clear", clear)

# start frame
frame.start()
