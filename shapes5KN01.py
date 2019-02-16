#shapes5KN.py- Kaylee N
from graphics.py import*

shapesWin = GraphWin("Shapes 5" , 500, 500)
shapesWin.setCoords(0,0,500,500)

#orange triangle 
orgTri = Polygon(Point(50,50), Point(75 ,100), Point(100,50))
orgTri.setFill("orange")
orgTri.draw(shapesWin)

#green square
gSq = Rectangle(Point(485,10),Point(435,60))
gSq.setFill(color_rgb(0,255,0))
gSq.draw(shapesWin)

#red oval
rOval = Oval(Point(490,490), Point(450,375))
rOval.setFill(color_rgb(255,0,0))
rOval.draw(shapesWin)

#purple circle
purCir = Circle(Point(75,440), 50)
purCir.setFill("purple")
purCir.draw(shapesWin)

#blue diamond
blDia = Polygon(Point(200,250), Point(250,300), Point(275,250), Point(250,200))
blDia.setFill(color_rgb(0,0,255))
blDia.draw(shapesWin)

shapesWin.getMouse()
shapesWin.close()








