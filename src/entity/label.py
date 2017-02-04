from . entity import *
from core.utils import *
import pygame


class Label(Entity):

	def __init__(self, text, parent = None):
		super(Label, self).__init__(parent)

		self.__font = None
		self.__text = None
		self.__label = None

		self.setFontSize(30)
		self.setText(text)

		self.__centerX = False
		self.__centerY = False


	def draw(self, screen, dt):

		x = toPixelsX(self.getParent(), self.getX())
		y = toPixelsY(self.getParent(), self.getY())

		screen.getSurface().blit(self.__label, (x, y))


	def getX(self):

		if self.__centerX:
			return (100 - self.__width) / 2
		else:
			return super(Label, self).getX()


	def getY(self):

		if self.__centerY:
			return (100 - self.__height) / 2
		else:
			return super(Label, self).getY()


	def setCenterX(self, center):

		self.__centerX = center


	def setCenterY(self, center):

		self.__centerY = center


	def setFontSize(self, fontSize):
		
		self.__font = pygame.font.SysFont("monospace", fontSize)


	def setText(self, text):

		self.__text = text
		
		self.__label = self.__font.render(self.__text, 1, (255, 255, 255))

		print(self.__label.get_rect().width)
		
		# Get width and height and convert to use percentage width (0-100)
		self.__width = self.__label.get_rect().width / toPixelsX(self.getParent(), self.getParent().getWidth()) * 100
		self.__height = self.__label.get_rect().height / toPixelsY(self.getParent(), self.getParent().getHeight()) * 100
