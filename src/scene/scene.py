from graphics.frame import Frame
# Scene will keep track of the game and server

class Scene(Frame):

	def __init__(self):

		self.__entities = []

		super(Scene, self).__init__(0, 0, 100, 100)
		self.__parent = None


	def draw(self, screen, dt):

		for entity in self.__entities:
			entity.draw(screen, dt)


	def addEntity(self, entity):

		self.__entities.append(entity)


	def onEvent(self, event):

		for entity in self.__entities:
			entity.onEvent(event)
