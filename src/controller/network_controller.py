from . controller import *
import core

class NetworkController(Controller):

	def __init__(self, paddle):
		super(NetworkController, self).__init__(paddle)


	def onEvent(self, event):

		if event.type == core.quong.SOCKET_RECIEVE:
			if event.entity == 'paddle' and event.id == self.getPaddle().getId():
				self.getPaddle().setX(event.pos[0])
				self.getPaddle().setY(event.pos[1])
				self.setDirection(event.direction)
				print(event.direction)
				print("Setting position")


	def setDirection(self, direction):

		super(NetworkController, self).setDirection(direction)
