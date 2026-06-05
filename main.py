import random
import pygame
from timer import GameTimer

from card import Card

pygame.init()

WIDTH = 900
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Memory Match")

BUTTON_WIDTH = 220
BUTTON_HEIGHT = 60
BUTTON_PADDING = 20

restart_rect = pygame.Rect(
    WIDTH // 2 - BUTTON_WIDTH // 2,
    HEIGHT // 2 + 50,
    BUTTON_WIDTH,
    BUTTON_HEIGHT
)

quit_rect = pygame.Rect(
    WIDTH // 2 - BUTTON_WIDTH // 2,
    HEIGHT // 2 + 50 + BUTTON_HEIGHT + BUTTON_PADDING,
    BUTTON_WIDTH,
    BUTTON_HEIGHT
)

ROWS = 5
COLS = 6

CARD_WIDTH = 100
CARD_HEIGHT = 100
PADDING = 15






grid_width = COLS * CARD_WIDTH + (COLS - 1) * PADDING
grid_height = ROWS * CARD_HEIGHT + (ROWS - 1) * PADDING

start_x = (WIDTH - grid_width) // 2
start_y = (HEIGHT - grid_height) // 2




first_card = None
second_card = None

flip_time = 0
game_won = False

timer = GameTimer()
timer.start()

def new_game():

    cards = []

    values = list(range(1, 16)) * 2
    random.shuffle(values)

    for row in range(ROWS):
        for col in range(COLS):

            x = start_x + col * (CARD_WIDTH + PADDING)
            y = start_y + row * (CARD_HEIGHT + PADDING)

            card = Card(x, y, CARD_WIDTH, CARD_HEIGHT)

            card.value = values.pop()

            cards.append(card)

    return cards
cards = new_game()

running = True



while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            mouse_pos = pygame.mouse.get_pos()
            
            
            if game_won:

                if restart_rect.collidepoint(mouse_pos):

                    cards = new_game()

                    first_card = None
                    second_card = None

                    flip_time = 0

                    game_won = False

                    timer = GameTimer()
                    timer.start()

                elif quit_rect.collidepoint(mouse_pos):

                    running = False

                continue


            for card in cards:

                if card.rect.collidepoint(mouse_pos):

                    if (
                        not card.flipped
                        and not card.matched
                        and second_card is None
                        ):

                        card.flipped = True

                        if first_card is None:
                            first_card = card

                        elif second_card is None:
                            second_card = card
                            flip_time = pygame.time.get_ticks()

                    break
    if first_card and second_card:

        current_time = pygame.time.get_ticks()

        if current_time - flip_time > 1000:

            if first_card.value == second_card.value:

                    first_card.matched = True
                    second_card.matched = True

            else:

                    first_card.flipped = False
                    second_card.flipped = False

            first_card = None
            second_card = None
    
    if all(card.matched for card in cards) and not game_won:
        game_won = True
        timer.stop()


    screen.fill((40, 40, 40))

    for card in cards:
        card.draw(screen)
   
   
   
    if game_won:

        font = pygame.font.SysFont(None, 72)

        text = font.render("YOU WIN!", True, (255, 215, 0))

        text_rect = text.get_rect(center=(WIDTH // 2, 60))


        
        screen.blit(text, text_rect)
        


        #TIMER
        time_font = pygame.font.SysFont(None, 42)

        time_text = time_font.render(
            f"Time: {timer.get_duration()}",
            True,
            (255, 255, 255)
        )

        time_rect = time_text.get_rect(
            center=(WIDTH // 2, 120)
        )

        screen.blit(time_text, time_rect)
        

        
        #Restart Button
        pygame.draw.rect(screen, (60, 180, 75), restart_rect)

        button_font = pygame.font.SysFont(None, 40)

        button_text = button_font.render(
            "PLAY AGAIN",
            True,
            (255, 255, 255)
        )

        button_rect = button_text.get_rect(center=restart_rect.center)

        screen.blit(button_text, button_rect)

        #Quit Button
        pygame.draw.rect(screen, (180, 60, 60), quit_rect)

        quit_text = button_font.render(
                "QUIT",
                True,
                (255, 255, 255)
            )

        quit_text_rect = quit_text.get_rect(
                center=quit_rect.center
            )

        screen.blit(quit_text, quit_text_rect)

        


    pygame.display.flip()

pygame.quit()