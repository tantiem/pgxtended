import pygame
from pygame import math

class pgxObject():
	"""
	Parent object of all objects in PGX. Introduces the global positioning system.

	...

	Attributes
	---------
	gPosition: (public) Vector2: 
		the global position, in worldspace. This is the literal location of the object, regardless of cam view.

	Methods
	-------
	GetCamAlignPos(self, cam): cam(Camera);
		Returns a position to draw an object at.
	InCamRange(self, cam): cam(Camera);
		Returns if object is in range of Camera cam

	"""
	def __init__(self, pos_vector):
		#gPosition: (public) Vector2: the global position, in worldspace. This is the literal location of the object, regardless of cam view.
		self.gPosition = pygame.math.Vector2(pos_vector)

		#IMPORTANT UPDATE: (11/2/2021)
		#Due to a conflict in implementation of some camera features, local position has been removed in favor
		#Of a separate drawing method. The new method is described below.

	def GetCamAlignPos(self, cam):
		"""
		Returns a position to draw an object at.

		Inherited:
		cam: cam.gPosition (Vector2) - the camera's "global position"
		"""
		#UPDATED (11/2/2021):
		#Does not set local pos anymore. Local pos no longer exists, rather, each camera will draw 
		#objects given to it based on current position.
		
		vec2CamViewportPos = math.Vector2(self.gPosition.x - cam.gPosition.x, self.gPosition.y - cam.gPosition.y)
		return vec2CamViewportPos

	def InCamRange(self, cam):
		"""
		Returns whether or not the other object is in range of this camera based on camera view.

        self: A pgxObject
        cam: A Camera
		"""
		raise NotImplementedError()


class PgxGroup(pygame.sprite.LayeredUpdates):
	def __init__(self, *sprites, **kwargs) -> None:
		super().__init__(*sprites, **kwargs)

	def draw(self, cam):
		for sprite in self.sprites():
			sprite.Draw(cam)

	def add(self, *sprites, **kwargs):
		return super().add(*sprites, **kwargs)
		
		

