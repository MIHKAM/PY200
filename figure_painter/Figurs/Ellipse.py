from Figurs.Base_figure import Figure

class Ellipse(Figure):
	def __init__(self, x=0, y=0, w=0, h=0):
		super().__init__(x, y)
		self.w = w
		self.h = h

	@property
	def x(self):
		return self._x

	@x.setter
	def x(self, x):
		if not isinstance(x, (int, float)):
			self._x = x

	@property
	def y(self):
		return self._y

	@property
	def equare(self):
		return self.w*self.h

	@property
	def width(self):
		return self.w

	@property
	def height(self):
		return self.h