from . import Undrawable
from pygame import mixer

class AudioSource(Undrawable.Undrawable):
    def __init__(self, filename, pos, isGlobal, radius=10, baseVolume=1):
        super().__init__(pos)
        #_global: (private) bool: Whether or not the sound plays regardless of distance to the focus
        #_sound: (private) pygame.mixer.sound: The sound object this audiosource plays
        #radius: (public) int: The minimum distance the focus must be for this sound to be audible
        #baseVolume (public) float: The base volume of the sound
        self._global = isGlobal
        self._sound = mixer.Sound(filename)
        self.radius = radius   
        self.baseVolume = baseVolume

        self._sound.set_volume(baseVolume)

    def Play(self):
        self._sound.play()

