# -*- coding:utf-8 -*-
# http://www.codeskulptor.org/#user26_vCcy99ZSCB_0.py

# program template for Spaceship
import simplegui
import math
import random

# globals for user interface
WIDTH = 800
HEIGHT = 600
score = 0
lives = 3
time = 0.5
angle_accel = 0
is_pressing_left = False
is_pressing_right = False
angle_accel_timer = None
a_missile = None
rock_group = set()
lives = 0
score = 0

def add_vec(pos, vec, index):
    pos[index] = pos[index] + vec[index] 

class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated

    
# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim
    
# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.f2013.png")

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, 50)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")

# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)


# Ship class
class Ship:
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        
    def draw(self,canvas):
        # canvas.draw_circle(self.pos, self.radius, 1, "White", "White")
        if self.thrust:
            image_center = [ self.image_center[0] + self.image_size[0], self.image_center[1] ] 
        else: 
            image_center =[ self.image_center[0], self.image_center[1]] 
        canvas.draw_image(self.image, image_center, self.image_size, self.pos, self.image_size, self.angle)

    def update(self):
        add_vec(self.pos, self.vel, 0)
        add_vec(self.pos, self.vel, 1)
        if self.pos[0] < -self.image_center[0]:
            self.pos[0] = WIDTH + self.image_center[0]
        elif self.pos[0] > WIDTH + self.image_center[0]:
            self.pos[0] = -self.image_center[0]

        if self.pos[1] < -self.image_center[1]:
            self.pos[1] = HEIGHT + self.image_center[1]
        elif self.pos[1] > HEIGHT + self.image_center[1]:
            self.pos[1] = -self.image_center[1]
        
        self.angle += self.angle_vel
        angle_vec = angle_to_vector(self.angle)
        angle_vec[0] *= 0.3
        angle_vec[1] *= 0.3
        if self.thrust:
            add_vec(self.vel, angle_vec, 0)
            add_vec(self.vel, angle_vec, 1)

        self.vel = [ self.vel[0] * 0.92, self.vel[1] * 0.92 ]

    def add_angle(self, ang_vel):
        self.angle_vel += ang_vel

    def set_thrust(self, thrusting):
        self.thrust = thrusting
        if thrusting:
            ship_thrust_sound.rewind()
            ship_thrust_sound.play()
        else:
            ship_thrust_sound.rewind()
            ship_thrust_sound.pause()
    
    def shoot(self):
        global a_missile
        original_cannon_pos = [ self.pos[0] + self.image_size[0] / 2, self.pos[1] ]

        rotated_cannon_pos = [
                            ( original_cannon_pos[0]-self.pos[0]) * math.cos( self.angle ) - 
                                ( original_cannon_pos[1] - self.pos[1] ) * math.sin( self.angle ) + self.pos[0],
                            (original_cannon_pos[0] - self.pos[0]) * math.sin( self.angle ) +
                                ( original_cannon_pos[1] - self.pos[1] ) * math.cos( self.angle ) + self.pos[1] ]

        a_missile = Sprite(rotated_cannon_pos, 
                            [ 10 * math.cos( self.angle ) + self.vel[0], 10 * math.sin( self.angle ) + self.vel[1] ],
                            self.angle,
                            0, 
                            missile_image, 
                            missile_info, 
                            missile_sound
                            )
        
        
# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()
   
    def draw(self, canvas):
    #    canvas.draw_circle(self.pos, self.radius, 1, "Red", "Red")
        canvas.draw_image( self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)
    
    def update(self):
        add_vec( self.pos, self.vel, 0)
        add_vec( self.pos, self.vel, 1)

        self.angle += self.angle_vel

    def collide(self, other_object):
        other_pos = other_object.get_position()[0]
        dist = (self.pos[0] - other_pos[0]) ** 2 + (self.pos[1] - other_pos[1]) ** 2
        dist = sqrt(dist)
        return self.radius + other_object.get_radius() <= dist

    def get_position(self):
        return self.pos

    def get_radius(self):
        return self.get_radius

