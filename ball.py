from turtle import Turtle

class Ball (Turtle):
    """
    The Class Of Ball That Inherits From Turtle Class From turtle module

    Args:
        Turtle (_type_): _description_
    """
    
    def __init__(self):
        """
        Initialize Magic Method
        """
        super().__init__()
        self.color('White')
        self.shape('circle')
        self.penup()
        self.x = 10
        self.y = 10