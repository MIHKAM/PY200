from Figurs.Base_figure import Figure

class CloseFigure(Figure):
    def __init__(self, *args):
        self.points = [*args]


    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        if not isinstance(x, int):
            self.x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        if not isinstance(y, int):
            self.y = y


