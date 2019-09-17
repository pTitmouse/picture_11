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

#машинка
#крыша 
penColor(100,0,100)
penSize(2)
brushColor(100,0,100)

rectangle(250 ,400 ,400, 450)
#корпус
penColor(100,0,100)
penSize(2)
brushColor(100,0,100)

rectangle(200 ,450 ,450, 520)


run()
