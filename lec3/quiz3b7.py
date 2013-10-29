# -*- coding:utf-8 -*-

# Mystery computation in Python
# Takes input n and computes output named result

import simplegui

# global state

result = 1
iteration = 0
max_iterations = 20

# helper functions

def init(start):
    """Initializes n."""
    global result
    result = start
    print "Input is", result
    
def get_next(current):
    return current / 2 if current % 2 == 0 else current * 3 + 1
# timer callback

def update():
    global iteration, result
    iteration += 1
    # Stop iterating after max_iterations
    if iteration >= max_iterations:
        timer.stop()
        print "Output is", result
    else:
        result = get_next(result)
        print result

# register event handlers

timer = simplegui.create_timer(1, update)

# start program
init(217)
timer.start()
