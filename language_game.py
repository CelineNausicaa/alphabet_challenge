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

#Displaying something
def display_something(text:str, position_X:int, position_Y:int, is_instruction=False, is_hebrew = False):
    text_colour = (100, 150, 200)
    if is_instruction:
        text_colour = (50, 10, 0)
    if is_hebrew:
        font = pygame.font.SysFont('Cyberbit', 32)
    else:
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


instructions=display_something('Which alphabet is this?',X//2,50, is_instruction=True)
next_question=display_something('To access the next question, just press "n" on your keyboard', X // 2, Y - 50)

alphabet=display_something('абвгдеёжзийклмнопрстуфхцчшщъыьэюя ', X // 2, 100)

#sprite_object = SpriteObject(*screen.get_rect().center, (128, 128, 0))
group = pygame.sprite.Group([
    SpriteObject(X // 2, Y // 2, "Cyrillic","Correct", is_correct=True),
    SpriteObject(X // 2, Y // 2 - 100, "Greek","Incorrect, bouh"),
    SpriteObject(X // 2, Y // 2 + 100, "Kannada","Incorrect, bouh"),
    SpriteObject(X // 2, Y // 2 + 200, "Latin","Incorrect, bouh")
])

alphabet_1=display_something('αβγδεζηθικλμνξοπρςστυφχψ ', X // 2, 100)

group_1 = pygame.sprite.Group([
    SpriteObject(X // 2, Y // 2, "Arabic","Incorrect"),
    SpriteObject(X // 2, Y // 2 - 100, "Cyrillic","Incorrect, bouh"),
    SpriteObject(X // 2, Y // 2 + 100, "Ukrainian Cyrillic","Incorrect, bouh"),
    SpriteObject(X // 2, Y // 2 + 200, "Greek","Correct", is_correct=True)
])

#abcdefghijklmnopqrstuvwxyz
hebrew_alphabet = 'אבגדהוזחטיכךלמםנןסעפףצץקרשת'
alphabet_2=display_something(hebrew_alphabet, X // 2, 100, is_hebrew = True)

group_2 = pygame.sprite.Group([
    SpriteObject(X // 2, Y // 2, "Kannada","Incorrect"),
    SpriteObject(X // 2, Y // 2 - 100, "Latin","Correct", is_correct=True),
    SpriteObject(X // 2, Y // 2 + 100, "Georgian","Incorrect, bouh"),
    SpriteObject(X // 2, Y // 2 + 200, "Devanagari","Incorrect, bouh")
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
    if i == 1:
        screen.fill((220, 240, 240))
        group_1.update(event_list)
        group_1.draw(screen)
        screen.blit(instructions[0], instructions[1])
        screen.blit(alphabet_1[0],alphabet_1[1])
        screen.blit(next_question[0], next_question[1])
        pygame.display.flip()

    elif i == 2:
        screen.fill((220, 240, 240))
        group_2.update(event_list)
        group_2.draw(screen)
        screen.blit(instructions[0], instructions[1])
        screen.blit(alphabet_2[0],alphabet_2[1])
        screen.blit(next_question[0], next_question[1])
        pygame.display.flip()

    else:
        # fill the screen with a color to wipe away anything from last frame
        screen.fill((220,240,240))

        group.update(event_list)
        group.draw(screen)

        #display words on the screen
        screen.blit(instructions[0], instructions[1])
        screen.blit(alphabet[0], alphabet[1])
        screen.blit(next_question[0], next_question[1])


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