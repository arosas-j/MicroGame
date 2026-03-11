"""
Clase del personaje jugable
"""
import pygame
from constants import (
    SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_SPEED,
    IMAGE_PLAYER_RIGHT, IMAGE_PLAYER_LEFT
)


class Personaje(pygame.sprite.Sprite):
    """Clase que representa al personaje jugable"""
    
    def __init__(self, x, y):
        super().__init__()
        self.image_right = pygame.image.load(IMAGE_PLAYER_RIGHT).convert_alpha()
        self.image_left = pygame.image.load(IMAGE_PLAYER_LEFT).convert_alpha()
        self.image = self.image_right
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.vel_x = 0
        self.vel_y = 0
        self.velocidad = PLAYER_SPEED
        self.direccion = "right"
        self.__vida = 100
        
    def manejar_input(self, keys):
        """Controlar el personaje con WASD"""
        self.vel_x = 0
        self.vel_y = 0
        
        if keys[pygame.K_w]:
            self.vel_y = -self.velocidad
        if keys[pygame.K_s]:
            self.vel_y = self.velocidad
        if keys[pygame.K_a]:
            self.vel_x = -self.velocidad
            self.direccion = "left"
        if keys[pygame.K_d]:
            self.vel_x = self.velocidad
            self.direccion = "right"
    
    def actualizar(self):
        """Actualizar posición y límites de pantalla"""
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        
        # Límites de pantalla
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
        
        # Cambiar textura según dirección
        if self.direccion == "right":
            self.image = self.image_right
        else:
            self.image = self.image_left
    
    def dibujar(self, surface):
        """Dibujar el personaje"""
        surface.blit(self.image, self.rect)

    def recibir_dano(self, cantidad):
        """Reduce vida del personaje sin bajar de 0."""
        self.__vida = max(0, self.__vida - cantidad)

    def obtener_vida(self):
        """Devuelve la vida actual en porcentaje (0-100)."""
        return self.__vida

    def esta_sin_vida(self):
        """Indica si el personaje ya no tiene vida."""
        return self.__vida <= 0
