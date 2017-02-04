# The main Quong script will assign the main instance here
quong = None


def toPercentX(x):

	return x / quong.getScreen().getWidth() * 100


def toPercentY(y):

	return y / quong.getScreen().getHeight() * 100


def toPixelsX(x):

	return x / 100.0 * quong.getScreen().getWidth()


def toPixelsY(y):

	return y / 100.0 * quong.getScreen().getHeight()