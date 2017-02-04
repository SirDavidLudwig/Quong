from . entity import *
from core.utils import *
import pygame


class Button(Entity):

	def __init__(self, width, height, text, parent):
		super(Button, self).__init__(parent)

		self.__width = width
		self.__height = height
		self.__text = text

		self.__centerX = False
		self.__centerY = False

		self.__pressed = False
		self.__clickListeners = []


	def onEvent(self, event):

		if event.type == pygame.MOUSEBUTTONDOWN:
			if self.isHover():
				self.__pressed = True

		elif event.type == pygame.MOUSEBUTTONUP:
			if self.isHover() and self.__pressed is True:
				for listener in self.__clickListeners:
					listener() 

			self.__pressed = False


	def setOnClickListener(self, callback):

		self.__clickListeners.append(callback)


	def isHover(self):

		x = toPercentX(pygame.mouse.get_pos()[0])
		y = toPercentY(pygame.mouse.get_pos()[1])

		return x >= self.getX() and \
		       y >= self.getY() and \
		       x <= self.getX() + self.__width and \
		       y <= self.getY() + self.__height


	def draw(self, screen, dt):

		self.drawOutline(screen)
		self.drawText(screen)


	def drawOutline(self, screen):
		
		x = toPixelsX(self.getParent(), self.getX())
		y = toPixelsY(self.getParent(), self.getY())

		width = toPixelsX(self.getParent(), self.__width)
		height = toPixelsY(self.getParent(), self.__height)

		color = (255, 0, 0) if self.__pressed and self.isHover() else (255, 255, 255)

		pygame.draw.rect(screen.getSurface(), color, [x, y, width, height], 2)


	def drawText(self, screen):

		font = pygame.font.SysFont("monospace", 30)
		label = font.render(self.__text, 1, (255, 255, 255))
		
		# Get width and height and convert to use percentage width (0-100)
		width = label.get_rect().width / screen.getWidth() * 100
		height = label.get_rect().height / screen.getHeight() * 100

		x = toPixelsX(self.getParent(), self.getX() + (self.__width - width) / 2)
		y = toPixelsY(self.getParent(), self.getY() + (self.__height - height) / 2)

		screen.getSurface().blit(label, (x, y))


	def getX(self):

		if self.__centerX:
			return (100 - self.__width) / 2
		else:
			return super(Button, self).getX()


	def getY(self):

		if self.__centerY:
			return (100 - self.__height) / 2
		else:
			return super(Button, self).getY()


	def setCenterX(self, center):

		self.__centerX = center


	def setCenterY(self, center):

		self.__centerY = center


	def setText(self, text):

		self.__text = text