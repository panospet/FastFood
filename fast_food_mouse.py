#!/usr/bin/python

import random
from gifimage import *

pygame.init()

# I use this font
monospace = pygame.font.SysFont("monospace", 25)
bigfont = pygame.font.SysFont("monospace", 60)

# load image
background_image = pygame.image.load("images/back_image.jpg")
backgroundRect = background_image.get_rect()

# set window
width = 1300
height = 700
size2 = (width, height)
screen = pygame.display.set_mode(size2)
print width, height

# my murray .gif pic
murray = GIFImage("images/little_murray.gif")
murray_width = murray.image.size[0]
murray_height = murray.image.size[1]

# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# game caption
pygame.display.set_caption('FastFood: A game for hungry people!')

# sounds
bite1 = pygame.mixer.Sound('sounds/bite1.wav')
bite2 = pygame.mixer.Sound('sounds/bite2.wav')
bite3 = pygame.mixer.Sound('sounds/bite3.wav')
bite4 = pygame.mixer.Sound('sounds/bite4.wav')
bite5 = pygame.mixer.Sound('sounds/bite5.wav')
bite_sounds_list = [bite1, bite2, bite3, bite4, bite5]
broken1 = pygame.mixer.Sound('sounds/broken1.wav')

a = []


# Randomly generated Items
class Item():
    def __init__(self, start_totalframes):
        self.totalframes = start_totalframes
        self.item_x = width

        number = random.randint(1, 5)
        if number == 1:
            self.icon = pygame.image.load("images/pitogyro.png")
            self.is_eatable = True
        elif number == 2:
            self.icon = pygame.image.load("images/coke.png")
            self.is_eatable = True
        elif number == 3:
            self.icon = pygame.image.load("images/nuggets.gif")
            self.is_eatable = True
        elif number == 4:
            self.icon = pygame.image.load("images/burger.png")
            self.is_eatable = True
        elif number == 5:
            self.icon = pygame.image.load("images/iron.png")
            self.is_eatable = False

        self.width, self.height = self.icon.get_size()
        self.item_y = random.randint(0, height - self.height)
        self.is_caught = False
        self.how_fast = random.randint(5, 10)

    def random_item_motion_and_catching(self, screen, item_x, item_y, how_fast, murray_x, murray_y, item_width,
                                        item_height, is_caught):

        item_x -= how_fast

        if item_x + item_width >= murray_x >= item_x and item_y + item_height >= murray_y >= item_y:
            is_caught = True
            item_x = -80

        elif item_x + item_width >= murray_x + murray_width >= item_x and item_y + item_height >= murray_y >= item_y:
            is_caught = True
            item_x = -80

        elif item_x + item_width >= murray_x >= item_x and item_y + item_height >= murray_y + murray_height >= item_y:
            is_caught = True
            item_x = -80

        elif item_x + item_width >= murray_x + murray_width >= item_x and item_y + item_height >= murray_y + murray_height >= item_y:
            is_caught = True
            item_x = -80

        elif item_y >= murray_y and item_y + item_height <= murray_y + murray_height and murray_x <= item_x <= murray_x + murray_width:
            is_caught = True
            item_x = -80

        elif item_x <= murray_x <= item_x + item_width and item_y >= murray_y and item_y + item_height <= murray_y + murray_height:
            is_caught = True
            item_x = -80

        else:
            screen.blit(self.icon, (item_x, item_y))

        return item_x, item_y, is_caught


def print_scores(time, score, teeth):
    timetext = monospace.render("time:" + str(time), 1, (255, 255, 255))
    scoretext = monospace.render("score:" + str(score), 1, (255, 255, 255))
    teethtext = monospace.render("teeth: " + str(teeth), 1, (255, 255, 255))
    screen.blit(timetext, (width - 200, 0))
    screen.blit(scoretext, (width - 200, 50))
    screen.blit(teethtext, (width - 200, 100))


