# The main Quong script will assign the main instance here
quong = None

def getQuong():

	return quong


def toPercentX(frame, x):

	print(frame.getRect().width, x, frame.getRect().x)
	return (x - frame.getRect().x) / frame.getRect().width * 100


def toPercentY(frame, y):

	return (y - frame.getRect().y) / frame.getRect().height * 100


def toPercentWidth(frame, width):

	return width / frame.getRect().width * 100


def toPercentHeight(frame, height):

	return height / frame.getRect().height * 100


def toPixelsX(frame, x):

	return int(x / 100.0 * frame.getRect().width + frame.getRect().x)


def toPixelsY(frame, y):

	return int(y / 100.0 * frame.getRect().height + frame.getRect().y)


def toPixelsWidth(frame, width):

	return int(width / 100.0 * frame.getRect().width)


def toPixelsHeight(frame, height):

	return int(height / 100.0 * frame.getRect().height)

