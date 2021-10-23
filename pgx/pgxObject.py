import pygame

class pgxObject():
	def __init__(self, pos_vector):
		#gPosition: (public) Vector2: the global position, in worldspace. This is the literal location of the object, regardless of cam view.
		#localPos: (public) Vector2: the local position, inside of the view frustrum. Use this to draw the object
		self.gPosition = pygame.math.Vector2(pos_vector)
		self.localPos = pygame.math.Vector2(pos_vector)

	def inRange(self, currentCamera):
		#return if this object is in view of the current camera
		#compare global positions of camera and this object. 
		pass