def print_record(time, score):
    congrats = bigfont.render("Congrats", 1, (255, 255, 255))
    record_message = monospace.render("you reached " + str(score) + " points in " + str(time) + " seconds", 1,
                                      (255, 255, 255))
    screen.blit(congrats, (width / 5, height / 2 - 40))
    screen.blit(record_message, (width / 5, height / 2 + 30))

    replay_or_end = monospace.render("press R to replay or ESC to quit", 1, (255, 255, 255))
    screen.blit(replay_or_end, (width / 5, height / 2 + 200))


def play_bite_sound(is_eatable):
    if is_eatable:
        bite_sounds_list[random.randint(0, len(bite_sounds_list) - 1)].play()
    else:
        broken1.play()


def game():
    running = True

    # clock stuff
    clock = pygame.time.Clock()
    fps = 70
    totalframes = 0
    time = 0

    # frequency of items coming
    # freq = 100

    # scores
    score = 0
    teeth = 20

    # while my game is running loop
    while running:

        murray_x, murray_y = pygame.mouse.get_pos()

        # background
        screen.blit(background_image, backgroundRect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                # game ends with escape key
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_r:
                    running = False
                    game()

        # murray changed position
        if murray_y > height - murray_height:
            murray_y = height - murray_height
        if murray_y < 0:
            murray_y = 0
        murray.render(screen, (murray_x, murray_y))

        freq = random.randint(20, 50)
        freq = freq / 2

        if totalframes % freq == 0:
            a.append(Item(totalframes))

        for item in a:
            if totalframes > item.totalframes:
                item.item_x, item.item_y, item.is_caught = item.random_item_motion_and_catching(screen, item.item_x,
                                                                                                item.item_y,
                                                                                                item.how_fast,
                                                                                                murray_x, murray_y,
                                                                                                item.width,
                                                                                                item.height,
                                                                                                item.is_caught)
                if item.item_x < -80:
                    a.remove(item)
                    if item.is_caught:
                        play_bite_sound(item.is_eatable)
                        if item.is_eatable:
                            score += 1
                        else:
                            score -= 10
                            teeth -= 1
                    elif not item.is_caught:
                        if item.is_eatable:
                            score -= 3

        time = float(float(totalframes) / float(fps))
        print_scores(time, score, teeth)

        c = clock.tick(fps)
        pygame.display.update()
        totalframes += 1

        if score >= 50:
            running = False
            the_end(time, score)

        if teeth == 0:
            running = False
            out_of_teeth(time)


def the_end(time, score):
    screen = pygame.display.set_mode(size2)
    screen.blit(background_image, backgroundRect)

    the_end_running = True

    # clock stuff
    clock = pygame.time.Clock()
    fps = 100
    total_frames = 0

    while the_end_running:
        pygame.display.update()
        print_record(time, score)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    the_end_running = False
                if event.key == pygame.K_r:
                    the_end_running = False
                    game()
    c = clock.tick(fps)
    total_frames += 1


def out_of_teeth(time):
    screen = pygame.display.set_mode(size2)
    screen.blit(background_image, backgroundRect)

    teeth_running = True

    # clock stuff
    clock = pygame.time.Clock()
    fps = 100
    totalframes = 0

    while teeth_running:
        pygame.display.update()
        no_teeth = monospace.render("You lotht all your teeth, thtupid.", 1, (255, 255, 255))
        screen.blit(no_teeth, (width / 2 - 200, height / 2))
        timetext = monospace.render("time: " + str(time), 1, (255, 255, 255))
        screen.blit(timetext, (width / 2 - 200, height / 2 + 40))
        thwag = pygame.image.load("images/noteeth.jpg")
        screen.blit(thwag, (100, 200))
        replay_or_end = monospace.render("press R to replay or ESC to quit", 1, (255, 255, 255))
        screen.blit(replay_or_end, (width / 5, height / 2 + 200))

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    teeth_running = False
                if event.key == pygame.K_r:
                    teeth_running = False
                    game()
    c = clock.tick(fps)
    totalframes += 1

if __name__ == '__main__':
    game()
