

class Controller():

	LEFT_UP  = 1
	RIGHT_DOWN = 2
	MAX_SPEED = 5000

	def __init__(self, paddle):

		self.__paddle = paddle
		self.__direction = 0


	def getDirection(self):

		return self.__direction


	def setDirection(self, direction):

		self.__direction = direction


	def tick(self, screen, dt):

		speed = int(self.__direction & Controller.LEFT_UP) * -Controller.MAX_SPEED
		speed += int(self.__direction & Controller.RIGHT_DOWN) * Controller.MAX_SPEED

		self.__paddle.move(speed * dt)
