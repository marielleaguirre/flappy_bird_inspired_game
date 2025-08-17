import pygame
import os
import random
import sys

pygame.font.init()
pygame.mixer.init()

SOUND_DIE = pygame.mixer.Sound(os.path.join("audio", "die.wav"))
SOUND_HIT = pygame.mixer.Sound(os.path.join("audio", "hit.wav"))
SOUND_POINT = pygame.mixer.Sound(os.path.join("audio", "point.wav"))
SOUND_SWOOSH = pygame.mixer.Sound(os.path.join("audio", "swoosh.wav"))
SOUND_WING = pygame.mixer.Sound(os.path.join("audio", "wing.wav"))

WIN_WIDTH = 500
WIN_HEIGHT = 800

BIRD_IMGS = [
    pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird1.png"))),
    pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird2.png"))),
    pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird3.png")))
]
PIPE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "pipe.png")))
BASE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "base.png")))
BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bg.png")))
