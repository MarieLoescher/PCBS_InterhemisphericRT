# Interhemispheric Transfer Times

## Introduction

The aim of this project was to create a simple experiment investigating interhemisheric transfer times (ITT). The design was based on the Poffenberger paradigm (Poffenberger, 1912, as cited by Marzi, 1999), in which ITT are inferred by the difference between the reponse time (RT) to a contralateral versus to an ipsolateral stimulus. The idea is to present a visual stimulus to only one of the two halves of the visual field, and to measure the RTs of a subject responding either with his contralateral or his ipsolateral hand.

There are several ways to implement this paradigm. At first, I wanted to lateralize the stimulus by presenting it either on the right or on the left of the screen. But I feared that screens might not be large enough to ensure that only one eye is seeing the stimulus. Poffenberger himself used a rotating chair to move the subjects so that the stimulus only hit the wanted part of the visual field. I finally chose to realize the paradigm by asking subjects to conceal one eye - but one could also implement it Poffenberger's way, as the stimulus is presented in the center of the screen in both cases.

The design of my experiment is the following:
- The stimulus is a white dot, appearing in random intervals between 1 and 3 seconds in the center of a full black screen. The task is to press either the 'F' key with the left or the 'J' key with the right index as fast as possible after stimulus onset.
- There are two factors with two levels each (4 conditions in total): At the beginning of each block, subjects are instructed to conceal either their right eye (L) or their left eye (R), while the other is seeing. They are then instructed to either respond ipsolaterally (i) or contralaterally (c) to the seeing eye (i.e. responding with right hand when right eye is seeing, or responding with left hand when right eye is seeing). This amounts to 4 blocks of 15 trials each: (1) R-i, (2) L-c, (3) R-c, (4) L-i.
- RTs are measured and stored as one file per subject. Each file gets a time stamp to be able to identify them.

To program this experience, I used PyGame from Python. I oriented myself along the guidelines on clean code I found through researching the topic, using for example an article (zedr, 2019) about the Python implementation of the book "Clean Code" by Robert C. Martin.


## Code documentation

The number of blocks `N_BLOCKS`, the number of trials per block `N_TRIALS` a well as other parameters like screen size or the name of the output file are put at the top of the script, readily adaptable if needed.

### Displaying instructions

To display the multi-line instructions, I used scaled .png images of the written text, stored in the code as `instruction_path`. The images are included on my Github repository. They are blitted at the coordinates (0, 75) because their height (450 pixel) was smaller than the screen height (600 pixel), but I needed the image to be vertically centered (line 41-46).

    def show_instructions(instructions_path, screen):
        screen.fill(BLACK)
        instructions = pygame.image.load(instructions_path)
        screen.blit(instructions, (0, 75))
        pygame.display.update()
        get_input()

### Block design and storing reaction times

The goal was to end up with one list `REACTION_TIMES`, itself containing one list of RTs per block. To make sure that only valid results were stored, I did not store RTs of trials where the subject responded with another key than the one asked for. This was important as, in my design, the subject always has both hands on the keyboard, and errors might happen. I thus defined a variable `key` per block (line 62-65):

    if block_number in [0, 1]:
        key = pygame.K_j
    elif block_number in [2, 3]:
        key = pygame.K_f

  and later used `key` to ensure only valid responses were stored into `REACTION_TIMES` (line 83-84):

    if get_input() == key:
        REACTION_TIMES[-1].append(pygame.time.get_ticks() - t0)

Errors of the subject might thus result in a variable number of recorded trials. I therefore ensured the function `run_trial()` keeps running until the wanted number of trials `N_TRIALS` is achieved, using a `while` loop that only gets to the end (and onto the next trial) if the correct key is pressed (lines 71, 83-85)

## Analyzing results

# Course Feedback
I started this course with a very rudimentary notion of programming with Python, gained through a 3-day crash course three years ago and since left untouched. Concretely, this meant I recognized basic notions (such as variables, functions and loops), but was not able to actively write my own simple code.
During this course, these notions were successfully refreshed. I learned (or re-learned) more or less everything I displayed through this project. I also learned about functions and packages more relevant to cognitive sciences, such as Expyriment, or how to measure time for an RT experiment such as here.

What I really liked about the course was the very useful and accessible script, the easy contact with the teacher, as well as the small exercices we did in the beginning that forced me to "throw myself into the cold water" by just getting to it and trying.

As there are no more introductory courses at the beginning of the semester like there were before, I think the course would greatly benefit from being separated into two or three levels. I had the feeling that half the class was bored and the other half lost and panicky.
Once the class is separated into distinct groups, there could then be a more structured class in which there is an alternation between a small lecture on a new concept, followed by a time of practice of the kind of the small exercises we did, and finally the common sharing of the solution. I felt like there could not be any structured class because people were not on the same page; and we could not discuss solutions as everyone did different exercises.

A last comment concerns the overlap with Datacamp, which was very confusing for beginners like me, especially when handling several programming languages at once. I believe the Cogmaster would greatly improve by mashing the PCBS and the Datacamp course together so as to create a meaningful and coordinated balance between lecture and practice.
