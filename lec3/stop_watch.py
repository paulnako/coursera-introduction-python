# -*- coding:utf-8 -*-
import simplegui
status_running = False
time_elapsed = 0
successful_stop = 0
total_stop = 0

# define event handler for timer with 0.1 sec interval
def timerHandler():
    global time_elapsed
    time_elapsed += 1

timer = simplegui.create_timer(100,timerHandler )

# template for "Stopwatch: The Game"

# define global variables


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    return "%d:%d%d.%d" % ( t // 600, ( t % 600 ) // 100, ( t % 100 ) // 10, t % 10)
        
# define event handlers for buttons; "Start", "Stop", "Reset"
def startHandler():
    global status_running
    status_running = True
    timer.start()

def stopHandler():
    global successful_stop
    global status_running
    if status_running:
        global total_stop
        timer.stop()
        total_stop += 1
        if time_elapsed % 50 == 0:
            successful_stop += 1
    status_running = False
 
def resetHandler():
    global time_elapsed
    global successful_stop
    global total_stop
    global status_running
    timer.stop()
    successful_stop = 0
    total_stop = 0
    time_elapsed = 0
    status_running = False

# define draw handler
def drawHandler(canvas):
    canvas.draw_text(format( time_elapsed ), (80, 120), 50, "white" )
    canvas.draw_text( "%d / %d" % (successful_stop, total_stop)  , (260, 15), 20, "green" )
    
# create frame
frame = simplegui.create_frame("stop_watch", 300, 200)
frame.add_button("Start", startHandler)
frame.add_button("Stop", stopHandler)
frame.add_button("Reset", resetHandler)

# register event handlers
frame.set_draw_handler(drawHandler)

# start frame
frame.start()

# Please remember to review the grading rubric

