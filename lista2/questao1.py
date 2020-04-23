import turtle
import sys

#turtle.setup(400,500)
wn= turtle.Screen()
wn.setup(400,500)
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
tess= turtle.Turtle()

def draw_housing():
    """ Draw a nice housing to hold the traffic lights """
    tess.pensize(3)
    tess.color("black", "darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40,180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()


draw_housing()
tess.penup()

tess.forward(40)
tess.left(90)
tess.forward(50)

tess.shape("circle")
tess.shapesize(3)
tess.fillcolor("green")

state_num = 0


def advance_state_machine():
    global state_num
    if state_num == 0:
        tess.forward(70)
        tess.fillcolor("orange")
        state_num=1
    elif state_num == 1:
        tess.forward(70)
        tess.fillcolor("red")
        state_num=2
    else:
        tess.back(140)
        tess.fillcolor("green")
        state_num =0



largura= tess.pensize()
def increase():
    global largura
    if largura < 20 :
        largura = largura + 1
    tess.width(largura)

def decrease():
    global largura
    if largura > 1:
        largura = largura -1
    tess.width(largura)


code_color= 0
def background():
    global code_color
    if code_color == 0:
        wn.bgcolor("lightgreen")
        code_color =1
    elif code_color== 1:
        wn.bgcolor("grey")
        code_color =2
    else:
        wn.bgcolor("purple")
        code_color=0


def blue():
    "Atributtes color blue"
    tess.fillcolor("blue")

def green():
    "Atributtes color green"
    tess.fillcolor("green")

def red():
    "Atributtes color red"
    tess.fillcolor("red")



wn.onkey(advance_state_machine, "space")
#MODIFICADO POR MIM
wn.onkey(increase,"+")
wn.onkey(decrease,"-")
wn.onkey(background,"c")
wn.onkey(blue,"b")
wn.onkey(green,"g")
wn.onkey(red,"r")
#FIM DA MODIFICAÇÃO
wn.listen()
wn.mainloop()