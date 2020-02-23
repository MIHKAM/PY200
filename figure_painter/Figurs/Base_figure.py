from abc import abstractmethod, abstractproperty
class Figure:
	def __init__(self, x=0, y=0):
		self._x = x  #start
		self._y = y


	@abstractmethod
	def perimeter(self):

		return 0

	def equare(self):
		return 0


	@abstractmethod
	def width(self):
		return 0


	@abstractmethod
	def height(self):
		return 0