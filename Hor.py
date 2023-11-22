# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import pygame
import sys

pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Your Horror Game")

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

player_image = pygame.image.load("player.png")
player_rect = player_image.get_rect()
player_rect.center = (width // 2, height // 2)

# Inside the game loop
screen.blit(player_image, player_rect)
# Add horror elements and events
# Example: Jump scare when player reaches a certain location
if player_rect.colliderect(scare_location_rect):
    # Implement jump scare
    pass
pygame.mixer.init()
pygame.mixer.music.load("background_music.mp3")
pygame.mixer.music.play(-1)  # Loop indefinitely

# Play sound effect
pygame.mixer.Sound("scream.wav").play()
