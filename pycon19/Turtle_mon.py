# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 10:47:44 2019

@author: Patrick.Barry
"""

import turtle
from random import randint



POPULATION = 1 #looper

def mon_maker():
    """Our very first monster"""
    random_mon = {'eyeratio':0.2, 'eyeL':30,
                  'mouthratio':0.8, 'mouthL':30,
                  'headL':40, 'headA':15,
                  'cheekL':25, 'cheekA':45,
                  'chinL': 30, 'chinA':90
                 }
    return random_mon

def drawhalfmonster(mirror, generikmon):
    """draws a half of a symetrical monster"""
    # place turtle at top middle facing up
    back_to_start()

    turtle.right(mirror*90)                 #requires turtle to be facing upwards
    turtle.right(mirror*generikmon['headA'])
    turtle.forward(generikmon['headL'])
    turtle.right(mirror*generikmon['cheekA'])
    turtle.forward(generikmon['cheekL'])
    turtle.right(mirror*generikmon['chinA'])
    turtle.forward(generikmon['chinL'])

    # get back to centerline
    turtle.setx(0)
    #note y cord of bottom of chin to figure out how far down to go to draw mouth
    y_chin = turtle.ycor()

    ### draw mouth
    back_to_start()
    turtle.penup()  # unless you want to draw a cat's nose
    turtle.forward(y_chin*generikmon['mouthratio'])
    turtle.right(mirror*90)
    turtle.pendown()
    turtle.forward(generikmon['mouthL'])

    ### draw eyes
    back_to_start()
    turtle.penup()  # unless you want to draw a cat's nose
    turtle.forward(y_chin*generikmon['eyeratio'])
    turtle.right(mirror*-90)
    turtle.forward(generikmon['eyeL'])
    turtle.shape("circle")
    turtle.stamp()

    turtle.penup()
    turtle.home()

def draw_monster(generikmon):
    """draws each half of the monster in turn"""
    turtle.clear()
    mirror = 1
    drawhalfmonster(mirror, generikmon)
    mirror = -1
    drawhalfmonster(mirror, generikmon)  #draws second half of monster
    return()

def back_to_start():
    """reset turtle"""
    turtle.penup()
    turtle.home()
    turtle.setheading(90)
    turtle.pendown()

def mutate_monster(generikmon):
    """step through monster randomly tweaking all of its numbers"""
    childmon = generikmon.copy()
    for ikey, ival in childmon.items():
        childmon[ikey] = childmon[ikey] * (1 + randint(-10, 10)/100)
       # ival not used in this case
    return childmon

def evaulate_monster(generikmon):
    """what are you trying to evolve your monster for?"""
    score = generikmon['headA']
    #score = generikmon['chinA']
    return score

#### main

mon1 = mon_maker()
fitness = []
for i in range(1, 20):
    #print(mon1)
    #draw_monster( mon1)
    mon2 = mutate_monster(mon1)
    score1 = evaulate_monster(mon1)
    score2 = evaulate_monster(mon2)
    print(score1, score2)
    if score1 >= score2:
        mon1 = mon1
        fitness.append(score1)
    else:
        mon1 = mon2
        fitness.append(score2)
        print('generation ', i, 'new mutation')

### make a graph of the fitness score
turtle.hideturtle()
turtle.clear()
draw_monster(mon1)
back_to_start()
turtle.penup()
turtle.forward(50)
turtle.pendown()

for i in fitness:
    x = turtle.xcor() + 2
    turtle.setpos(x, i + 50)
