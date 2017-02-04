# The main Quong script will assign the main instance here
quong = None


def toPercentX(x, frame = quong.getScreen()):

	return x / quong.getScreen().getWidth() * 100


def toPercentY(y, frame = quong.getScreen()):

	return y / quong.getScreen().getHeight() * 100


def toPixelsX(x, frame = quong.getScreen()):

	return x / 100.0 * quong.getScreen().getWidth()


def toPixelsY(y, frame = quong.getScreen()):

	return y / 100.0 * quong.getScreen().getHeight()