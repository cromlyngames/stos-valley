# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 12:18:40 2019

@author: Patrick.Barry
"""

import turtle
from random import randint as r_i

MUTATION_RATE = 20 # in x
MUTATE = 5 # x% change
turtle.colormode(255)
turtle.clear()
POPROW = 12  # 12 per popualtion
GENERATIONS = 5 

 #sets drawing canvas up

def fill_dna():
    dna =[]
    #fill the dna with random lengths and turns
    for i in range(0,100):
        x = r_i(-15,15)
        dna.append(x)
    return(dna)
    
def draw_dna(dna):    
    it = iter(dna)
    turtle.setheading(90)
    for v, a in zip(it, it):
        #print (v, a)
        turtle.forward(v)
        turtle.left(a)
    return()
    
def mutate_dna(dna):
    new_dna =[]
    for i in dna:
        test = r_i(1, MUTATION_RATE)
        if test == 1:
            x = i*MUTATE/100
        else:
            x = i
        new_dna.append(x)
    return(new_dna)

def splice_dna(dna1, dna2):
    new_dna = []
    for i in range(0, len(dna1)):
        test = r_i(1,2)
        if test ==1:
            x = dna1[i]
        else:
            x = dna2[i]
        new_dna.append(x)
    return(new_dna)
            

def draw_pop(population, ycord):
    turtle.penup()
    turtle.setpos(-100,ycord)
    turtle.pendown()
    turtle.pencolor(0,0,0)
    turtle.setheading(180)
    turtle.forward(400)
    
    for i in range(0, len(population)):
        startxcor = (200/POPROW)*i -100 
        turtle.penup()
        turtle.setpos(startxcor,ycord)
        turtle.pendown()
        red = r_i(1,255)
        green = r_i(1,255)
        blue = r_i(1,255)
        turtle.pencolor(red, green, blue )
        draw_dna(population[i])
    return()


### main
population =[]

### initiate popualtion
for i in range(0,POPROW):
    print(i)
    new_thing = fill_dna()
    population.append(new_thing)

### main loop
turtle.clear()


for i in range (0,GENERATIONS):
    ycord = (-200/GENERATIONS)*i +100
    draw_pop(population, ycord)
    male = int(input("parent 1: 1,2,3 ect"))-1 # to idnex to zero for first
    female = int(input("parent 2: 1,2,3"))-1 # to idnex to zero for first
    male_dna = population[male]
    female_dna = population[female]
    new_pop=[]
    for i2 in range(0,POPROW):
        print(i, i2)
        new_thing = splice_dna(male_dna, female_dna)
        new_thing = mutate_dna(new_thing)
        new_pop.append(new_thing)    
    population= new_pop
   
    
