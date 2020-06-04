import pygame
import os


class Music:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        interface_folder = os.path.dirname(__file__)
        sounds_folder = os.path.join(interface_folder, "sounds")
        pygame.mixer.music.load(os.path.join(sounds_folder, "21.mp3"))
        pygame.mixer.music.play(- 1)
        self.sound = pygame.mixer.Sound(os.path.join(sounds_folder, 'sfx-1.wav'))

    @staticmethod
    def stop():
        pygame.mixer.music.pause()

    @staticmethod
    def replay():
        pygame.mixer.music.unpause()

    @staticmethod
    def set_volume(volume):
        pygame.mixer.music.set_volume(volume)

    def sound_play(self):
        self.sound.play()

