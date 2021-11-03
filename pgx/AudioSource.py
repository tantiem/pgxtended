from . import Undrawable

class AudioSource(Undrawable.Undrawable):
    def __init__(self, pos, isGlobal, sound, radius=10, baseVolume=1):
        super().__init__(pos)
        #_global: (private) bool: Whether or not the sound plays regardless of distance to the focus
        #_sound: (private) pygame.mixer.sound: The sound object this audiosource plays
        #radius: (public) int: The minimum distance the focus must be for this sound to be audible
        #baseVolume (public) float: The base volume of the sound
        self._global = isGlobal
        self._sound = sound
        self.radius = radius   
        self.baseVolume = baseVolume

