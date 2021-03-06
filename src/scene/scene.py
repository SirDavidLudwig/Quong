from graphics.frame import Frame
# Scene will keep track of the game and server

class Scene(Frame):

	def __init__(self):
		super(Scene, self).__init__(0, 0, 100, 100)

		self.__frames = []
		self.__entities = []
		self.__parent = None


	def initialize(self):

		pass # Initialization code goes here


	def draw(self, screen, dt):

		for frame in self.__frames:
			frame.draw(frame, dt)

		for entity in self.__entities:
			entity.draw(screen, dt)


	def addEntity(self, entity):

		self.__entities.append(entity)


	def addFrame(self, frame):

		self.__frames.append(frame)


	def onEvent(self, event):

		for entity in self.__entities:
			entity.onEvent(event)
