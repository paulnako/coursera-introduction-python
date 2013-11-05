# -*- coding:utf-8 -*-

import simplegui
num = 5

def downHandler(key):
    global num
    num *= 2
    print num

def upHandler(key):
    global num
    num -= 3
    print num

frame = simplegui.create_frame("key press an up", 300, 200)
frame.set_keydown_handler(downHandler)
frame.set_keyup_handler(upHandler)

frame.start()
