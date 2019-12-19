import pygame
import pygame.freetype


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
    return pygame.display.set_mode((800, 600), pygame.FULLSCREEN)


def run_experiment(screen):
    show_instructions("general_instructions.txt", screen)

    for block_number in range(N_BLOCKS):
        run_block(screen, block_number)


def show_instructions(instructions_path, screen):
    screen.fill(BLACK)
    myfont = pygame.freetype.SysFont('Times New Roman', 20)
    with open(instructions_path, "r") as f:
        text = [line for line in f]
    # for y, line on zip(ys, text):
    for line in text:
        textsurface = myfont.render(line, fgcolor=WHITE)[0]

    textrect = textsurface.get_rect()
    textrect.center = (400, 300)
    screen.blit(textsurface, textrect)
    pygame.display.update()
    get_input()


def get_input():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                else:
                    return event.key


def run_block(screen, block_number):
    show_instructions(f"block_{block_number}_instructions.txt", screen)

    for trial in range(N_TRIALS):
        run_trial(screen)


def run_trial(screen):
    screen.fill(BLACK)
    r = screen.get_rect()
    pygame.draw.circle(screen, WHITE, (r.width // 2, r.height // 2), 10)
    pygame.display.flip()
    get_input()


def close_window():
    pass


#    reaction_times = []

if __name__ == '__main__':
    main()
