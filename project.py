import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

NTRIALS = 15  # Number of trials
OUTPUT_FILE = 'reaction_times.csv'

## Set up the experiment screen
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.mouse.set_visible(False)
r = screen.get_rect()
W, H = r.width, r.height
pygame.draw.line(screen, WHITE, (W // 2, 0), (W // 2, H))
pygame.display.flip()
#pygame.time.wait(2000) # As long as I don't have an escape button
reaction_times = []

#for ev in pygame.event.get():
#   if ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE:
#      pygame.quit()

# wait till the window is closed
done = False
while not done:
        for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        done = True






#try:
#    for t in range(NTRIALS):

#        pygame.draw.circle(screen, BLACK, (W // 2, H // 2), 4)
#        pygame.display.flip()
#        t0 = pygame.time.get_ticks()

#        buttonpressed = False
#        while not(buttonpressed):
#            for ev in pygame.event.get():
#                if ev.type == pygame.MOUSEBUTTONDOWN:
#                    t1 = pygame.time.get_ticks()
#                    buttonpressed = True
#                if ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE:
#                    raise Exception()
#        reaction_times.append(t1 - t0)

#        screen.fill(BLACK)
#        pygame.display.flip()

#except:
#    pass

#finally:
#    saveresults = open(OUTPUT_FILE, 'w')
#    saveresults.write('Trial,RT\n')
#    for t, r in enumerate(reaction_times):
#        saveresults.write(str(t) + ", " + str(r) + "\n")
#    saveresults.close()
#    pygame.quit()
