"""A module to control the ins and outs of pygame input."""

from typing import Tuple
import pygame
from pygame import locals as locs
from pygame.event import Event


class InputManager:
    def __init__(self):
        self.eventQueue = []

    def Refresh(self):
        self.eventQueue = pygame.event.get()

    def GetEventQueue(self):
        return self.eventQueue

    def EventActive(self, eventType):
        """
        Returns whether or not the event type is active in the current event queue.
        """
        for event in self.eventQueue:
            if event.type == eventType:
                return True
        return False

    def GetActiveEvent(self, eventType):
        """
        Checks whether or not the event type is active. If so, returns that event. If not, returns NONE.
        """
        for event in self.eventQueue:
            if event.type == eventType:
                return event
        return None

    def GetMousePos(self):
        """Get mouse positions"""
        return pygame.mouse.get_pos()

    def GetMouseClicked(self):
        """Returns if the mouse has been clicked since the last refresh."""
        return self.EventActive(locs.MOUSEBUTTONDOWN)

    def GetMouseMoved(self):
        """Returns whether or not the mouse has been moved since the last refresh."""
        return self.EventActive(locs.MOUSEMOTION)

    def GetKeyHeld(self,key):
        """
        Held down key input
        Returns: Whether or not key is being held.
        """
        held_keys = pygame.key.get_pressed()
        if held_keys[key]:
            return True
        return False

    def GetKeyPressed(self,key):
        """
        Pressed key input
        Returns: Whether or not a key has been pressed since last refresh.
        """
        keyFound = False
        for event in self.eventQueue:
            if event.type == locs.KEYDOWN:
                if event.key == key:
                    keyFound = True
        return keyFound


