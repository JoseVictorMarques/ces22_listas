import turtle
import sys
 
def draw_poly( t, n, sz):
    "Make turtle t draw a polygon of size"
    #Definir a cor
    t.pencolor("red")
    #Definir o largura do pincel
    t.pensize(5)
    #Desenhar o poligono
    for i in range(n):
        t.forward(sz)
        t.left(360/n)


wn = turtle.Screen() # Set up the window and its attributes 
wn.bgcolor("lightgreen") 
wn.title("Tess meets a function")
tess = turtle.Turtle() 	# Create Tess
draw_poly(tess,8, 50)  # Call the function to draw the poligon
wn.mainloop()
