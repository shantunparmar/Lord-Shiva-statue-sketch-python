from turtle import *

title("Har Har Mahadev")
setup(550, 750)
penup()
goto(-100, -80)
pendown()
bgcolor("#0a1640") 
fillcolor("orange")  
pencolor("white")
speed(0)  

def round_shape(s=20, f=200):
    begin_fill()
    for _ in range(2):
        forward(f)
        circle(s, 180)
    end_fill()

round_shape()
