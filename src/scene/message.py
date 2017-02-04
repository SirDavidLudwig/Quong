from . scene import *
from entity.label import *


class Message(Scene):

	def __init__(self, message):
		super(Message, self).__init__()
		
		self.__message = message


	def initialize(self):

		label = Label(self.__message)
		label.setCenterX(True)
		label.setCenterY(True)

		self.addEntity(label)