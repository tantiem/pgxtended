from . import pgxObject

import pygame

#Drawable objects exist in space, and can be drawn with a draw function.

class Drawable(pgxObject.pgxObject, pygame.sprite.Sprite):
	"""
	Inherits pgxObject, pygame.Sprite

	The most base class for all drawn objects. Controls drawing and updating.
	...

	Attributes
	----------
	localLayer:	(public) int:
		Drawing layer of this object. Objects in the same layer will be drawn in order.
		layer order is not designed to be global, but can be if desired. Idea is that certain types of objects have their own
		general layers (i.e. UI, background, foreground, etc) and the local layer decides layering based on those groupings.
		In pygame, however, there are no layers, and layering is determined by draw order only.

	image:		(public) pygame.Surface: 
		the image to render in the Draw() method. if group is not none, it will be used by the sprite init 
		to add object to a group automatically.

	rect:		(public) pygame.Rect: 
		The image rect to allow functionality for collisions.

	Methods
	-------
	Draw(cam):a cam(pgx.Camera);
		draws image to camera surface
	"""
	def __init__(self, pos, image, group=None, layer=0):
		super().__init__(pos)
		pygame.sprite.Sprite.__init__(self,group)
		
		self.localLayer = layer
		self.image = image
		self.rect = image.get_rect(topleft=self.gPosition)

	def Draw(self,cam):
		"""
		Draws an image onto the cam.camSurface using the blit method.
		The destination param of blit is pgxObject -> GetCamAlignPos.

		cam: a Camera object
		"""
		#draw
		#draw based on local position and existence.
		#Use dst argument on blitting. 
		cam.camSurface.blit(self.image, self.GetCamAlignPos(cam))
		pass

	def Update(self,cam):
		"""
		Generic update method. Override as needed

		cam: a Camera object
		"""
		raise NotImplementedError()

	def update(self,*args,**kwargs):
		"""
		This is the method inherited from pygame.sprite.Sprite()

		it does nothing by default, so I just made it be a wrapper for 
		the pgx Update() method. If you want to use sprite.update (like in a group)
		then you should pass the cam as args[0]
		"""
		
		self.Update(args[0])

	



