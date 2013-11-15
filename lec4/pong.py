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
PADDLE_VEL = [0, 10]
INITIAL_BALL_VEL = [1, 1]
ball_pos = [WIDTH / 2,  HEIGHT / 2]
ball_vel = INITIAL_BALL_VEL
paddle1_pos = [HALF_PAD_WIDTH,  HEIGHT / 2] # start pos
paddle2_pos = [WIDTH - HALF_PAD_WIDTH,  HEIGHT / 2] # start pos
score1 = 0 
score2 = 0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2,  HEIGHT / 2]
    if direction == RIGHT:
        ball_vel = INITIAL_BALL_VEL
    elif direction == LEFT:
        ball_vel = [ -1 * INITIAL_BALL_VEL[0], INITIAL_BALL_VEL[1]]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, ball_vel  # these are numbers
    global score1, score2  # these are ints
    score1 = score2 = 0
    paddle1_vel = paddle2_vel = [0, 0]
    ball_vel = INITIAL_BALL_VEL
    paddle1_pos = [HALF_PAD_WIDTH,  HEIGHT / 2] # start pos
    paddle2_pos = [WIDTH - HALF_PAD_WIDTH,  HEIGHT / 2] # start pos
    
    # notify player to start and take some seconds until start
    # TODO

    spawn_ball(RIGHT)

def timerHandler():
    global ball_pos, paddle1_pos, paddle2_pos, ball_vel, score1, score2
    
    # update ball pos. when reflect against the wall, velocity flip
    if ball_pos[0] + ball_vel[0] - BALL_RADIUS <= 0:
        ball_vel[0] *= -1
        ball_pos[0] = 0 + BALL_RADIUS
    elif ball_pos[0] + ball_vel[0] + BALL_RADIUS >= WIDTH:
        ball_vel[0] *= -1
        ball_pos[0] = WIDTH - BALL_RADIUS
    else:
        ball_pos[0] = ball_pos[0] + ball_vel[0]        

    if ball_pos[1] + ball_vel[1] - BALL_RADIUS <= 0:
        ball_vel[1] *= -1
        ball_pos[1] = BALL_RADIUS
    elif ball_pos[1] + ball_vel[1] + BALL_RADIUS >= HEIGHT:
        ball_vel[1] *= -1
        ball_pos[1] = HEIGHT - BALL_RADIUS
    else:
        ball_pos[1] = ball_pos[1] + ball_vel[1]        

    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos[1] - HALF_PAD_HEIGHT < 0 or paddle1_pos[1] + HALF_PAD_HEIGHT > HEIGHT: 
        paddle1_pos = [ paddle1_pos[0] + paddle1_vel[0], paddle1_pos[1] + paddle1_vel[1] ]  
    if paddle2_pos[1] - HALF_PAD_HEIGHT < 0 or paddle2_pos[1] + HALF_PAD_HEIGHT > HEIGHT: 
        paddle2_pos = [ paddle2_pos[0] + paddle2_vel[0], paddle2_pos[1] + paddle2_vel[1] ]  

    # count up
    if ball_pos[0] - BALL_RADIUS <= 0 and ( \
                                ( ball_pos[1] < paddle1_pos[1] - HALF_PAD_HEIGHT ) or \
                                 ( ball_pos[1] > paddle1_pos[1] + HALF_PAD_HEIGHT ) \
                                )  :
        score2 += 1
        new_game()
    elif ball_pos[0] + BALL_RADIUS <= 0 and ( 
                                ( ball_pos[1] < paddle2_pos[1] - HALF_PAD_HEIGHT ) or
                                 ( ball_pos[1] > paddle2_pos[1] + HALF_PAD_HEIGHT )
                                )  :
        score1 += 1
        new_game()
    
    # when reflected ball against the paddle, velocity up!
    # TODO
    
timer = simplegui.create_timer(15, timerHandler) # 15 milsecond = 1/60 second

def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos
        
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # draw ball
    c.draw_circle( ball_pos, BALL_RADIUS, 1, "red", "white" )       

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
    c.draw_text(str(score1), ( WIDTH / 2 - 20 , 40), 20, "white" )
    c.draw_text(str(score2), ( WIDTH / 2 + 20 , 40), 20, "white" )
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['up']:
        paddle1_vel = PADDLE_VEL
    elif key == simplegui.KEY_MAP['down']:
        paddle1_vel = [ PADDLE_VEL[0] , -PADDLE_VEL[1] ]
    elif key == simplegui.KEY_MAP['w']:
        paddle2_vel = PADDLE_VEL
    elif key == simplegui.KEY_MAP['s']:
        paddle2_vel = [ PADDLE_VEL[0] , -PADDLE_VEL[1] ]
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    paddle1_vel = paddle2_vel = [0, 0]

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()
timer.start()
frame.start()
