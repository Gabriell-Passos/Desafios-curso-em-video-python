print ("Reprodutor de áudios MP3")
import pygame
pygame.init()
pygame.mixer.music.load('aaas.mp3')
pygame.mixer.music.play()
pygame.event.wait()

    # Tudo Certo!