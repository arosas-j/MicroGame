"""
Funciones de interfaz de usuario del juego
"""
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, COLOR_BLACK, COLOR_WHITE, COLOR_RED


def mostrar_pantalla_inicio(screen, background, tile_size, titulo):
    """Muestra una pantalla inicial y espera a que el jugador pulse espacio."""
    font_titulo = pygame.font.Font(None, 84)
    texto_titulo = font_titulo.render(titulo, True, COLOR_BLACK)

    font_subtitulo = pygame.font.Font(None, 44)
    texto_inicio = font_subtitulo.render("Pulsa ESPACIO para comenzar", True, COLOR_BLACK)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "salir"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "salir"
                if event.key == pygame.K_SPACE:
                    return "comenzar"

        for y in range(0, SCREEN_HEIGHT, tile_size):
            for x in range(0, SCREEN_WIDTH, tile_size):
                screen.blit(background, (x, y))

        screen.blit(texto_titulo, (
            SCREEN_WIDTH // 2 - texto_titulo.get_width() // 2,
            SCREEN_HEIGHT // 2 - 90,
        ))
        screen.blit(texto_inicio, (
            SCREEN_WIDTH // 2 - texto_inicio.get_width() // 2,
            SCREEN_HEIGHT // 2 + 10,
        ))
        pygame.display.update()


def mostrar_game_over(screen, puntuacion):
    """
    Mostrar pantalla de game over y esperar a que cierre
    
    Args:
        screen: Superficie de pygame para dibujar
        puntuacion: Puntuación final del jugador
    
    Returns:
        "salir" para cerrar el juego
        "reiniciar" para empezar una nueva partida
    """
    font = pygame.font.Font(None, 72)
    texto_game_over = font.render("GAME OVER", True, COLOR_RED)
    
    font_small = pygame.font.Font(None, 36)
    texto_puntos = font_small.render(f"Puntuación: {puntuacion}", True, COLOR_WHITE)
    texto_reiniciar = font_small.render("Presiona ESPACIO para reiniciar", True, COLOR_WHITE)
    texto_cerrar = font_small.render("Presiona ESC para cerrar", True, COLOR_WHITE)
    
    esperando = True
    while esperando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "salir"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "salir"
                if event.key == pygame.K_SPACE:
                    return "reiniciar"
        
        screen.fill(COLOR_BLACK)
        screen.blit(texto_game_over, (SCREEN_WIDTH // 2 - texto_game_over.get_width() // 2, 
                                      SCREEN_HEIGHT // 2 - 100))
        screen.blit(texto_puntos, (SCREEN_WIDTH // 2 - texto_puntos.get_width() // 2, 
                                   SCREEN_HEIGHT // 2))
        screen.blit(texto_reiniciar, (SCREEN_WIDTH // 2 - texto_reiniciar.get_width() // 2, 
                                      SCREEN_HEIGHT // 2 + 60))
        screen.blit(texto_cerrar, (SCREEN_WIDTH // 2 - texto_cerrar.get_width() // 2, 
                                   SCREEN_HEIGHT // 2 + 110))
        pygame.display.update()
    
    return "salir"


def dibujar_puntuacion(screen, puntuacion):
    """
    Dibuja la puntuación en la esquina superior izquierda
    
    Args:
        screen: Superficie de pygame para dibujar
        puntuacion: Puntuación actual
    """
    font_puntuacion = pygame.font.Font(None, 36)
    texto_puntuacion = font_puntuacion.render(f"Puntuación: {puntuacion}", True, COLOR_BLACK)
    screen.blit(texto_puntuacion, (10, 10))


def dibujar_barra_vida(screen, vida_porcentaje):
    """Dibuja una barra de vida en porcentaje (0-100)."""
    barra_x = 10
    barra_y = 50
    barra_ancho = 200
    barra_alto = 22

    vida_clamp = max(0, min(100, vida_porcentaje))
    relleno_ancho = int((vida_clamp / 100) * barra_ancho)

    if vida_clamp > 50:
        color_vida = (40, 200, 40)
    elif vida_clamp > 25:
        color_vida = (240, 180, 0)
    else:
        color_vida = COLOR_RED

    pygame.draw.rect(screen, COLOR_WHITE, (barra_x, barra_y, barra_ancho, barra_alto), 2)
    if relleno_ancho > 0:
        pygame.draw.rect(screen, color_vida, (barra_x, barra_y, relleno_ancho, barra_alto))
