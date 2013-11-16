# -*- coding:utf-8 -*-

import simplegui

image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/alphatest.png")
def drawHandler(canvas):
    canvas.draw_image(image,  [220, 100], [100, 100], [220, 100], [500, 400])

frame = simplegui.create_frame( "alphabet", 500, 400 )
frame.set_draw_handler(drawHandler)
frame.start()
