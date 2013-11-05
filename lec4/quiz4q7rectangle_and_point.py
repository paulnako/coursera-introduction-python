# -*- coding:utf-8 -*-

import simplegui

start_point = [10, 20]
velocity = [3, 0.7]
point = [10, 20]

def draw_handler(canvas):
    canvas.draw_polygon([ [50, 50] , [180, 50] , [180, 140] , [50, 140]] , 1, "white") 
    point[0] += velocity[0]
    point[1] += velocity[1]
    canvas.draw_line( start_point, point, 1, "red") 


frame = simplegui.create_frame("colllision", 300, 200)

frame.set_draw_handler(draw_handler)

frame.start()
