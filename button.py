import pygame
pygame.init()

WHITE = (255, 255, 255)
class Button:
    def __init__(self, x, y, width, height, color, text = ""):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text = text



    def draw_button(self, surface, outline = None):
        if outline:
            pygame.draw.rect(surface, outline, (self.x - 4, self.y -4, self.width + 8, self.height + 8))
        button = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(surface, self.color, button)

        if self.text != "":
            font = pygame.font.SysFont('comicsans', 40)
            text = font.render(self.text, 1, WHITE)
            surface.blit(text, (self.x + self.width // 2 - text.get_width() // 2,self.y +self.height // 2 - text.get_height() // 2) )


    def is_over(self, pos):
        return self.x < pos[0] <self.x + self.width and self.y < pos[1] <self.y + self.height
