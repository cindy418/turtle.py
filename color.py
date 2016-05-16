from turtle import *

def main():
    peacecolors = ("red3","#FF8888","orange","#FFB3FF","yellow",
                   "#FFFF77","seagreen4","#BBFF66","orchid4","#D28EFF","lightblue",
                   "royalblue1","#0088A8","dodgerblue4")

    reset()
    Screen()
    up()
    goto(-400,-195)
    width(30)
    bgcolor("#CCEEFF")
	
    for pcolor in peacecolors:
        color(pcolor)
        down()
        forward(780)
        up()
        backward(780)
        left(90)
        forward(30)
        right(90)

    width(10)
    color("white")
    goto(200,-200)
  
    down()
    circle(130)
    circle(120)
    circle(110)
    circle(100)
    circle(90)
    circle(80)
    circle(70)
    circle(60)
    circle(50)
    circle(40)
    circle(30)
    circle(20)	
    up()
    
    backward(400)
    down()
    circle(90)
    circle(80)
    circle(70)
    circle(60)
    circle(50)
    circle(40)
    circle(30)
    circle(20)	
    up()

    forward(180)
    left(90)
    forward(200)
    right(90)
    	
    down()
    circle(70)
    circle(60)
    circle(50)
    left(90)
    forward(100)
    up()
    left(180)
    forward(50)
    right(45)
    down()
    forward(50)
    up()
    backward(50)
    left(90)
    down()
    forward(50)	
    up()
   
    goto(0,300)
    return "Done!"

if __name__ == "__main__":
    main()
    mainloop()
