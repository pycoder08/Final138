from graphics import *

class Button:
    
    def __init__(self, win, center, width, height, label):
        w = width/2.0
        h = height/2.0

        x = center.getX()
        y = center.getY()

        self.xmin = x - w
        self.xmax = x + w

        self.ymin = y - h
        self.ymax = y + h

        self.rect = Rectangle(Point(self.xmin, self.ymin), Point(self.xmax, self.ymax))
        self.rect.setFill('lightgray')
        self.rect.draw(win)

        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()

    def activate(self):
        "Sets the button to be activated"
        self.label.setFill('black')
        self.active = True
    
    def deactivate(self):
        "Sets the button to be deactivated"
        self.label.setFill('darkgrey')
        self.active = False

    def clicked(self, p):
        "Checkes if the button has been clicked"
        return (self.active and
                (self.xmin <= p.getX() <= self.xmax) and
                (self.ymin <= p.getY() <= self.ymax))
    
