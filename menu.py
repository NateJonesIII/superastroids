import sys
import pygame

def main_menu(screen):
    font = pygame.font.Font(None, 74)
    menu_text = font.render('Press Enter to Start', True, (255, 255, 255))
    menu_rect = menu_text.get_rect(center=(screen.get_width()//2, screen.get_height()//2))

    while True:
        screen.fill((0, 0, 0))
        screen.blit(menu_text, menu_rect)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return  # Exit the main menu and start the game