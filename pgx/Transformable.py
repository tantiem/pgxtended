from . import Drawable
from pygame import rect
from pygame import transform
from pygame import math


class Transformable(Drawable.Drawable):
	def __init__(self,pos,image, group=None, layer=0):
		super().__init__(pos, image, group, layer)
		#_scale: (private) int: scale of the object. Usually 1. Modify only with methods, changing sprite transform can be wonky
		#_rotation: (private) float: rotation of the object. Usually 0. Modify only with methods, changing sprite transform can be wonky
		#_baseSize: (private) Vector2: s.e; base size of object. Don't change this directly, unless you like headaches!
		self._scale = 1
		self._rotation = 0.0
		self._baseSize = math.Vector2(self.rect.width,self.rect.height)

	def MoveAbsolute(self, vec2Pos):
		#Inherited: self.gPosition (Vector2) - Global position

		#Move directly to, I ain't smoothing this for you!
		#Global position change
		self.gPosition = vec2Pos

	def MoveRelative(self, vec2Change):
		#Inherited: self.gPosition (Vector2) - Global position

		#Move relatively, still ain't smoothing.
		#Global position change
		self.gPosition += vec2Change
	
	def ScaleTo(self, intScale):
		#scale the object with a pygame transform, absolutely
		if intScale > 0:
			self._scale = intScale
			self.image = transform.scale(self.image,(self._baseSize.x * intScale, self._baseSize.y * intScale))
		else:
			print("Trying to set an invalid scale! (<= 0)")
		

	def RotateTo(self, floatRotation):
		#rotate object with pygame transform, absolutely
		#Positive values are counter clockwise.
		deltaRotation = (floatRotation % 360) - self._rotation
		self.Rotate(deltaRotation)

	def Rotate(self, deltaRotation):
		#Use pygame.transform.rotate to additively rotate the surface.
		#keeps track of current rotation.
		self.image = transform.rotate(self.image,deltaRotation)
		self._rotation += deltaRotation
		if(self._rotation > 360 or self._rotation < -360):
			self._rotation %= 360

	def Update(self, cam):
		#Makes sure that the rect object is updated for collision purposes
		self.rect.update(self.gPosition.x,self.gPosition.y,self.rect.width,self.rect.height)