def spin_ship():
    if  - 0.07 < my_ship.angle_vel < 0.07 :
        my_ship.add_angle(angle_accel)

def process_sprite_group( canvas, sprite_set):
    for sprite in sprite_set:
        sprite.update()
        sprite.draw(canvas)


def keydown_handler(key):
    global angle_accel, angle_accel_timer, thrusting, is_pressing_left, is_pressing_right 
    angle_accel_val = 0.008
    if key == simplegui.KEY_MAP['left']:
        angle_accel = -angle_accel_val
        if angle_accel_timer:
            angle_accel_timer.stop()
        angle_accel_timer = simplegui.create_timer( ( 1000 / 60), spin_ship)
        my_ship.angle_vel = 0
        angle_accel_timer.start()
        is_pressing_left = True
    elif key == simplegui.KEY_MAP['right']:
        angle_accel = angle_accel_val
        if angle_accel_timer:
            angle_accel_timer.stop()
        angle_accel_timer = simplegui.create_timer( ( 1000 / 60), spin_ship)
        my_ship.angle_vel = 0
        angle_accel_timer.start()
        is_pressing_right = True
    elif key == simplegui.KEY_MAP['up']:
        my_ship.set_thrust(True)
    elif key == simplegui.KEY_MAP['space']:
        my_ship.shoot()


def keyup_handler(key):
    global angle_accel, angle_accel_timer, thrusting, is_pressing_left, is_pressing_right 
    if key == simplegui.KEY_MAP['left']:
        is_pressing_left = False
        if is_pressing_left:
            keydown_handler(simplegui.KEY_MAP['left'])
        elif is_pressing_right:
            keydown_handler(simplegui.KEY_MAP['right'])
        else:
            my_ship.angle_vel = 0
            angle_accel_timer.stop()
    elif key == simplegui.KEY_MAP['right']:
        is_pressing_right = False
        if is_pressing_left:
            keydown_handler(simplegui.KEY_MAP['left'])
        elif is_pressing_right:
            keydown_handler(simplegui.KEY_MAP['right'])
        else:
            my_ship.angle_vel = 0
            angle_accel_timer.stop()
    elif key == simplegui.KEY_MAP['up']: 
        my_ship.set_thrust(False)

           
def draw(canvas):
    global time, rock_group, a_missile, my_ship, lives, score
    
    # animiate background
    time += 1
    wtime = (time / 4) % WIDTH
    center = debris_info.get_center()
    size = debris_info.get_size()
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))

    canvas.draw_text("Lives", [  70, 40 ], 20, "White")
    canvas.draw_text(str(lives), [ 70, 60 ], 20, "White")

    canvas.draw_text("Score", [ WIDTH - 140, 40 ], 20, "White")
    canvas.draw_text(str(score), [ WIDTH - 140, 60 ], 20, "White")

    # draw ship and sprites
    my_ship.draw(canvas)
    process_sprite_group(rock_group)
    if a_missile:
        a_missile.draw(canvas)
    
    # update ship and sprites
    my_ship.update()
    if a_missile:
        a_missile.update()
            
# timer handler that spawns a rock    
def rock_spawner():
    global rock_group
    if len( rock_group) < 12:
        rock_group.add(
                    Sprite([ random.randint(0, WIDTH) ,
                          random.randint(0, HEIGHT)],
                          [ random.randint(-10, 10 ) / 10.0, random.randint(-10, 10 ) / 10.0],
                          random.randint(-68, 68 ) / 10.0,
                          random.randint(-5, 5 ) / 10.0,
                          asteroid_image,
                          asteroid_info)
                        )


    
# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

# initialize ship and two sprites
my_ship = Ship([100, 200], [0, 0], 0, ship_image, ship_info)

# register handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown_handler)
frame.set_keyup_handler(keyup_handler)

timer = simplegui.create_timer(1000.0, rock_spawner)

# get things rolling
timer.start()
frame.start()
