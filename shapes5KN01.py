#shapes5KN.py- Kaylee N
from graphics import*

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





