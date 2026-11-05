import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    while running:
        # poll for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        #fill screen with black
        screen.fill((0, 0, 0))
        #display hello world on screen
        font = pygame.font.Font(None, 74)
        #white text
        text = font.render("Hello World", True, (255, 255, 255))
        # center even if screen size changes
        screen.blit(text, (screen.get_width() / 2 - text.get_width() / 2, screen.get_height() / 2 - text.get_height() / 2))
        #swap the buffers
        pygame.display.flip()
        #limit to 60 fps
        clock.tick(60)
    pygame.quit()


if __name__ == "__main__":
    main()