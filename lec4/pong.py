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
ball_pos = [WIDTH / 2,  HIGHT / 2]
ball_vel = [1, 1]
paddle1_pos = [PAD_WIDTH / 2,  HIGHT / 2] # start pos
paddle2_pos = [WIDTH - PAD_WIDTH / 2,  HIGHT / 2] # start pos
score1 = 0 
score2 = 0


# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2,  HIGHT / 2]
    if direction == RIGHT:
        ball_vel = [1, 1]
    elif direction == LEFT:
        ball_vel = [-1, 1]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints

def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
        
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos = [ball_pos[0] + ball_vel[0],  ball_pos[1] + ball_vel[1] ]

    # draw ball
    c.draw_circle( BALL_RADIUS, 1, "red", "white")       
    
    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos[1] - PAD_HEIGHT / 2 < 0 or paddle1_pos[1] + PAD_HEIGHT / 2 > HEIGHT: 
        paddle1_pos = [ paddle1_pos[0] + paddle1_vel[0], paddle1_pos[1] + paddle1_vel[1] ]  
    if paddle2_pos[1] - PAD_HEIGHT / 2 < 0 or paddle2_pos[1] + PAD_HEIGHT / 2 > HEIGHT: 
        paddle2_pos = [ paddle2_pos[0] + paddle2_vel[0], paddle2_pos[1] + paddle2_vel[1] ]  

    # draw paddles
    canvas.draw_polygon(
                         [
                            [paddle1_pos[0] - PAD_WIDTH / 2, paddle1_pos[1] - PAD_HEIGHT / 2 ],
                            [paddle1_pos[0] - PAD_WIDTH / 2, paddle1_pos[1] + PAD_HEIGHT / 2 ], 
                            [paddle1_pos[0] + PAD_WIDTH / 2, paddle1_pos[1] - PAD_HEIGHT / 2 ], 
                            [paddle1_pos[0] + PAD_WIDTH / 2, paddle1_pos[1] + PAD_HEIGHT / 2 ], 
                        ],
                        1, 
                        'white',
                        'white'
                        )

    canvas.draw_polygon(
                         [
                            [paddle2_pos[0] - PAD_WIDTH / 2, paddle2_pos[1] - PAD_HEIGHT / 2 ],
                            [paddle2_pos[0] - PAD_WIDTH / 2, paddle2_pos[1] + PAD_HEIGHT / 2 ], 
                            [paddle2_pos[0] + PAD_WIDTH / 2, paddle2_pos[1] - PAD_HEIGHT / 2 ], 
                            [paddle2_pos[0] + PAD_WIDTH / 2, paddle2_pos[1] + PAD_HEIGHT / 2 ], 
                        ],
                        1, 
                        'white',
                        'white'
                        )
    # draw scores
    canvas.draw_text(str(score1), ( WIDTH / 2 - 20 , 40), 20 )
    canvas.draw_text(str(score2), ( WIDTH / 2 + 20 , 40), 20 )
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['up']:
        paddle1_vel = PADDLE_VEL
    elif key == simplegui.KEY_MAP['down']:
        paddle1_vel = [ PADDLE_VEL[0] , -PADDLE_VEL[1] ]
    elif key == simplegui.KEY_MAP['up']:
        paddle1_vel = PADDLE_VEL
        
   
def keyup(key):
    global paddle1_vel, paddle2_vel


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()
frame.start()
