import core.quong

class BallController:

	MAX_SPEED = 200

	def __init__(self, ball):

		self.__ball = ball
		self.__unitVec = (-1.0, 0.0)
		self.__speed = 40
		self.__x, self.__y = 50, 50


	def onEvent(self, event):

		if event.type == core.quong.SOCKET_RECIEVE and event.ball.updated:
			self.setX(event.ball.x)
			self.setY(event.ball.y)
			self.setVelocity(event.ball.velocity)


	def getUnitVec(self):

		return self.__unitVec


	def getSpeed(self):

		return self.__speed


	def getVelocity(self):

		return tuple((i*self.__speed for i in self.__unitVec))

	def setVelocity(self, velocity):

		self.__speed = math.sqrt(sum((i*i for i in velocity)))
		self.__unitVec = tuple((i/self.__speed for i in velocity))


	def getX(self):

		return self.__x

	def setX(self, x):

		self.__x = x


	def getY(self):

		return self.__y

	def setY(self):

		self.__y = y

