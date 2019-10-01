# picture_11
#картинка нa python
from graph import *
windowSize(600, 1200)
#небо
penColor(0,10,10)
penSize(2)
brushColor(0,10,10)

rectangle(3,3 ,500, 400)


#земля
penColor(0,200,200)
penSize(2)
brushColor(0,200,200)

rectangle(3,400 ,500, 900)


#левый верхний 1
penColor(0,100,200)
penSize(2)
brushColor(0,100,200)
A=rectangle(a+10,10 ,a+100, 400)

#левый верхний 2
penColor(0,150,200)
penSize(2)
brushColor(0,150,200)
B=rectangle(a+120,20 ,a+210, 410)

#левый нижний
penColor(0,150,100)
penSize(2)
brushColor(0,150,100)
C=rectangle(a+90,90 ,a+180, 460)

#правый верхний
penColor(0,100,100)
penSize(2)
brushColor(0,100,100)
D=rectangle(a+400,10 ,a+490, 410)

#правый нижний
penColor(0,200,100)
penSize(2)
brushColor(0,200,100)
E=rectangle(a+310 ,50 ,a+400, 460)

#овальчики
penColor(100,100,10)
penSize(2)
brushColor(100,100,0)

c=canvas()
c.create_oval(150,5,590,100)
c.create_oval(5,40,300,130)
c.create_oval(100,150,590,250)
c.create_oval(5,300,200,360)
c.create_oval(10,420,130,470)
c.create_oval(10,480,130,530)
c.create_oval(-30,450,600,650)

#машинка
##крыша 
penColor(100,0,100)
penSize(2)
brushColor(100,0,100)

l=rectangle(250 ,450 ,400, 500)

##корпус
penColor(100,0,100)
penSize(2)
brushColor(100 ,0 ,100)

h=rectangle(200 ,500 ,450 ,550)
## окошки
penColor(0,0,10)
penSize(2)
brushColor(0,0,10)

p=rectangle(260 ,460 ,315, 500)

penColor(0,0,10)
penSize(2)
brushColor(0,0,10)

f=rectangle(335 ,460 ,390, 500)
##колёса
penColor(0,0,10)
penSize(2)
brushColor(0,0,10)

d=circle(250 , 540 , 20)
a=circle(400,540,20)

#animation
def update():
  moveObjectBy(d, 5, 0)
  moveObjectBy(a, 5, 0)
  moveObjectBy(f, 5, 0)
  moveObjectBy(p, 5, 0)
  moveObjectBy(h, 5, 0)
  moveObjectBy(l, 5, 0)
  moveObjectBy(A, -5, 0)
  moveObjectBy(B, -5, 0)
  moveObjectBy(C, -5, 0)
  moveObjectBy(D, -5, 0)
  moveObjectBy(E, -5, 0)
  
def keyPressed(event):
  if event.keycode == VK_ESCAPE:
    close()




onKey(keyPressed)
onTimer(update, 50)


  

run()
