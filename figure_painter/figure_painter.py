import os

os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = 'C:\\ProgramData\\Anaconda3\\Lib\\site-packages\\PySide2\\plugins\\platforms'

import sys
# Подключаем модули QApplication и QLabel
from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtGui import QPainter, QBrush
from PySide2.QtCore import Qt, QPoint

# Импортируйте свой файл с фигурами
from Figurs.Rectangle import Rectangle
from Figurs.Ellipse import Ellipse
from Figurs.Base_figure import Figure
from Figurs.CloseFigure import CloseFigure

class FigureWidget(QWidget):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.setWindowTitle('Рисовалка фигур')
		self.__figures = []
		
	def set_figures(self, figures):
		self.__figures = figures
		
		
	def paintEvent(self, event):
    
		painter = QPainter(self)
		reset_brush = painter.brush()
		for figure in self.__figures:
			if not isinstance(figure, Figure):
				raise TypeError
				
			if isinstance(figure, Rectangle):
				painter.setBrush(QBrush(Qt.red))
				painter.drawRect(figure.x, figure.y, figure.width, figure.height)
				continue

			if isinstance(figure, Ellipse):
				painter.setBrush(QBrush(Qt.green))
				painter.drawEllipse(figure.x, figure.y, figure.width, figure.height)
				continue

			if isinstance(figure, CloseFigure):
				painter.setBrush(QBrush(Qt.blue))
				points = []
				for point in figure.points:
					points.append(QPoint(point['x'], point['y']))
				painter.drawPolygon(points)
				continue


                                                     
if __name__ == '__main__':
	app = QApplication(sys.argv)
	figure_widget = FigureWidget()

	# Создайте список фигур
	figures = [Rectangle(5, 5, 100, 100), Ellipse(200, 5, 100, 100),
			   CloseFigure({'x': 50, 'y': 50}, {'x': 50, 'y': 100}, {'x': 100, 'y': 100})]

	figure_widget.set_figures(figures)

	figure_widget.show()
	sys.exit(app.exec_())
