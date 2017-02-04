
from core.quong import *
import sys


def main(argv):

	quong = Quong(argv)

	return sys.exit(quong.run())


if __name__ == '__main__':
	main(sys.argv)