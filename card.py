import pygame


class Card:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

        self.value = None
        self.flipped = False
        self.matched = False

    def draw(self, screen):

        if self.matched:
            return

        if self.flipped:
            color = (220, 220, 220)

            pygame.draw.rect(screen, color, self.rect)
            pygame.draw.rect(screen, (0, 0, 0), self.rect, 2)

            font = pygame.font.SysFont(None, 36)

            text = font.render(str(self.value), True, (0, 0, 0))

            text_rect = text.get_rect(center=self.rect.center)

            screen.blit(text, text_rect)

        else:
            color = (70, 130, 180)

            pygame.draw.rect(screen, color, self.rect)
            pygame.draw.rect(screen, (0, 0, 0), self.rect, 2)