# -*- coding:utf-8 -*-
import simplegui
status_running = False
time_elapsed = 0
def timerHandler():
    pass
timer = simplegui.create_timer(100,timerHandler )
# template for "Stopwatch: The Game"

# define global variables


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    return "%d:%d%d.%d" % ( t // 600, ( t % 600 ) // 100, ( t % 100 ) // 10, t % 10)
        
# define event handlers for buttons; "Start", "Stop", "Reset"
def startHandler():
    timer.start()

def stopHandler():
    timer.stop()

def resetHandler():
    timer.stop()
    global time_elapsed
    time_elapsed = 0

# define event handler for timer with 0.1 sec interval
def timerHandler():
    global time_elapsed
    ++time_elapsed 

# define draw handler
def drawHandler(canvas):
    canvas.draw_text(format( time_elapsed ), (100, 100), "white" )

    
# create frame
frame = simplegui.create_frame("stop_watch", 300, 200)
frame.add_button("start", startHandler)
frame.add_button("stop", stopHandler)
frame.add_button("reset", resetHandler)

# register event handlers
frame.set_draw_handler(drawHandler)

# start frame
frame.start()

# Please remember to review the grading rubric

