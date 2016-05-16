from turtle import *

def yin(radius, color1, color2, rig, lef):
    color("#EEFFBB")
    goto(rig, lef)
    bgcolor("#EEFFBB")
    width(3)
    color("#77DDFF", color1)
    down()
    begin_fill()
    circle(radius/2., 180)
    circle(radius, 180)
    left(180)
    circle(-radius/2., 180)
    end_fill()
    left(90)
    up()
    forward(radius*0.35)
    right(90)
    down()
    color(color1, color2)
    begin_fill()
    circle(radius*0.15)
    end_fill()
    left(90)
    up()
    backward(radius*0.35)
    down()
    left(90)
    up()
	
def yang(radius, color1, color2, rig, lef):
    color("#EEFFBB")
    goto(rig, lef)
    bgcolor("#EEFFBB")
    width(3)
    color("#77DDFF", color1)
    down()
    begin_fill()
    circle(-radius/2., 180)
    circle(-radius, 180)
    left(180)
    circle(radius/2., 180)
    end_fill()
    left(90)
    up()
    forward(-radius*0.7)
    right(90)
    down()
    color(color1, color2)
    begin_fill()
    circle(radius*0.15)
    end_fill()
    left(90)
    up()
    backward(radius*0.7)
    down()
    left(90)
    up()

def form():
    width(8)
    color("#FFB3FF")
    goto(0,0)
    down()
    forward(200)
    up()
    backward(200)
    left(180)
    down()
    forward(200)
    up()
    right(90)
    down()
    forward(200)
    right(90)
    forward(400)
    right(90)
    forward(400)
    right(90)
    forward(400)
    right(90)
    forward(200)
    up()
    forward(200)
    right(90)
    forward(200)
    right(90)
    down()
    forward(400)
    up()

def main():
    reset()
    yin(100, "#77DDFF", "white", -100,100)
    yin(100, "white", "#77DDFF", -100,100)
	
    yin(100, "#77DDFF", "white", 100,100)
    yin(100, "white", "#77DDFF", 100,100)
	
    yang(100, "#77DDFF", "white", -100,-100)
    yang(100, "white", "#77DDFF", -100,-100)
	
    yang(100, "#77DDFF", "white", 100,-100)
    yang(100, "white", "#77DDFF", 100,-100)
	
    form()
    ht()
    return "Done!"

if __name__ == '__main__':
    main()
    mainloop()