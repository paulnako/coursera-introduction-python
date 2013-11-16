# -*- coding:utf-8 -*-

# Image positioning problem

###################################################
# Student should enter code below

import simplegui

# global constants
WIDTH = 400
HEIGHT = 300
clicked = []

# load test image
asteroid = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/asteroid.png")


# mouseclick handler
def click(pos):
    global clicked
    clicked = [ pos[0], pos[1] ] 

    
# draw handler
def draw(canvas):
    global clicked, asteroid
    if clicked:
        canvas.draw_image( asteroid, [ 95/2 , 93/2 ] , [95, 93], clicked, [95, 93]  )

    
# create frame and register draw handler    
frame = simplegui.create_frame("Test image", WIDTH, HEIGHT)
frame.set_canvas_background("Gray")
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click)

# start frame
frame.start()
