import pgxObject
import pygame

#Drawable objects exist in space, and can be drawn with a draw function.

class Drawable(pgOjbect, pygame.sprite.Sprite):
	def __init__(self, pos, image, layer=0):
		super().__init__(pos)
		self.localLayer = layer
		self.image = image

	def Draw(self,Surface_dst):
		#draw
		#draw based on local position and existence.
		#Use dst argument on blitting. 
		pass
