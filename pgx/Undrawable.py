from . import pgxObject

class Undrawable(pgxObject.pgxObject):
	def __init__(self, pos):
		super().__init__(pos)
