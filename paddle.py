from turtle import Turtle

class Paddle(Turtle):
    """
    The Paddle Class That Inherits From Turtle Class From turtle module

    Args:
        Turtle (_type_): _description_
    """
    
    def __init__(self, position):
        """
        Initialize Magic Method
        """
        
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(5, 1)
        self.penup()
        self.goto(position)
        
    def up(self):
        """
        Go Up
        """
        
        self.goto(self.xcor(), self.ycor()+40)
        
    def down(self):
        """
        Go Down
        """
        
        self.goto(self.xcor(), self.ycor()-40)