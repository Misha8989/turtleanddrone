# from djitellopy import Tello
#import turtle
import pygame
clock = pygame.time.Clock()

x = 60
y = 60
color = (255,255,255)
background = (0,0,0)

pygame.init()
win = pygame.display.set_mode((500,500))
win.fill(background)
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()
    pygame.draw.rect(win, color, pygame.Rect(x, y, 90, 90))
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        y -= 1
        if x<=0:
          x=0
        elif x>=400:
          x=400
        if y>=400:
          y=400
        elif y<=0:
          y=0
        win.fill(background)
    if pressed[pygame.K_DOWN]: 
        y += 1
        if x<=0:
          x=0
        elif x>=400:
          x=400
        if y>=400:
          y=400
        elif y<=0:
          y=0
        win.fill(background)
    if pressed[pygame.K_RIGHT]:
        x += 1
        if x<=0:
          x=0
        elif x>=400:
          x=400
        if y>=400:
          y=400
        elif y<=0:
          y=0
        win.fill(background)
    if pressed[pygame.K_LEFT]: 
        x -= 1
        if x<=0:
          x=0
        elif x>=400:
          x=400
        if y>=400:
          y=400
        elif y<=0:
          y=0
        win.fill(background)
    pygame.display.update()
    clock.tick(60)

# # tello = Tello()

# screen = turtle.Screen()
# screen.setup(500,500)
# screen.bgcolor("blue")
# t = turtle.Turtle()
# t.shape("square")
# t.goto(0,0)
# tello.connect()
# def move_right_control():
#     tello.move_right(40)
# def move_left_control():
#     tello.move_left(40)
# def move_forward_control():
#     tello.move_forward(40)
# def move_backward_control():
#     tello.move_back(40)
# def move_up_control():
#     tello.takeoff()
# def move_down_control():    
#     tello.land()

# move_up_control()
# move_forward_control()
# move_left_control()
# move_right_control()
# move_down_control()


# def drone():
#    tello.rotate_clockwise(90)
#    tello.move_forward(30)
#    tello.rotate_clockwise(90)
#    tello.move_forward(30)
#    tello.rotate_clockwise(90)
#    tello.move_forward(30)

#tello.move_left(50)
#tello.move_right(50)
#tello.move_forward(50)
#tello.move_back(50)
# for i in range(0,3):w

#tello.land()
