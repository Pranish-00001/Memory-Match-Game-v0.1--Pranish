class GameTimer:

    def __init__(self):
        self.start_time = 0
        self.end_time = 0

    def start(self):
        import pygame
        self.start_time = pygame.time.get_ticks()

    def stop(self):
        import pygame
        self.end_time = pygame.time.get_ticks()

    def get_duration(self):
        elapsed = (self.end_time - self.start_time) / 1000

        minutes = int(elapsed // 60)
        seconds = int(elapsed % 60)

        return f"{minutes:02}:{seconds:02}"