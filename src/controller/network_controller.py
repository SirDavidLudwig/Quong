from . controller import *

class NetworkController(Controller):

	def __init__(self, paddle, id):
		super(NetworkController, self).__init__(paddle)
		self.__id = id


	def onEvent(self, event):

		if event.type == core.quong.SOCKET_RECIEVE:
			self.setDirection(event.paddle[id].direction)
