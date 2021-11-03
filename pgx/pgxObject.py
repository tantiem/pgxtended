import pygame
from pygame import math

class pgxObject():
	def __init__(self, pos_vector):
		#gPosition: (public) Vector2: the global position, in worldspace. This is the literal location of the object, regardless of cam view.
		self.gPosition = pygame.math.Vector2(pos_vector)

		#IMPORTANT UPDATE: (11/2/2021)
		#Due to a conflict in implementation of some camera features, local position has been removed in favor
		#Of a separate drawing method. The new method is described below.

	def GetCamAlignPos(self, cam):
		#UPDATED (11/2/2021):
		#Does not set local pos anymore. Local pos no longer exists, rather, each camera will draw 
		#objects given to it based on current position.

		#Returns a position to draw an object at.

		#Inherited:
		#cam: cam.gPosition (Vector2) - the camera's "global position"
		#Should always be called after all movements are done.
		#this objects local position found by assuming cameras global position
		#is the origin.
		
		vec2CamViewportPos = math.Vector2(self.gPosition.x - cam.gPosition.x, self.gPosition.y - cam.gPosition.y)
		return vec2CamViewportPos

	
