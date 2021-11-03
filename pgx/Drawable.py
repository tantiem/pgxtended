from . import pgxObject

import pygame

#Drawable objects exist in space, and can be drawn with a draw function.

class Drawable(pgxObject.pgxObject, pygame.sprite.Sprite):
	def __init__(self, pos, image, group=None, layer=0):
		super().__init__(pos)
		pygame.sprite.Sprite.__init__(self,group)
		#localLayer: (public) int: Drawing layer of this object. Objects in the same layer will be drawn in order.
		#-layer order is not designed to be global, but can be if desired. Idea is that certain types of objects have their own
		#-general layers (i.e. UI, background, foreground, etc) and the local layer decides layering based on those groupings.
		#-In pygame, however, there are no layers, and layering is determined by draw order only.
		#image: (public) pygame.Surface: the image to render in the Draw() method. 
		#if group is not none, it will be used by the sprite init to add object to a group automatically.
		self.localLayer = layer
		self.image = image
		self.rect = image.get_rect(topleft=self.gPosition)

	def Draw(self,cam):
		#draw
		#draw based on local position and existence.
		#Use dst argument on blitting. 
		cam.camSurface.blit(self.image, self.GetCamAlignPos(cam))
		pass

	def Update(self,cam):
		raise NotImplementedError()

	def update(self,*args,**kwargs):
		#This is the method inherited from pygame.sprite.Sprite()
		#it does nothing by default, so I'm going to just make it be a wrapper for 
		#the pgx Update() method. If you want to use sprite.update (like in a group)
		#then you should pass the cam as args[0]
		self.Update(args[0])

	



