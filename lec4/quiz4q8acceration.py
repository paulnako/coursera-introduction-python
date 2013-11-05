# -*- coding:utf-8 -*-
import simplegui

start = [0, 0]
point = start
velocity = [0, 0]
acceleration = [0, 0]
delta = [0.1, 0.2]

trace = []
def drawHandler(canvas):
    global count
    global point
    global velocity
    global acceleration
    global delta

    acceleration[0] += delta[0]
    acceleration[1] += delta[1]

    velocity[0] += acceleration[0]
    velocity[1] += acceleration[1]

    point = [point[0] + velocity[0], point[1] + velocity[1]]
    trace.append(point)
    canvas.draw_polygon(trace, 1, "red")

frame = simplegui.create_frame("acceleration", 3000, 2000)
frame.set_draw_handler(drawHandler)

frame.start()
