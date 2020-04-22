import turtle
import sys

def draw_picture(t, size):
    "Draw some squares"
    #Definir a cor
    t.pencolor("red")
    #Definir a largura do pincel
    t.pensize(3)
    for i in range (1,6):
        t.position()
        for j in range(4):
            t.forward(size*i)
            t.left(90)
            if j==3:
                #Parar de desenhar
                t.penup()
                #Ir para a posicao
                t.goto(-size*i/2, -size*i/2)
                #Voltar a desenhar
                t.pendown()


wn = turtle.Screen() # Set up the window and its attributes 
wn.bgcolor("lightgreen") 
wn.title("Victor meets a function")
victor = turtle.Turtle() 	# Create Victor
draw_picture(victor, 20)  # Call the function to draw some squares
wn.mainloop()
