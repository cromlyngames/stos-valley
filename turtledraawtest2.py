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
              'numofToes':3,    'frontbackratio':0.75, 'toelengthD':0.12,               #numofToes, frontbackratio, toelengthD, 
              'tailbodyratio':0.1, 'tailspineD':0.5, 'tailtipA':80, 'tailtipD': 0.1           #tailbodywidthratio, tailspineD, tailtipA, tailtipD
              }



def randommonMaker():
    randomdetail = { 'expansionslot': 0,
                      'eyeratio': random.random(),   'frownA': random.randint(10, 70),     'eyesize': random.random(),
                      'nosesize': random.random(),   'mouthsize': random.random()*0.6,
                      'numofTeeth': random.randint(1, 5), 'fanglength':random.random(), 'fangtipratio':random.random(),
                      'clawlength':random.random()*0.2
                    }

    randommon = { 'detail0':randomdetail,
                  'crownD':random.random()*0.8,
                  'ear1A': random.randint(45, 135),     'ear2D':random.random()*0.3,        'ear3A':random.randint(15, 75),       
                  'ear4A':random.randint(45, 135),      'ear5A':random.randint(15, 75),     'ear6D':random.random()*0.2,   #ear1A,ear2D,ear3A,ear4A,ear5A,ear5D,
                  'cheekD':random.random()*0.4,         'jawlineA':random.randint(10, 90),  'shoulderD':random.random()*0.34,               #cheekD,jawlineA,shoulderD,
                  'shoulderA':random.randint(30, 90),   'thighD':random.random()*0.6,       'elbowA':random.randint(5, 20),      'shinD':random.random()*0.6,            #shoulderA, thighD, elbowA, shinD
                  'numofToes':random.randint(1, 5),     'frontbackratio':random.random()*0.75, 'toelengthD':random.random()*0.24,               #numofToes, frontbackratio, toelengthD, 
                  'tailbodyratio':random.random()*0.2,  'tailspineD':random.random()*1.0,   'tailtipA':random.randint(1, 89), 'tailtipD': random.random()*0.2            #tailbodywidthratio, tailspineD, tailtipA, tailtipD
                  }
    return(randommon)


####
def mutatemonster(scale, parentmon):
    badness =2
    while badness>0:
        childmon=parentmon
        childdetails = childmon['detail0']
        for ikey,ival in childdetails.items():
            childdetails[ikey] =childdetails[ikey]*(1+(random.random()+random.random()+random.random()-1.5)/10)
            
        childdetails['numofTeeth']=int(childdetails['numofTeeth'])  #need a integer number of teeth!
        if childdetails['numofTeeth'] < 0:
            childdetails['numofTeeth']=childdetails['numofTeeth']+1
        for ikey,ival in childmon.items():
            if ikey =='detail0': pass #do nothing
            else:
                childmon[ikey] = childmon[ikey]*(1+(random.random()+random.random()+random.random()-1.5)/10)
        childmon['numofToes']=int(childmon['numofToes']) #need a integer number of toes!
        if childmon['numofToes'] == 0:
            childmon['numofToes']=childmon['numofToes']+1
        print('Drawing possible child')
        badness =drawmonster(scale, childmon)  # uses the drawing test to see if new monster good, if not repeats the mutation.
        print ('badness =', badness)
    print('child accepted')
    return(childmon)

def drawmonster(scale,generikmon):
    print('drawing...')
    looper=1
    mirror=1
    turtle.penup()
    turtle.home()
    turtle.clear()
    turtle.setheading(90) #sets drawing canvas up
    turtle.hideturtle()
    turtle.speed(10)
    turtle.pendown()
            
    # looper=drawmonster(mirror, scale, testingmon)

    looper=drawhalfmonster(mirror, scale, randommon) #if badness occurs, looper=/= 0
    if looper==0:
        turtle.penup()
        turtle.home()
        turtle.pendown()
        turtle.setheading(90)
        mirror=-1
        drawhalfmonster(mirror, scale, randommon)  #draws second half of monster
    return(looper)
    
       

    
