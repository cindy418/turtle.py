from turtle import *

def colorful():
    colors = ("red3","#FF8888","orange","#FFB3FF","yellow",
              "#FFFF77","seagreen4","#BBFF66","orchid4","#D28EFF","lightblue",
              "royalblue1","#0088A8","dodgerblue4") #線條顏色

    reset() 
    Screen()
    up()
    goto(-400,-195)
    speed(10)	
    width(30)               
    bgcolor("#CCEEFF") #背景顏色 
	
    for pcolor in colors: #畫彩色線條
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
    circle(130) #第一個圈
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
    circle(90) #第二個圈
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
    circle(70) #第三個圖
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
   
def yin(radius, color1, color2, rig, lef): #第一種陰陽
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
	
def yang(radius, color1, color2, rig, lef): #第二種陰陽
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

def form(): #表格
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
	
def mouse(): #米奇
    left(90)
    goto(0,0)
    width(3)     
    color("black")
    down()        #臉
    begin_fill()
    circle(100)
    end_fill()
    up()
	
    goto(-105,140) #耳朵
    down()
    begin_fill()
    circle(50)
    end_fill()
    up()
    
    goto(105,140) #耳朵
    down()
    begin_fill()
    circle(50)
    end_fill()
    up()
	
    goto(0,130)  #臉部輪廓
    left(110)
    width(3)     
    color("floralwhite")
    down()
    circle(30,140) 
    up()

    goto(0,130)
    left(180)
    down()
    circle(-30,140) 
    up()
    
    goto(-70,70)
    right(90)
    down()
    circle(20,150) 
    up()

    goto(-70,70)
    left(86)
    down()
    forward(70)
    up()
    
    goto(72,70)
    right(100)
    down()
    circle(-20,150) 
    up()

    goto(72,70)
    right(80)
    down()
    forward(70)
    up()
    
    goto(-70,30)
    right(151)
    down()
    circle(100,90)
    up()
	
    goto(-30,60)  #眼睛
    down()
    begin_fill()
    circle(10)
    end_fill()
    up()
	
    goto(50,60)  #眼睛
    down()
    begin_fill()
    circle(10)
    end_fill()
    up()
	
    goto(9,30) #嘴巴
    down()
    begin_fill()
    circle(5)
    end_fill()
    up()

def main():
    reset()
    colorful()
    
    reset()
    yin(100, "#77DDFF", "white", -100,100) #第一個陰陽
    yin(100, "white", "#77DDFF", -100,100) 
	
    yin(100, "#77DDFF", "white", 100,100)  #第二個陰陽
    yin(100, "white", "#77DDFF", 100,100)
	
    yang(100, "#77DDFF", "white", -100,-100) #第三個陰陽
    yang(100, "white", "#77DDFF", -100,-100)
	
    yang(100, "#77DDFF", "white", 100,-100) #第四個陰陽
    yang(100, "white", "#77DDFF", 100,-100)
	
    form() #表格
    mouse() #米老鼠
    ht()
    return "Done!"

if __name__ == '__main__':
    main()
    mainloop()
