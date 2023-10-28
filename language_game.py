import pygame

# pygame setup

pygame.init()

programIcon = pygame.image.load('icon.png')

pygame.display.set_icon(programIcon)

#screen setups
X, Y=1280, 720
screen = pygame.display.set_mode((X, Y))

pygame.display.set_caption('Language Game')
clock = pygame.time.Clock() #keeps track of time (FPs)
running = True
dt = 0 #delta time

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2) #middle

#loading images

cyrillic = pygame.image.load("cyrillic.png").convert()
greek = pygame.image.load("greek.png").convert()
hebrew = pygame.image.load("hebrew.png").convert()
burmese = pygame.image.load("burmese.png").convert()
chinese = pygame.image.load("chinese.png").convert()
japanese = pygame.image.load("japanese.png").convert()

#Displaying something

def display_something(text:str, position_X:int, position_Y:int, is_instruction=False):
    text_colour = (100, 150, 200)
    if is_instruction:
        text_colour = (50, 10, 0)

    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render(text, True, text_colour, None)
    textRect = text.get_rect()
    textRect.center = (position_X, position_Y)
    return text, textRect

#getting some sprites in the game

class SpriteObject(pygame.sprite.Sprite):
    def __init__(self, x, y,text, correction, is_correct = False):
        super().__init__()

        text_colour = (0, 150, 200)

        font = pygame.font.Font('freesansbold.ttf', 32)

        self.original_image = font.render(text, True, text_colour, None)
        self.hover_image = font.render(text, True, (255,255,255), None)
        if is_correct:
            self.click_image = font.render(correction, True, (120, 220, 120), None)
        else:
            self.click_image = font.render(correction, True, (240,140,140), None)

        self.image = self.original_image
        self.rect = self.image.get_rect(center=(x, y))

        self.hover = False
        self.clicked = False


    def update(self, event_list):
        mouse_pos = pygame.mouse.get_pos()
        mouse_buttons = pygame.mouse.get_pressed()

        self.hover = self.rect.collidepoint(mouse_pos)
        # self.hover = self.rect.collidepoint(mouse_pos) and any(mouse_buttons)

        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    self.clicked = not self.clicked
        self.image = self.click_image if self.clicked else (self.hover_image if self.hover else self.original_image)


