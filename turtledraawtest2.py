import turtle
import random
from tkinter import *

mirror=1       #used to reflect the turtle
scale =100  #used to scale the size of the monster
looper=1    #if 0 then program will complete
population =1 #looper 

testingdetail = { 'expansionslot': 0,
              'eyeratio': 0.5,   'frownA': 10,     'eyesize': 0.9,
              'nosesize': 0.5,   'mouthsize': 0.3,  
            }
  
testingmon ={ 'detail0':testingdetail,
              'crownD':0.4,
              'ear1A':90,       'ear2D':0.15,   'ear3A':45,       'ear4A':90, 'ear5A':45, 'ear6D':0.1,   #ear1A,ear2D,ear3A,ear4A,ear5A,ear5D,
              'cheekD':0.2,     'jawlineA':60,  'shoulderD':0.17,               #cheekD,jawlineA,shoulderD,
              'shoulderA':60,   'thighD':0.3,   'elbowA':10,      'shinD':0.3,            #shoulderA, thighD, elbowA, shinD
              'NumofToes':3,    'frontbackratio':0.75, 'toelengthD':0.12,               #NumOfToes, frontbackratio, toelengthD, 
              'tailbodyratio':0.1, 'tailspineD':0.5, 'tailtipA':80, 'tailtipD': 0.1           #tailbodywidthratio, tailspineD, tailtipA, tailtipD
              }



def randommonMaker():
    randomdetail = { 'expansionslot': 0,
                      'eyeratio': random.random(),   'frownA': random.randint(10, 70),     'eyesize': random.random()*1.5,
                      'nosesize': random.random(),   'mouthsize': random.random()*0.6,  
                    }

    randommon = { 'detail0':randomdetail,
                  'crownD':random.random()*0.8,
                  'ear1A': random.randint(45, 135),     'ear2D':random.random()*0.3,        'ear3A':random.randint(15, 75),       
                  'ear4A':random.randint(45, 135),      'ear5A':random.randint(15, 75),     'ear6D':random.random()*0.2,   #ear1A,ear2D,ear3A,ear4A,ear5A,ear5D,
                  'cheekD':random.random()*0.4,         'jawlineA':random.randint(10, 90),  'shoulderD':random.random()*0.34,               #cheekD,jawlineA,shoulderD,
                  'shoulderA':random.randint(30, 90),   'thighD':random.random()*0.6,       'elbowA':random.randint(5, 20),      'shinD':random.random()*0.6,            #shoulderA, thighD, elbowA, shinD
                  'NumofToes':random.randint(1, 5),     'frontbackratio':random.random()*0.75, 'toelengthD':random.random()*0.24,               #NumOfToes, frontbackratio, toelengthD, 
                  'tailbodyratio':random.random()*0.2,  'tailspineD':random.random()*1.0,   'tailtipA':random.randint(1, 89), 'tailtipD': random.random()*0.2            #tailbodywidthratio, tailspineD, tailtipA, tailtipD
                  }
    return(randommon)

def drawmonster(mirror, scale, generikmon):
    #for i in range(25):
    #      print(generikmon[i], i)
    badnesscount=0
    turtle.right(mirror*90)                 #requires turtle to be facing upwards       
    turtle.forward(scale*generikmon['crownD'])  #crownD
    turtle.left(mirror*generikmon['ear1A'])     #ear1A
    turtle.forward(scale*generikmon['ear2D'])  #ear2D
    turtle.right(mirror*generikmon['ear3A'])    #ear3A
    turtle.forward(scale*generikmon['ear2D'])  #ear2D
    turtle.right(mirror*generikmon['ear4A'])    #ear4A
    turtle.forward(scale*generikmon['ear6D'])  #ear6D
    turtle.right(mirror*generikmon['ear5A'])    #ear5A
    turtle.forward(scale*generikmon['ear6D'])  #ear5D
    #into the cheek
    turtle.setheading(270)         #fixed
    turtle.forward(scale*generikmon['cheekD'])  #cheekD
    if turtle.xcor()*mirror<0:
        badnesscount=badnesscount+1
        return(badnesscount)
    if turtle.ycor()>0:
        badnesscount=badnesscount+2
        return(badnesscount)
    #along the jaw and then the shoulder
    turtle.left(mirror*generikmon['jawlineA'])     #jawlineA
    turtle.forward(scale*generikmon['shoulderD']) #shoulderD
    turtle.right(mirror*(180-generikmon['jawlineA']))
    turtle.forward(scale*generikmon['shoulderD']*2)
    if turtle.xcor()*mirror<0:
        badnesscount=badnesscount+3
        return(badnesscount)
    if turtle.ycor()>0:
        badnesscount=badnesscount+2
        return(badnesscount)
    #down the arm
    turtle.left(mirror*generikmon['shoulderA'])    #shoulderA
    turtle.forward(scale*generikmon['thighD']) #thighD
    turtle.left(mirror*generikmon['elbowA'])    #elbowA
    turtle.forward(scale*generikmon['shinD'])#shinD
    # into the toes!
    NumofToes = generikmon['NumofToes']
    fullwidth= turtle.xcor()
    tailwidth= fullwidth*generikmon['tailbodyratio'] #talibodywidthratio,
    pawswidth= fullwidth-tailwidth
    frontpawwidth=pawswidth*generikmon['frontbackratio'] #fronttobackratio
    toewidth=frontpawwidth/(NumofToes)
    if turtle.ycor()>0:
        badnesscount=badnesscount+2
        return(badnesscount)
    for i in range(NumofToes):
        turtle.setheading(270)
        turtle.forward(scale*generikmon['toelengthD'])#toelengthD
        turtle.right(mirror*90)
        turtle.forward(mirror*toewidth)  #mirror required here since xcord is negative on second hlaf
        turtle.right(mirror*90)
        turtle.forward(scale*generikmon['toelengthD']) #toelegnth - going back up               
      #into the rear toes. # all lengths scaled by generikmon[16] = frontotbackratio
    toewidth=(pawswidth-frontpawwidth)/NumofToes  #redefines toe width for backpaws.
    for i in range(NumofToes):
        turtle.setheading(270)
        turtle.forward(scale*generikmon['frontbackratio']*generikmon['toelengthD'])#toelengthD
        turtle.right(mirror*90)
        turtle.forward(mirror*toewidth)
        turtle.right(mirror*90)
        turtle.forward(scale*generikmon['frontbackratio']*generikmon['toelengthD']) #toelegnth - going back up   
    if turtle.xcor()*mirror<0:
        badnesscount=badnesscount+4
        return(badnesscount)
    # and the tail
    turtle.setheading(270)
    turtle.forward(scale*generikmon['tailspineD']) #talespine
    turtle.left(mirror*generikmon['tailtipA'])        #tailtipA
    turtle.forward(scale*generikmon['tailtipD'])   #tailtipD
    turtle.right(mirror*generikmon['tailtipA'])
    turtle.forward(scale*generikmon['tailtipD'])
    turtle.right(mirror*generikmon['tailtipA'])
    turtle.forward(scale*generikmon['tailtipD'])
    turtle.left(mirror*(generikmon['tailtipA'])-90)
    turtle.forward(tailwidth)
    drawmonsterdetails(mirror,scale,randommon) #ADD the details
   # looper=drawmonsterdetails(mirror,scale,testingmon) #ADD the details
    return(badnesscount)
    
