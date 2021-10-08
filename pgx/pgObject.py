import pygame

class pgObject:
	def __init__(self, pos_vector):
		self.position = pygame.math.Vector2(pos_vector)

	def inRange(self, currentCamera):
		#return if this object is in view of the current camera
		pass