instructions=display_something('Which alphabet is this?', X//2, 50, is_instruction=True)
next_question=display_something('To access the next question, just press "n" on your keyboard', X // 2, Y - 50)
final_message = display_something('Congratulations, you have completed the game!', X//2, Y//2)

#sprite_object = SpriteObject(*screen.get_rect().center, (128, 128, 0))
group = pygame.sprite.Group([
    SpriteObject(X // 2, Y // 2, "Cyrillic","Correct", is_correct=True),
    SpriteObject(X // 2, Y // 2 - 100, "Greek","Incorrect, bouh"),
    SpriteObject(X // 2, Y // 2 + 100, "Kannada","Incorrect, bouh"),
    SpriteObject(X // 2, Y // 2 + 200, "Latin","Incorrect, bouh")
])

group_1 = pygame.sprite.Group([
    SpriteObject(X // 2, Y // 2, "Arabic","Incorrect"),
    SpriteObject(X // 2, Y // 2 - 100, "Cyrillic","Incorrect, bouh"),
    SpriteObject(X // 2, Y // 2 + 100, "Ukrainian Cyrillic","Incorrect, bouh"),
    SpriteObject(X // 2, Y // 2 + 200, "Greek","Correct", is_correct=True)
])

group_2 = pygame.sprite.Group([
    SpriteObject(X // 2, Y // 2, "Kannada","Incorrect"),
    SpriteObject(X // 2, Y // 2 - 100, "Hebrew","Correct", is_correct=True),
    SpriteObject(X // 2, Y // 2 + 100, "Georgian","Incorrect, bouh"),
    SpriteObject(X // 2, Y // 2 + 200, "Devanagari","Incorrect, bouh")
])

group_3 = pygame.sprite.Group([
    SpriteObject(X // 2, Y // 2, "Hindi","Incorrect"),
    SpriteObject(X // 2, Y // 2 - 100, "Latin","Incorrect"),
    SpriteObject(X // 2, Y // 2 + 100, "Cherokee","Incorrect, bouh"),
    SpriteObject(X // 2, Y // 2 + 200, "Burmese","Correct",is_correct=True)
])

group_4 = pygame.sprite.Group([
    SpriteObject(X // 2, Y // 2, "Japanese","Correct", is_correct=True),
    SpriteObject(X // 2, Y // 2 - 100, "Devanagari","Incorrect"),
    SpriteObject(X // 2, Y // 2 + 100, "Armenian","Incorrect, bouh"),
    SpriteObject(X // 2, Y // 2 + 200, "Burmese","Incorrect")
])

group_5 = pygame.sprite.Group([
    SpriteObject(X // 2, Y // 2, "Cherokee","Incorrect"),
    SpriteObject(X // 2, Y // 2 - 100, "Japanese","Incorrect"),
    SpriteObject(X // 2, Y // 2 + 100, "Chinese","Correct", is_correct=True),
    SpriteObject(X // 2, Y // 2 + 200, "Korean","Incorrect")
])

change_question=False

i = 0

while running:

    event_list = pygame.event.get()

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window

    for event in event_list:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n:
                change_question=True
                i += 1

    #if change_question:
    if i == 0:
        # fill the screen with a color to wipe away anything from last frame
        screen.fill((220,240,240))

        screen.blit(cyrillic, (X / 2 - cyrillic.get_width() / 2, Y / 5 - cyrillic.get_height() / 5))

        group.update(event_list)
        group.draw(screen)

        #display instructions on the screen
        screen.blit(instructions[0], instructions[1])
        screen.blit(next_question[0], next_question[1])

    elif i == 1:
        screen.fill((220, 240, 240))
        screen.blit(greek, (X / 2 - greek.get_width() / 2, Y / 5 - greek.get_height() / 5))
        group_1.update(event_list)
        group_1.draw(screen)
        screen.blit(instructions[0], instructions[1])
        screen.blit(next_question[0], next_question[1])
        pygame.display.flip()

    elif i == 2:
        screen.fill((220, 240, 240))
        screen.blit(hebrew, (X / 2 - hebrew.get_width() / 2, Y / 5 - hebrew.get_height() / 5))
        group_2.update(event_list)
        group_2.draw(screen)
        screen.blit(instructions[0], instructions[1])
        screen.blit(next_question[0], next_question[1])
        pygame.display.flip()

    elif i == 3:
        screen.fill((220, 240, 240))
        screen.blit(burmese, (X / 2 - burmese.get_width() / 2, Y / 5 - burmese.get_height() / 5))
        group_3.update(event_list)
        group_3.draw(screen)
        screen.blit(instructions[0], instructions[1])
        screen.blit(next_question[0], next_question[1])
        pygame.display.flip()

    elif i == 4:
        screen.fill((220, 240, 240))
        screen.blit(japanese, (X / 2 - japanese.get_width() / 2, Y / 5 - japanese.get_height() / 5))
        group_4.update(event_list)
        group_4.draw(screen)
        screen.blit(instructions[0], instructions[1])
        screen.blit(next_question[0], next_question[1])
        pygame.display.flip()

    elif i == 5:
        screen.fill((220, 240, 240))
        screen.blit(chinese, (X / 2 - chinese.get_width() / 2, Y / 5 - chinese.get_height() / 5))
        group_5.update(event_list)
        group_5.draw(screen)
        screen.blit(instructions[0], instructions[1])
        screen.blit(next_question[0], next_question[1])
        pygame.display.flip()

    else:
        screen.fill((220, 240, 240))
        screen.blit(final_message[0], final_message[1])



    #pygame.draw.circle(screen, "blue", player_pos, 20)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt


    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()