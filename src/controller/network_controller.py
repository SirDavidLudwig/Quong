from . controller import *

class NetworkController(Controller):

	def __init__(self, paddle):
		super(NetworkController, self).__init__(paddle)


	def onEvent(self, event):

		if event.type == core.quong.SOCKET_RECIEVE and event.id == self.getId():
			self.setDirection(event.direction)


	def setDirection(self, direction):

		print("Direction set to", direction)
		super(NetworkController, self).setDirection(direction)