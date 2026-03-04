"""
Constantes y configuración global del juego
"""
import os
import pygame

# Configuración de pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
WINDOW_TITLE = "Bee game"

# Rutas de recursos (relativo al directorio de este archivo)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(SCRIPT_DIR, "../assets/textures")

# Rutas de imágenes
IMAGE_PLAYER_RIGHT = os.path.join(ASSETS_DIR, "p_right.png")
IMAGE_PLAYER_LEFT = os.path.join(ASSETS_DIR, "p_left.png")
IMAGE_ENEMY = os.path.join(ASSETS_DIR, "enemy.png")
IMAGE_COLLECTIBLE = os.path.join(ASSETS_DIR, "collectable.png")
IMAGE_BACKGROUND = os.path.join(ASSETS_DIR, "background.png")

# Configuración de personaje
PLAYER_SPEED = 5
PLAYER_START_X = SCREEN_WIDTH // 2
PLAYER_START_Y = SCREEN_HEIGHT // 2

# Configuración de enemigos
ENEMY_SPEED = 3
ENEMY_SPAWN_RATE = 60  # Frames entre spawns

# Configuración de coleccionables
COLLECTIBLE_SPEED = 2
COLLECTIBLE_SPAWN_RATE = 120  # Frames entre spawns
COLLECTIBLE_POINTS = 10

# Configuración de fondo
BACKGROUND_TILE_SIZE = 32

# Colores
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_RED = (255, 0, 0)
