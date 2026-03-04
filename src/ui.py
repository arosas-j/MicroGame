"""
Funciones de interfaz de usuario del juego
"""
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, COLOR_BLACK, COLOR_WHITE, COLOR_RED


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
    texto_puntuacion = font_puntuacion.render(f"Puntuación: {puntuacion}", True, COLOR_WHITE)
    screen.blit(texto_puntuacion, (10, 10))
