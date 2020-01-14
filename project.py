import pygame, random
import pygame.freetype
from datetime import datetime


SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

N_BLOCKS = 4
N_TRIALS = 15
OUTPUT_FILE = f'reaction_times_{datetime.now().strftime("%d-%m-%YT%H-%M")}.csv' # putting a time stamp into the name of the output file to later identify it
REACTION_TIMES = []


def main():
    screen = open_window()
    run_experiment(screen)
    saveresults = open(OUTPUT_FILE, 'w')
    saveresults.write('Block, Trial, RT[ms]\n')
    for block, trials in enumerate(REACTION_TIMES):
        for trial, reaction_time in enumerate(trials):
            saveresults.write(str(block+1) + ", " + str(trial+1) + ", " + str(reaction_time) + "\n")
    saveresults.close()
    close_window()


def open_window():
    pygame.init()
    pygame.mouse.set_visible(False)
    return pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)


def run_experiment(screen):
    show_instructions("general_instructions.png", screen)

    for block_number in range(N_BLOCKS):
        run_block(screen, block_number)


def show_instructions(instructions_path, screen):
    screen.fill(BLACK)
    instructions = pygame.image.load(instructions_path)
    screen.blit(instructions, (0, 75))
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
    show_instructions(f"block_{block_number}_instructions.png", screen)
    REACTION_TIMES.append([])
    if block_number in [0, 1]:
        key = pygame.K_j
    elif block_number in [2, 3]:
        key = pygame.K_f
    for trial in range(N_TRIALS):
        run_trial(screen, key)


def run_trial(screen, key):
    while True:
        screen.fill(BLACK)
        r = screen.get_rect()

        waiting_time = random.randint(1000, 3000)
        pygame.display.update()
        pygame.time.delay(waiting_time)

        pygame.draw.circle(screen, WHITE, (r.width // 2, r.height // 2), 10)
        pygame.display.flip()
        t0 = pygame.time.get_ticks()

        if get_input() == key:
            REACTION_TIMES[-1].append(pygame.time.get_ticks() - t0)
            return


def close_window():
    pygame.quit()

if __name__ == '__main__':
    main()
