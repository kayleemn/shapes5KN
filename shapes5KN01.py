#shapes5KN.py- Kaylee N
from graphics import*
winX = 500
winY = 500

#Window
shapesWin = GraphWin("Shapes 5" , 500, 500)
shapesWin.setCoords(0,0,500,500)

#orange triangle 
orgTri = Polygon(Point(30,10), Point(75 ,60), Point(100,10))
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
blDia = Polygon(Point(winX/2-50,winY/2), Point(winX/2,winY/2+50), Point(winX/2+50,winY/2), Point(winX/2,winY/2-50))
blDia.setFill(color_rgb(0,0,255))
blDia.draw(shapesWin)

shapesWin.getMouse()
shapesWin.close()








