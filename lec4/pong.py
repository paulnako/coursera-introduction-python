# -*- coding:utf-8 -*-

# Implementation of classic arcade game Pong
import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
PADDLE_VEL = [0, 7]
INITIAL_BALL_VEL = [3, 0.5]
ball_pos = [WIDTH / 2,  HEIGHT / 2]
ball_vel = INITIAL_BALL_VEL
paddle1_pos = [HALF_PAD_WIDTH,  HEIGHT / 2] # start pos
paddle2_pos = [WIDTH - HALF_PAD_WIDTH,  HEIGHT / 2] # start pos
score1 = 0 
score2 = 0
paddle1_move_up = False
paddle1_move_down = False
paddle2_move_up = False
paddle2_move_down = False
paddle1_direction = ""
paddle2_direction = ""

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2,  HEIGHT / 2]
    if direction == RIGHT:
        ball_vel = [ INITIAL_BALL_VEL[0], INITIAL_BALL_VEL[1]]
    elif direction == LEFT:
        ball_vel = [ -1 * INITIAL_BALL_VEL[0], INITIAL_BALL_VEL[1]]

# define event handlers
def new_game(direction = random.choice([RIGHT, LEFT])):
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, ball_vel  # these are numbers
    global score1, score2  # these are ints
    score1 = score2 = 0
    paddle1_vel = [0, 0]
    paddle2_vel = [0, 0]
    paddle1_pos = [HALF_PAD_WIDTH,  HEIGHT / 2] # start pos
    paddle2_pos = [WIDTH - HALF_PAD_WIDTH,  HEIGHT / 2] # start pos
    
    # notify player to start and take some seconds until start
    # TODO

    spawn_ball(direction)

def timerHandler():
    global ball_pos, paddle1_pos, paddle2_pos, ball_vel, score1, score2, paddle1_vel, paddle2_vel
    global paddle1_direction, paddle2_direction

    # update ball pos. when reflect against the wall, velocity flip
    if ball_pos[0] + ball_vel[0] - BALL_RADIUS < 0:
        # when reflected ball against the paddle, velocity up!
        ball_vel[0] *= 1.1
        ball_vel[0] *= 1.1
        ball_vel[0] *= -1
        ball_pos[0] = 0 + BALL_RADIUS
    elif ball_pos[0] + ball_vel[0] + BALL_RADIUS > WIDTH:
        ball_vel[0] *= 1.1
        ball_vel[0] *= 1.1
        ball_vel[0] *= -1
        ball_pos[0] = WIDTH - BALL_RADIUS
    else:
        ball_pos[0] = ball_pos[0] + ball_vel[0]        

    if ball_pos[1] + ball_vel[1] - BALL_RADIUS < 0:
        ball_vel[1] *= -1
        ball_pos[1] = BALL_RADIUS
    elif ball_pos[1] + ball_vel[1] + BALL_RADIUS > HEIGHT:
        ball_vel[1] *= -1
        ball_pos[1] = HEIGHT - BALL_RADIUS
    else:
        ball_pos[1] = ball_pos[1] + ball_vel[1]        

    # update paddle's velocity
    if paddle2_move_up and paddle2_move_down:
        if paddle2_direction == "up":
            paddle2_vel = [ PADDLE_VEL[0] , - PADDLE_VEL[1] ]
        elif paddle2_direction == "down":
            paddle2_vel = [ PADDLE_VEL[0] , PADDLE_VEL[1] ]
    elif paddle2_move_up:     
        paddle2_vel = [ PADDLE_VEL[0] , - PADDLE_VEL[1] ]
    elif paddle2_move_down:     
        paddle2_vel = [ PADDLE_VEL[0] , PADDLE_VEL[1] ]
    else :
        paddle2_vel = [0, 0]

    if paddle1_move_up and paddle1_move_down:
        if paddle1_direction == "up":
            paddle1_vel = [ PADDLE_VEL[0] , - PADDLE_VEL[1] ]
        elif paddle1_direction == "down":
            paddle1_vel = [ PADDLE_VEL[0] , PADDLE_VEL[1] ]
    elif paddle1_move_up:     
        paddle1_vel = [ PADDLE_VEL[0] , - PADDLE_VEL[1] ]
    elif paddle1_move_down:     
        paddle1_vel = [ PADDLE_VEL[0] , PADDLE_VEL[1] ]
    else :
        paddle1_vel = [0, 0]

    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos[1] + paddle1_vel[1] - HALF_PAD_HEIGHT > 0 \
        and paddle1_pos[1] + paddle1_vel[1] + HALF_PAD_HEIGHT < HEIGHT: 
        paddle1_pos = [ paddle1_pos[0] + paddle1_vel[0], paddle1_pos[1] + paddle1_vel[1] ]  
    elif paddle1_pos[1] + paddle1_vel[1] - HALF_PAD_HEIGHT <= 0 \
        and paddle1_pos[1] + paddle1_vel[1] + HALF_PAD_HEIGHT < HEIGHT :
        paddle1_pos = [ paddle1_pos[0] + paddle1_vel[0], HALF_PAD_HEIGHT]  
    elif paddle1_pos[1] + paddle1_vel[1] + HALF_PAD_HEIGHT >= HEIGHT \
        and paddle1_pos[1] + paddle1_vel[1] - HALF_PAD_HEIGHT > 0 :
        paddle1_pos = [ paddle1_pos[0] + paddle1_vel[0], HEIGHT - HALF_PAD_HEIGHT]  

    if paddle2_pos[1] + paddle2_vel[1] - HALF_PAD_HEIGHT > 0 \
       and paddle2_pos[1] + paddle2_vel[1] + HALF_PAD_HEIGHT < HEIGHT: 
        paddle2_pos = [ paddle2_pos[0] + paddle2_vel[0], paddle2_pos[1] + paddle2_vel[1] ]  
    elif paddle2_pos[1] + paddle2_vel[1] - HALF_PAD_HEIGHT <= 0 \
        and paddle2_pos[1] + paddle2_vel[1] + HALF_PAD_HEIGHT < HEIGHT :
        paddle2_pos = [ paddle2_pos[0] + paddle2_vel[0], HALF_PAD_HEIGHT]  
    elif paddle2_pos[1] + paddle2_vel[1] + HALF_PAD_HEIGHT >= HEIGHT \
        and paddle2_pos[1] + paddle2_vel[1] - HALF_PAD_HEIGHT > 0 :
        paddle2_pos = [ paddle2_pos[0] + paddle2_vel[0], HEIGHT - HALF_PAD_HEIGHT]  

    # count up
    if ball_pos[0] - BALL_RADIUS - PAD_WIDTH < 0 and ( \
                                ( ball_pos[1] < paddle1_pos[1] - HALF_PAD_HEIGHT ) or \
                                 ( ball_pos[1] > paddle1_pos[1] + HALF_PAD_HEIGHT ) \
                                )  :
        score2 += 1 
        spawn_ball(RIGHT)
    elif ball_pos[0] + BALL_RADIUS + PAD_WIDTH > WIDTH and ( 
                                ( ball_pos[1] < paddle2_pos[1] - HALF_PAD_HEIGHT ) or
                                 ( ball_pos[1] > paddle2_pos[1] + HALF_PAD_HEIGHT )
                                )  :
        score1 += 1 
        spawn_ball(LEFT)


    
