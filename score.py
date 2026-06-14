from turtle import Turtle

class Score(Turtle):
    """
    The Score Class That Inherits From Turtle Class From turtle module

    Args:
        Turtle (_type_): _description_
    """
    
    def __init__(self):
        """
        Initialize Magic Method
        """
        
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.r = 0
        self.l = 0
        self.display()
        
    def display(self):
        """
        Display Method
        """
        
        self.clear()
        self.goto(100, 230)
        self.write(self.r, align = "center", font = ("courier", 40, "bold"))
        self.goto(-100, 230)
        self.write(self.l, align = "center", font = ("courier", 40, "bold"))
        
    def l_point(self):
        """
        A Method That Increases Points For Left Paddle
        """
        
        self.l += 1
        self.display()
        
    def r_point(self):
        """
        A Method That Increases Points For Right Paddle
        """
        
        self.r += 1
        self.display()