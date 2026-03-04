"""
Clase del enemigo
"""
import pygame
import random
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, ENEMY_SPEED, IMAGE_ENEMY


class Enemigo(pygame.sprite.Sprite):
    """Clase que representa un enemigo"""
    
    def __init__(self, velocidad=ENEMY_SPEED):
        super().__init__()
        self.image = pygame.image.load(IMAGE_ENEMY).convert_alpha()
        self.rect = self.image.get_rect()
        self.velocidad = velocidad
        self.vel_x = 0
        self.vel_y = 0
        
        # Determinar lado de salida aleatorio
        self._spawnar_en_borde_aleatorio()
    
    def _spawnar_en_borde_aleatorio(self):
        """Posiciona el enemigo en un borde aleatorio"""
        lado = random.choice(["arriba", "abajo", "izquierda", "derecha"])
        
        if lado == "arriba":
            self.rect.x = random.randint(0, SCREEN_WIDTH)
            self.rect.y = -self.rect.height
            self.vel_y = self.velocidad
        elif lado == "abajo":
            self.rect.x = random.randint(0, SCREEN_WIDTH)
            self.rect.y = SCREEN_HEIGHT
            self.vel_y = -self.velocidad
        elif lado == "izquierda":
            self.rect.x = -self.rect.width
            self.rect.y = random.randint(0, SCREEN_HEIGHT)
            self.vel_x = self.velocidad
        else:  # derecha
            self.rect.x = SCREEN_WIDTH
            self.rect.y = random.randint(0, SCREEN_HEIGHT)
            self.vel_x = -self.velocidad
    
    def actualizar(self):
        """Actualizar posición del enemigo"""
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
    
    def esta_fuera_pantalla(self):
        """Verificar si el enemigo salió de la pantalla"""
        return (self.rect.right < 0 or self.rect.left > SCREEN_WIDTH or
                self.rect.bottom < 0 or self.rect.top > SCREEN_HEIGHT)
    
    def dibujar(self, surface):
        """Dibujar el enemigo"""
        surface.blit(self.image, self.rect)
