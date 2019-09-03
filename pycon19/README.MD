What this workshop is about:

1) playing with some working code, breaking it, fixing it and playing some more. 
2) it is not about teaching you all of python in 60-90min. HOWEVER, we will use libraries, define custom functions, store data in dictionaries and lists, use loops and if statements and look at different types of output. It actually covers a lot.
3) it is not a treatise on using evoltionary techniques on engineering structual problems (Pete Debney has already written that)
https://www.istructe.org/journal/volumes/volume-94-(2016)/issue-3/an-introduction-to-engineering-optimisation-method/

# Principals: 
Like baking, or painting, coding is a craft. Anyone can do it, and practice makes you better
Documentation is like lunch. Even a small bit in a rush is much much better then skipping it
Everyone around is interested and a beginner who is learning quickly. This means if you are stuck, they might know that bit! ask!
In fact, pairing up is a standard professional programming technique!
Unlike engineering, there are huge and fantastic help guides online. Try and visit stackoverflow at least once this session.

example: https://stackoverflow.com/questions/29003604/produce-overlapping-triangles-using-python-turtle
link to the turtle documentation: https://docs.python.org/3/library/turtle.html


# First Program: 

Open Ananconda, Open spyder.
Type the below into the main window (on the left). Then click the Green play button on the top ribbon. something should appear on the bottom right. Python is CaSe SenSitiVe

    # my first program comment
      print("Hello world!")


# Five Minutes Later. try this:

    import turtle

    turtle.forward(50)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forwards(50)
    print("finished!")

why does this code not run? Hints: whitespace/indentation matters in python, and I'm dyslexic
As well as the 'finished' there should also be a little popup window 

# Five Minutes later:
got to here https://github.com/cromlyngames/stos-valley/new/master/pycon19
and download and open or copy and past the Turtle_mon.py program into spyder and play it. What does it do?

Can you draw on paper the high level flowchart of the program? What functions get called in what order? 
What does commeting/uncommenting (using #) on line 99 do?
If you want it to mutate faster, what should you change?

# Ok, so grab the paper and let's draw yourself a thing. Symetrical lets you reuse more code (30min+)
(I'd recommend keeping it simplish to start with, less typing later. This just gives us a data set to experiment on, and 
Label each length with a name, label each angle with a name, grab a ruler and protractor and start measuring (or eyeball it!)

Now you need to update two functions. The one that sets the dictionary of lengths and angles, and the function that actually draws it. The dictionary is more effort to make and use to draw with then a list, but it is much easier to do evaluations with.


# Now add an evaluation function based on your dictionary and your thing.
Examples might be:
    RunningAwayScore = LegLength + EarSize
    CatchingFliesScore = EyeDistance + MouthSize + ToungeSize
    BeingAVampireScore = TeethLength - ToothtipA  #long sharp teeth
    SurvivingHibertation = BMIratio + WaistL + Fur Length
    CuteScore = Eyesize + DimpleSize - FrownA

