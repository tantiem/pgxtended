from . import Drawable
from pygame import math
from pygame import rect


class Transformable(Drawable.Drawable):
	def __init__(self,pos,image, group=None, layer=0):
		super().__init__(pos, image, group, layer)
		#_scale: (private) int: scale of the object. Usually 1. Modify only with methods, changing sprite transform can be wonky
		#_rotation: (private) float: rotation of the object. Usually 0. Modify only with methods, changing sprite transform can be wonky
		self._scale = 1
		self._rotation = 0.0

	def MoveAbsolute(self, vec2Pos):
		#Inherited: self.gPosition (Vector2) - Global position

		#Move directly to, I ain't smoothing this for you!
		#Global position change
		self.gPosition = vec2Pos
		pass

	def MoveRelative(self, vec2Change):
		#Inherited: self.gPosition (Vector2) - Global position

		#Move relatively, still ain't smoothing.
		#Global position change
		self.gPosition += vec2Change
	
	def ScaleTo(self, intScale):
		#scale the object with a pygame transform, absolutely
		pass

	def RotateTo(self, floatRotation):
		#rotate object with pygame transform, absolutely
		pass
	
	def CamAlign(self, cam):
		#set position based on cam position
		#This probably does not need to be overloaded

		#Inherited: self.localPos (Vector2) - Local position
		#cam: cam.gPosition (Vector2) - the camera's "global position"
		#Should always be called after all movements are done.
		#this objects local position found by assuming cameras global position
		#is the origin.
		
		vec2NewPos = math.Vector2(self.gPosition.x - cam.gPosition.x, self.gPosition.y - cam.gPosition.y)
		self.localPos = vec2NewPos
		self.rect.update(vec2NewPos.x,vec2NewPos.y,self.rect.width,self.rect.height)
		
		pass

	def Update(self, cam):
		self.CamAlign(cam)