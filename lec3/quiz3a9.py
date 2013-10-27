# -*- coding:utf-8 -*-

# first example of drawing on the canvas

import simplegui

# define draw handler
def draw(canvas):
    canvas.draw_circle([90, 200], 20, 10, "white")
    canvas.draw_circle([210, 200], 20, 10, "white")
    canvas.draw_line([50, 180], [250, 180], 40, "red")
    canvas.draw_line([55, 170], [90, 120], 5, "red")
    canvas.draw_line([90, 120], [130, 120], 5, "red")
    canvas.draw_line([180, 108], [180, 160], 140, "red")

# create frame
frame = simplegui.create_frame("Text drawing", 300, 300)

# register draw handler    
frame.set_draw_handler(draw)

# start frame
frame.start()
