from . frame import Frame
from core.utils import *
import pygame


class DebugFrame(Frame):

	def draw(self, screen, dt):

		pygame.draw.rect(getQuong().getScreen().getSurface(), (60, 60, 60), self.getRect())

		super(DebugFrame, self).draw(screen, dt)
