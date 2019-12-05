import pygame


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

N_BLOCKS = 4
N_TRIALS = 15
OUTPUT_FILE = 'reaction_times.csv'


def main():
    screen = open_window()
    run_experiment(screen)
    close_window()


def open_window():
    pygame.init()
    pygame.mouse.set_visible(False)
    return pygame.display.set_mode((0, 0), pygame.FULLSCREEN)


def run_experiment(screen):
    # Show general instructions
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface = myfont.render('General instructions', False, WHITE)
    screen.blit(textsurface,(0,0))
    get_input()

    # Start experiment
    for block in range(N_BLOCKS):
        run_block(screen)


def get_input():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                else:
                    return event.key


def run_block(screen):
    # show instructions for the block
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface = myfont.render('Block instructions', False, WHITE)
    screen.blit(textsurface,(0,0))
    pygame.display.flip()

    # start block of trials
    get_input()
    for trial in range(N_TRIALS):
        run_trial(screen)


def run_trial(screen):
    r = screen.get_rect()
    pygame.draw.circle(screen, WHITE, (r.width // 2, r.height // 2), 10)
    pygame.display.flip()
    print(get_input())


def close_window():
    pass


#    reaction_times = []

if __name__ == '__main__':
    main()
