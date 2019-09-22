# picture_11
картинка на python
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

rectangle(10,10 ,100, 400)

#левый верхний 2
penColor(0,150,200)
penSize(2)
brushColor(0,150,200)

rectangle(120,20 ,210, 410)

#левый нижний
penColor(0,150,100)
penSize(2)
brushColor(0,150,100)

rectangle(90,90 ,180, 460)

#правый верхний
penColor(0,100,100)
penSize(2)
brushColor(0,100,100)

rectangle(400,10 ,490, 410)

#правый нижний
penColor(0,200,100)
penSize(2)
brushColor(0,200,100)

rectangle(310 ,50 ,400, 460)


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

rectangle(250 ,450 ,400, 500)
##корпус
penColor(100,0,100)
penSize(2)
brushColor(100 ,0 ,100)

rectangle(200 ,500 ,450 ,550)
## окошки
penColor(0,0,10)
penSize(2)
brushColor(0,0,10)

rectangle(260 ,460 ,315, 500)

penColor(0,0,10)
penSize(2)
brushColor(0,0,10)

rectangle(335 ,460 ,390, 500)
##колёса
penColor(0,0,10)
penSize(2)
brushColor(0,0,10)

circle(250 , 540 , 20)
circle(400,540,20)

#animation



onKey(keyPressed)
onTimer(update, 50)   

run()