####
def drawhalfmonster(mirror, scale, generikmon):
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
        badnesscount=badnesscount+1
        return(badnesscount)
    #along the jaw and then the shoulder
    turtle.left(mirror*generikmon['jawlineA'])     #jawlineA
    turtle.forward(scale*generikmon['shoulderD']) #shoulderD
    turtle.right(mirror*(180-generikmon['jawlineA']))
    turtle.forward(scale*generikmon['shoulderD']*2)
    if turtle.xcor()*mirror<0:
        badnesscount=badnesscount+1
        return(badnesscount)
    if turtle.ycor()>0:
        badnesscount=badnesscount+1
        return(badnesscount)
    #down the arm
    turtle.left(mirror*generikmon['shoulderA'])    #shoulderA
    turtle.forward(scale*generikmon['thighD']) #thighD
    turtle.left(mirror*generikmon['elbowA'])    #elbowA
    turtle.forward(scale*generikmon['shinD'])#shinD
    # into the toes!
    startoftoes=turtle.pos()
    turtle.setheading(270)
    turtle.forward(scale*generikmon['toelengthD'])#toelengthD
    if turtle.xcor()*mirror<0:
        badnesscount=badnesscount+1
        return(badnesscount)
    #front paw
    fullwidth= turtle.xcor()
    tailwidth= fullwidth*generikmon['tailbodyratio'] #talibodywidthratio,
    pawswidth= fullwidth-tailwidth
    frontpawwidth=pawswidth*generikmon['frontbackratio'] #fronttobackratio
    backpawwidth=pawswidth-frontpawwidth
    
    turtle.right(mirror*90)
    turtle.forward(mirror*frontpawwidth) #draws front foot 'block'
    turtle.setheading(90)
    turtle.forward(scale*generikmon['toelengthD'])#toelengthD
    #line between front and back
    turtle.left(mirror*generikmon['elbowA'])
    turtle.forward(0.5*scale*generikmon['shinD'])
    turtle.forward(0.5*scale*generikmon['thighD'])
    turtle.forward(-0.5*scale*generikmon['thighD']) # now reverse back along that line
    turtle.left(mirror*-0.5*generikmon['elbowA'])
    turtle.forward(-0.5*scale*generikmon['shinD'])
    #rearpaw
    turtle.setheading(270)
    turtle.forward(scale*generikmon['frontbackratio']*generikmon['toelengthD'])#toelengthD
    turtle.right(mirror*90)
    turtle.forward(mirror*backpawwidth)
    turtle.right(mirror*90)
    turtle.forward(scale*generikmon['frontbackratio']*generikmon['toelengthD'])
    
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
    drawmonsterdetails(mirror,scale,randommon, startoftoes) #ADD the details
   # looper=drawmonsterdetails(mirror,scale,testingmon) #ADD the details
    return(badnesscount)
    
def drawmonsterdetails(mirror, scale, generikmon,startoftoes):
    detailsbit = generikmon['detail0']
    turtle.penup()
    turtle.goto(startoftoes)
    turtle.pendown()
    ### draw the toes webs and claws    
    numofToes = generikmon['numofToes']
    fullwidth= turtle.xcor()
    tailwidth= fullwidth*generikmon['tailbodyratio'] #talibodywidthratio,
    pawswidth= fullwidth-tailwidth
    frontpawwidth=pawswidth*generikmon['frontbackratio'] #fronttobackratio
    toewidth=frontpawwidth/(numofToes)
    for i in range(numofToes):
        turtle.setheading(270)
        turtle.forward(scale*generikmon['toelengthD'])#toelengthD
        turtle.right(mirror*90)
        turtle.forward(mirror*toewidth*0.1)  #mirror required here since xcord is negative on second hlaf
        # start claw layout calcs
        xclawstart = turtle.xcor()
        xclawtip = xclawstart - toewidth*0.4
        xclawend = xclawtip - toewidth*0.4
        yclawstart = turtle.ycor()
        yclawtip = yclawstart-scale*detailsbit['clawlength']
        yclawend = yclawstart
        #draw claw (it's already at the start)
        turtle.goto(xclawtip, yclawtip)
        turtle.goto(xclawend, yclawend)     
        turtle.forward(mirror*toewidth*0.1)  #mirror required here since xcord is negative on second hlaf
        turtle.right(mirror*90)
        turtle.forward(scale*generikmon['toelengthD']) #toelegnth - going back up               
      #into the rear toes. # all lengths scaled by generikmon[16] = frontotbackratio
    toewidth=(pawswidth-frontpawwidth)/numofToes  #redefines toe width for backpaws.
    for i in range(numofToes):
        turtle.setheading(270)
        turtle.forward(scale*generikmon['frontbackratio']*generikmon['toelengthD'])#toelengthD
        turtle.right(mirror*90)
        turtle.forward(mirror*toewidth*0.1)  #mirror required here since xcord is negative on second hlaf
        # start claw layout calcs
        xclawstart = turtle.xcor()
        xclawtip = xclawstart - toewidth*0.4
        xclawend = xclawtip - toewidth*0.4
        yclawstart = turtle.ycor()
        yclawtip = yclawstart-scale*detailsbit['clawlength']
        yclawend = yclawstart
        #draw claw (it's already at the start)
        turtle.goto(xclawtip, yclawtip)
        turtle.goto(xclawend, yclawend)     
        turtle.forward(mirror*toewidth*0.1)  #mirror required here since xcord is negative on second hlaf
        turtle.right(mirror*90)
        turtle.forward(scale*generikmon['frontbackratio']*generikmon['toelengthD']) #toelegnth - going back up
        

    ### draw the ears
    turtle.penup()
    turtle.home()
    turtle.setheading(90)
    turtle.right(mirror*90)                 #requires turtle to be facing upwards       
    turtle.forward(scale*generikmon['crownD'])  #crownD follow crown line exactly
    turtle.left(mirror*generikmon['ear1A'])     #ear1A
    turtle.right(mirror*90)     #turns back into shape.
    turtle.forward(scale*(generikmon['ear2D']*0.1+0.01))
    startoftheear = turtle.pos()
    turtle.pendown()
        # start actually drawing
    turtle.setheading(90)
    turtle.right(mirror*90)
    turtle.left(mirror*generikmon['ear1A'])     #ear1A
    turtle.forward(scale*generikmon['ear2D']*0.8)  #ear2D
    turtle.right(mirror*generikmon['ear3A'])    #ear3A
    turtle.forward(scale*generikmon['ear2D']*0.8)  #ear2D
    turtle.right(mirror*generikmon['ear4A'])    #ear4A
    turtle.forward(scale*generikmon['ear6D']*0.7)  #ear6D
    turtle.right(mirror*generikmon['ear5A'])    #ear5A
    turtle.forward(scale*generikmon['ear6D']*0.7)  #ear5D
    turtle.goto(startoftheear)                      #finishs the ear off.
    ### draw the eyes (stamped over ears if needed)
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