timer = simplegui.create_timer(15, timerHandler) # 15 milsecond = 1/60 second

def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos
        
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # draw ball
    c.draw_circle( ball_pos, BALL_RADIUS, 1, "white", "white" )       

    # draw paddles
    c.draw_polygon(
                         [
                            [paddle1_pos[0] - HALF_PAD_WIDTH, paddle1_pos[1] - HALF_PAD_HEIGHT ],
                            [paddle1_pos[0] + HALF_PAD_WIDTH, paddle1_pos[1] - HALF_PAD_HEIGHT ], 
                            [paddle1_pos[0] + HALF_PAD_WIDTH, paddle1_pos[1] + HALF_PAD_HEIGHT ], 
                            [paddle1_pos[0] - HALF_PAD_WIDTH, paddle1_pos[1] + HALF_PAD_HEIGHT ], 
                        ],
                        1, 
                        'white',
                        'white'
                        )

    c.draw_polygon(
                         [
                            [paddle2_pos[0] - HALF_PAD_WIDTH, paddle2_pos[1] - HALF_PAD_HEIGHT ],
                            [paddle2_pos[0] + HALF_PAD_WIDTH, paddle2_pos[1] - HALF_PAD_HEIGHT ], 
                            [paddle2_pos[0] + HALF_PAD_WIDTH, paddle2_pos[1] + HALF_PAD_HEIGHT ], 
                            [paddle2_pos[0] - HALF_PAD_WIDTH, paddle2_pos[1] + HALF_PAD_HEIGHT ], 
                        ],
                        1, 
                        'white',
                        'white'
                        )
    # draw scores
    c.draw_text(str(score1), ( WIDTH / 2 - 120 , 100), 60, "white", "serif" )
    c.draw_text(str(score2), ( WIDTH / 2 + 120 , 100), 60, "white", "serif" )
        
def keydown(key):
    global paddle1_vel, paddle2_vel, paddle1_move_up, paddle1_move_down, paddle2_move_up, paddle2_move_down
    global paddle1_direction, paddle2_direction
    if key == simplegui.KEY_MAP['up']:
        paddle2_move_up = True
        paddle2_direction = "up"
    elif key == simplegui.KEY_MAP['down']:
        paddle2_move_down = True
        paddle2_direction = "down"
    elif key == simplegui.KEY_MAP['w']:
        paddle1_move_up = True
        paddle1_direction = "up"
    elif key == simplegui.KEY_MAP['s']: 
        paddle1_move_down = True
        paddle1_direction = "down"
   
def keyup(key):
    global  paddle1_move_up, paddle1_move_down, paddle2_move_up, paddle2_move_down
    global  paddle1_direction, paddle2_direction

    if key == simplegui.KEY_MAP['up']:
        paddle2_move_up = False
        if not paddle2_move_down:
            paddle2_direction = ""
    elif key == simplegui.KEY_MAP['down']:
        paddle2_move_down = False
        if not paddle2_move_up:
            paddle2_direction = ""
    elif key == simplegui.KEY_MAP['w']:
        paddle1_move_up = False
        paddle1_direction = ""
        if not paddle1_move_down:
            paddle1_direction = ""
    elif key == simplegui.KEY_MAP['s']:
        paddle1_move_down = False
        if not paddle1_move_up:
            paddle1_direction = ""

def restartHandler():
    new_game()

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", restartHandler)

# start frame
new_game()
timer.start()
frame.start()
