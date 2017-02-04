# The main Quong script will assign the main instance here
quong = None

def getQuong():

	return quong


def toPercentX(x, frame = None):

	if frame is None:
		frame = quong.getScreen()

	return int(x / frame.getWidth() * 100)


def toPercentY(y, frame = None):

	if frame is None:
		frame = quong.getScreen()

	return int(y / frame.getHeight() * 100)


def toPixelsX(x, frame = None):

	if frame == None:
		frame = quong.getScreen().getScene()

	return int(x / 100.0 * frame.getRect().width + frame.getRect().x)


def toPixelsY(y, frame = None):

	if frame == None:
		frame = quong.getScreen().getScene()

	return int(y / 100.0 * frame.getRect().height + frame.getRect().y)
