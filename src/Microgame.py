"""
Bucle principal
"""
import pygame
from constants import (
    SCREEN_WIDTH, SCREEN_HEIGHT, FPS, WINDOW_TITLE,
    ENEMY_SPAWN_RATE, COLLECTIBLE_SPAWN_RATE, COLLECTIBLE_POINTS,
    IMAGE_BACKGROUND, BACKGROUND_TILE_SIZE, COLOR_BLACK,
    SOUND_PICK_COLLECTIBLE, SFX_VOLUME,
    MUSIC_BACKGROUND, MUSIC_VOLUME, ENEMY_DAMAGE
)
from player import Personaje
from enemy import Enemigo
from collectible import Coleccionable
from ui import (
    mostrar_game_over,
    dibujar_puntuacion,
    dibujar_barra_vida,
    mostrar_pantalla_inicio,
)

pygame.init()

# Crear pantalla y reloj
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(WINDOW_TITLE)
clock = pygame.time.Clock()

# Cargar fondo
background = pygame.image.load(IMAGE_BACKGROUND).convert()

# Cargar efectos de sonido
sonido_recoger = pygame.mixer.Sound(SOUND_PICK_COLLECTIBLE)
sonido_recoger.set_volume(SFX_VOLUME)

# Cargar y reproducir música de fondo en bucle infinito
pygame.mixer.music.load(MUSIC_BACKGROUND)
pygame.mixer.music.set_volume(MUSIC_VOLUME)
pygame.mixer.music.play(-1)

# Crear personaje
personaje = Personaje(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

# Listas de enemigos y coleccionables
enemigos = []
spawn_counter = 0

coleccionables = []
item_spawn_counter = 0

# Sistema de puntuación
puntuacion = 0


def iniciar_nueva_partida():
    """Reinicia todo el estado de juego para una nueva partida"""
    global personaje, enemigos, spawn_counter, coleccionables, item_spawn_counter, puntuacion
    personaje = Personaje(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    enemigos = []
    spawn_counter = 0
    coleccionables = []
    item_spawn_counter = 0
    puntuacion = 0


def actualizar(keys):
    """Actualiza la lógica del juego"""
    global spawn_counter, item_spawn_counter, puntuacion
    
    # Actualizar personaje
    personaje.manejar_input(keys)
    personaje.actualizar()
    
    # Spawning de enemigos
    spawn_counter += 1
    if spawn_counter >= ENEMY_SPAWN_RATE:
        enemigos.append(Enemigo())
        spawn_counter = 0
    
    # Spawning de coleccionables
    item_spawn_counter += 1
    if item_spawn_counter >= COLLECTIBLE_SPAWN_RATE:
        coleccionables.append(Coleccionable())
        item_spawn_counter = 0
    
    # Actualizar enemigos
    for enemigo in enemigos[:]:
        enemigo.actualizar()
        if enemigo.esta_fuera_pantalla():
            enemigos.remove(enemigo)
    
    # Actualizar coleccionables
    for coleccionable in coleccionables[:]:
        coleccionable.actualizar()
        if coleccionable.esta_fuera_pantalla():
            coleccionables.remove(coleccionable)
    
    # Detectar colisión con enemigos
    for enemigo in enemigos[:]:
        if personaje.rect.colliderect(enemigo.rect):
            personaje.recibir_dano(ENEMY_DAMAGE)
            enemigos.remove(enemigo)
            if personaje.esta_sin_vida():
                return False  # Fin del juego
    
    # Detectar colisión con coleccionables
    for coleccionable in coleccionables[:]:
        if personaje.rect.colliderect(coleccionable.rect):
            puntuacion += COLLECTIBLE_POINTS
            sonido_recoger.play()
            coleccionables.remove(coleccionable)
    
    return True  # Juego continúa


def dibujar():
    """Dibuja todos los elementos del juego"""
    # Dibujar fondo en mosaico
    for y in range(0, SCREEN_HEIGHT, BACKGROUND_TILE_SIZE):
        for x in range(0, SCREEN_WIDTH, BACKGROUND_TILE_SIZE):
            screen.blit(background, (x, y))
    
    # Dibujar objetos
    personaje.dibujar(screen)
    for enemigo in enemigos:
        enemigo.dibujar(screen)
    for coleccionable in coleccionables:
        coleccionable.dibujar(screen)
    
    # Mostrar UI
    dibujar_puntuacion(screen, puntuacion)
    dibujar_barra_vida(screen, personaje.obtener_vida())
    
    pygame.display.update()


def bucle_principal():
    """Bucle principal del juego"""
    global puntuacion
    
    running = True
    while running:
        clock.tick(FPS)
        
        # Manejo de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        # Obtener teclas presionadas
        keys = pygame.key.get_pressed()
        
        # Actualizar lógica del juego
        juego_activo = actualizar(keys)
        
        if not juego_activo:
            accion = mostrar_game_over(screen, puntuacion)
            if accion == "reiniciar":
                iniciar_nueva_partida()
                continue
            running = False
        
        # Dibujar
        dibujar()


if __name__ == "__main__":
    accion_inicio = mostrar_pantalla_inicio(
        screen,
        background,
        BACKGROUND_TILE_SIZE,
        WINDOW_TITLE,
    )

    if accion_inicio == "comenzar":
        bucle_principal()

    pygame.mixer.music.stop()
    pygame.quit()
