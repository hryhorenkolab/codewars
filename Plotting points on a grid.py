class Grid():
  """Make a class Grid which accepts two arguments, width and height and makes a multiline string zeros"""
    def __init__(self, width, height):
        self.cols = width
        self.rows = height
        self.body = [['0' for y in range(width)] for x in range(height)]
    
    def plot_point(self, x, y):
    """It has a function plot_point which plots an X on the grid. It accepts two arguments, x and y. x and y should be 1-based."""
        self.body[y-1][x-1] = 'X'
        
    def __repr__(self):
        return "".join(["{}\n".format("".join(self.body[r])) for r in range(self.rows)])[:-1]
    
    @property    
    def grid(self):
    """It also has an attribute grid which contains the multiline string"""
        return self.__repr__()