def drawmonsterdetails(mirror, scale, generikmon):
    detailsbit = generikmon['detail0']
      #for i in range(25):
       # print(generikmon[i], i)
    badnesscount=0
    ### draw the eyes
    turtle.penup()
    turtle.home()
   # print(turtle.xcor(),turtle.ycor())
    turtle.setheading(90)
    turtle.right(mirror*90)                 #requires turtle to be facing upwards       
    turtle.forward(scale*generikmon['crownD']*detailsbit['eyeratio']) #crownD, #eyeratio
    turtle.setheading(270)
    turtle.forward(scale*generikmon['cheekD']*(1-detailsbit['eyeratio'])) #cheekD, #eyeratio
    turtle.shape("circle")
    turtle.resizemode("user")
    turtle.shapesize(detailsbit['eyesize'],detailsbit['eyesize']*detailsbit['eyeratio']*4,1)
   # print(turtle.shapesize())
    turtle.tilt(mirror*detailsbit['frownA'])
    turtle.stamp()
    turtle.tilt(-1*mirror*detailsbit['frownA']) #takes the tilt off the turtle to avoid later confusion
    turtle.shapesize(1,1,1)             #takes off the eye size, i think.
    ### draw the nose
    turtle.penup()
    turtle.home()
    turtle.setheading(270)
    turtle.forward(scale*generikmon['cheekD']) #cheekD
    turtle.shape("triangle")
    turtle.shapesize(detailsbit['nosesize'],detailsbit['nosesize'],1)
    turtle.stamp()
    #and from the nose, the mouth
    turtle.pendown()
    turtle.forward(scale*generikmon['shoulderD']*detailsbit['nosesize']+detailsbit['nosesize']) #shouldD below the nose
    turtle.left(mirror*90)
    turtle.forward(scale*generikmon['crownD']*detailsbit['mouthsize']) #crownD   #width of mouth
    turtle.penup()
    turtle.home()
    return()



##########################################
while (population < 10):
   # print(population)
    looper=1
    while (looper>0):    #will keep drawing monsters until a good drawing achieved
        mirror=1
        turtle.penup()
        turtle.home()
        turtle.clear()
        turtle.setheading(90) #sets drawing canvas up
        turtle.hideturtle()
        turtle.speed(10)
        turtle.pendown()
        
        randommon =randommonMaker()
       # looper=drawmonster(mirror, scale, testingmon)
        looper=drawmonster(mirror, scale, randommon) #if badness occurs, looper=/= 0
        
        #print(looper)
        turtle.penup()
        turtle.home()
        turtle.pendown()
        turtle.setheading(90)
        mirror=-1
        drawmonster(mirror, scale, randommon)  #draws second half of monster

   # print("made")
    ts = turtle.getscreen()
    filenamer = str(population)  #turns population iteration into a string for filenameig
    filenamerEPS = filenamer+".eps"
    #print("filename =")
    ps=ts.getcanvas().postscript(file=filenamerEPS)
   # im=Image.open(io.BytesIO(ps.encode('utf-8')))
  #  im=im.resize((2560.1600), Image.ANTIALIAS)
   # quality_val=95
  #  sharp = ImageEnhance.Sharpness(im)
  #  sharp.enhance(2.0).save(filenamer+ ".png", 'PNG')
 #   print (filenamer)
    population=population+1
    print("pop= ", population)
