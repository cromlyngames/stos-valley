import turtle
import random
   
testingmon = [0,
    0.4,                         #crownD,
    90, 0.15, 45, 90, 45, 0.1,   #ear1A,ear2D,ear3A,ear4A,ear5A,ear5D,
    0.2, 60, 0.17,               #cheekD,jawlineA,shoulderD,
    60, 0.3, 10, 0.3,            #shoulderA, thighD, elbowA, shinD
    3, 0.75, 0.12,               #NumOfToes, frontbackratio, toelengthD, 
    0.1, 0.5, 80, 0.1           #tailbodywidthratio, tailspineD, tailtipA, tailtipD
    ]


mirror=1       #used to reflect the turtle
scale =100  #used to scale the size of the monster
looper=1    #if 0 then program will complete



def randommonMaker():
    randommon = [0,
        random.random()*0.4,                         #crownD,
        random.randint(45, 135), random.random()*0.15, random.randint(15, 75), random.randint(45, 135), random.randint(15, 75), random.random()*0.1,   #ear1A,ear2D,ear3A,ear4A,ear5A,ear5D,
        random.random()*0.2, random.randint(10, 70), random.random()*0.17,               #cheekD,jawlineA,shoulderD,
        random.randint(30, 90), random.random()*0.3, random.randint(5, 20), random.random()*0.3,            #shoulderA, thighD, elbowA, shinD
        random.randint(1, 5), random.random()*0.75, random.random()*0.12,               #NumOfToes, frontbackratio, toelengthD, 
        random.random()*0.1, random.random()*0.5, random.randint(1, 89), random.random()*0.1           #tailbodywidthratio, tailspineD, tailtipA, tailtipD
        ]
    return(randommon)




def drawmonster(mirror, scale, generikmon):
  #  for i in range(25):
   #       print(generikmon[i], i)
    badnesscount=0

    turtle.right(mirror*90)                 #requires turtle to be facing upwards       
    turtle.forward(scale*generikmon[1])  #crownD
    turtle.left(mirror*generikmon[2])     #ear1A
    turtle.forward(scale*generikmon[3])  #ear2D
    turtle.right(mirror*generikmon[4])    #ear3A
    turtle.forward(scale*generikmon[3])  #ear2D
    turtle.right(mirror*generikmon[5])    #ear4A
    turtle.forward(scale*generikmon[7])  #ear5D
    turtle.right(mirror*generikmon[6])    #ear5A
    turtle.forward(scale*generikmon[7])  #ear5D
    #into the cheek
    turtle.setheading(270)         #fixed
    turtle.forward(scale*generikmon[8])  #cheekD
    if turtle.xcor()*mirror<0:
        badnesscount=badnesscount+1
        return(badnesscount)
    if turtle.ycor()>0:
        badnesscount=badnesscount+2
        return(badnesscount)
    #along the jaw and then the shoulder
    turtle.left(mirror*generikmon[9])     #jawlineA
    turtle.forward(scale*generikmon[10]) #shoulderD
    turtle.right(mirror*(180-generikmon[9]))
    turtle.forward(scale*generikmon[10]*2)
    if turtle.xcor()*mirror<0:
        badnesscount=badnesscount+3
        return(badnesscount)
    if turtle.ycor()>0:
        badnesscount=badnesscount+2
        return(badnesscount)
    #down the arm
    turtle.left(mirror*generikmon[11])    #shoulderA
    turtle.forward(scale*generikmon[12]) #thighD
    turtle.left(mirror*generikmon[13])    #elbowA
    turtle.forward(scale*generikmon[14])#shinD
    # into the toes!
    NumofToes = generikmon[15]
    fullwidth= turtle.xcor()
    tailwidth= fullwidth*generikmon[18] #talibodywidthratio,
    pawswidth= fullwidth-tailwidth
    frontpawwidth=pawswidth*generikmon[16] #fronttobackratio
    toewidth=frontpawwidth/(NumofToes)
    if turtle.ycor()>0:
        badnesscount=badnesscount+2
        return(badnesscount)
    for i in range(NumofToes):
        turtle.setheading(270)
        turtle.forward(scale*generikmon[17])#toelengthD
        turtle.right(mirror*90)
        turtle.forward(mirror*toewidth)  #mirror required here since xcord is negative on second hlaf
        turtle.right(mirror*90)
        turtle.forward(scale*generikmon[17]) #toelegnth - going back up               
      #into the rear toes. # all lengths scaled by generikmon[16] = frontotbackratio
    toewidth=(pawswidth-frontpawwidth)/NumofToes  #redefines toe width for backpaws.
    for i in range(NumofToes):
        turtle.setheading(270)
        turtle.forward(scale*generikmon[16]*generikmon[17])#toelengthD
        turtle.right(mirror*90)
        turtle.forward(mirror*toewidth)
        turtle.right(mirror*90)
        turtle.forward(scale*generikmon[16]*generikmon[17]) #toelegnth - going back up   
    if turtle.xcor()*mirror<0:
        badnesscount=badnesscount+4
        return(badnesscount)
    # and the tail
    turtle.setheading(270)
    turtle.forward(scale*generikmon[19]) #talespine
    turtle.left(mirror*generikmon[20])        #tailtipA
    turtle.forward(scale*generikmon[21])   #tailtipD
    turtle.right(mirror*generikmon[20])
    turtle.forward(scale*generikmon[21])
    turtle.right(mirror*generikmon[20])
    turtle.forward(scale*generikmon[21])
    turtle.left(mirror*(generikmon[20])-90)
    turtle.forward(tailwidth)
    if turtle.xcor()*mirror<0:
        badnesscount=badnesscount+5
    return(badnesscount)

while (looper>0):
    mirror=1
    turtle.clear()
    turtle.home()
    turtle.setheading(90)
    randommon =randommonMaker()
    turtle.hideturtle()
    turtle.speed(0)
    looper=drawmonster(mirror, scale, randommon)
    print(looper)
    turtle.penup()
    turtle.home()
    turtle.pendown()
    turtle.setheading(90)
    mirror=-1
    drawmonster(mirror, scale, randommon)
