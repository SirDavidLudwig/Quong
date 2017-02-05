

class Controller():

	LEFT_UP  = 1
	RIGHT_DOWN = 2
	MAX_SPEED = 65

	def __init__(self, paddle):

		self.__paddle = paddle
		self.__direction = 0

		self.__lastDt = 0


	def getDirection(self):

		return self.__direction


	def setDirection(self, direction):

		self.__direction = direction


	def tick(self, screen, dt):

		self.__lastDt = dt

		self.__speed = 0

		if self.__direction & Controller.LEFT_UP:
			self.__speed += -Controller.MAX_SPEED

		if self.__direction & Controller.RIGHT_DOWN:
			self.__speed += Controller.MAX_SPEED

		self.__paddle.move(self.__speed * dt)