def evalmonster(generikmon):
    detailsbit = generikmon['detail0']
    senseEval = 1/4*(detailsbit['eyesize'] +detailsbit['nosesize'] + generikmon['ear2D'] + generikmon['ear6D'])
    hidingEval = 1- 1/5*(generikmon['crownD']+generikmon['cheekD']+generikmon['shoulderD']+generikmon['thighD']+generikmon['shinD'])
    strengthEval = 1/3*(generikmon['shoulderD']+generikmon['frontbackratio'] + (1- generikmon['tailbodyratio']))
    speedFOREST = 1/5*(detailsbit['clawlength'] +generikmon['tailspineD'] + generikmon['toelengthD']+generikmon['thighD']+generikmon['shinD'])
    sprinterelbow = 1- ((90-generikmon['elbowA'])/100)**2  #should be larger as the elbow gets straighter - ie ostrich not lizard
    speedMEADOW = 1/4*(generikmon['shinD']+generikmon['thighD']+1/generikmon['numofToes']+sprinterelbow)
    speedSWAMP = 1/3*(generikmon['tailtipD']+(1-generikmon['frontbackratio'])+generikmon['tailbodyratio'])
    preybonus = 1/3*(detailsbit['eyeratio']+generikmon['crownD']+detailsbit['fangtipratio'])
    predbonus = 1/3*(detailsbit['clawlength']+detailsbit['fanglength']+(1-detailsbit['fangtipratio']))
    metabolisim = 1-1/(detailsbit['eyesize']+detailsbit['nosesize']+detailsbit['clawlength']+detailsbit['fanglength']
                      +generikmon['crownD']+generikmon['ear2D']+generikmon['ear6D']+generikmon['cheekD']
                      +generikmon['shoulderD']+generikmon['thighD']+generikmon['shinD']+generikmon['toelengthD']
                      +generikmon['tailspineD']+generikmon['tailtipD'])
    evalresults = { 'senseEval': senseEval, 'hidingEval': hidingEval, 'stregnthEval': strengthEval,
                    'speedFOREST':speedFOREST, 'speedMEADOW':speedMEADOW, 'speedSWAMP':speedSWAMP,
                    'preybonus':preybonus, 'predbonus':predbonus, 'metabolisim':metabolisim}
    #print(evalresults)
                    
    return(evalresults)                 

##########################################
populationtotal = int(input("how many monsters?: "))
generationtotal = int(input("how many generations?: "))
focus = str(input("senseEval, hidingEval, strengthEval, speedFOREST, speedMEADOW, speedSWAMP, preybonus, predbonus, metabolisim ?'"))
populationtotal = populationtotal+1  #needed to make the loop work properly. poptotal = 2 gives one monster
while (population < populationtotal):
   # print(population)
        badness=1

        while badness>0:
            randommon =randommonMaker()
            badness=drawmonster(scale, randommon)   # draws inital monster

        
        generation = 0 #resets generation loop counter
        while (generation < generationtotal):
            childmon = mutatemonster(scale, randommon)  # creates new child of that monster

            ts = turtle.getscreen()
            filenamer = str(population)+'_'+str(generation)  #turns population iteration into a string for filenameig
            filenamerEPS = filenamer+".eps"
            ps=ts.getcanvas().postscript(file=filenamerEPS)
            
            parentresults = evalmonster(randommon)
            childresults = evalmonster(childmon)
            if parentresults[focus]>childresults[focus]:
                childmon = mutatemonster(scale, randommon)
            else:
                childmon = mutatemonster(scale, childmon) #generates new monster from whichever one is 'fitter'
                
            generation=generation+1
        print(childmon)
        population=population+1    
        print("pop= ", population)

    
