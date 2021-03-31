###
### http://anh.cs.luc.edu/handsonPythonTutorial/index.html
###

###
### http://anh.cs.luc.edu/python/hands-on/3.1/examples.zip
###

from graphics import *

### Instantiate Graphics Window
win = GraphWin('my window', 1200,700)

## Makes the window backgorund black
win.setBackground('black')

### Start your nested loops here

for x in range(5):

    for y in range(10):

        ### First pick a center point for the rectanlge
        pt = Point(30 + 100 * x/2, y * 50)

        # Then draw the Rectangle
        rect = Rectangle(Point(5, 5), pt)

        rect.setOutline('black')
        rect.setFill('blue')


        # Then render
        rect.draw(win)

### end your loop here

## Makes a message for the user 
message = Text(Point(win.getWidth()/2, 15), 'Click three points to draw a Triangle')

message.setSize(18)
message.draw(win)

## Has the user click three points to make a triangle
p1 = win.getMouse()
p1.draw(win)

p2 = win.getMouse()
p2.draw(win)

p3 = win.getMouse()
p3.draw(win)

vertices = [p1, p2, p3]
triangle = Polygon(vertices)
triangle.setFill('white')
triangle.setOutline('cyan')
triangle.setWidth(7)
triangle.draw(win)

## Informs the user that they can click anywhere to exit
message = Text(Point(win.getWidth()/2, win.getHeight() - 75 ), 'Click anywhere to Quit')

customColor = color_rgb(255, 100, 12)

message.setFill(customColor)
message.setSize(18)
message.draw(win)

# Wait for a mouse click to close the Graphics window
win.getMouse()
