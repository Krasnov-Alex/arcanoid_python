
import pygame

WIDTH = 800
HEIGHT = 650
FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Player(pygame.sprite.Sprite):
  def __init__(self, kof, color, x, y):
      pygame.sprite.Sprite.__init__(self)
      self.image = pygame.Surface((x, y))
      self.image.fill(color)
      self.rect = self.image.get_rect()
      self.rect.center = ((WIDTH / 2), (HEIGHT - 100))
      self.speed = 8
      self.kof = kof

  def update(self):
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT and self.rect.left >= 0:
        self.rect.x -= self.speed
      if event.key == pygame.K_RIGHT and self.rect.right <= WIDTH:
        self.rect.x += self.speed
    if (self.rect.bottom >= qube.rect.bottom >= self.rect.top) and (qube.rect.right <= self.rect.right and qube.rect.left >= self.rect.left):
      qube.county = False
      global koef
      if qube.rect.center[0] < (self.rect.center[0] - 25):
        koef = 2.0
        qube.countx = False
      elif qube.rect.center[0] > (self.rect.center[0] + 25):
        koef = 2.0
        qube.countx = True
      elif qube.rect.center[0] < self.rect.center[0]:
        koef = 1.0
        qube.countx = False
      elif qube.rect.center[0] > self.rect.center[0]:
        koef = 1.0
        qube.countx = True

class Qube(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.Surface((26, 26))
    self.image.fill(RED)
    self.rect = self.image.get_rect()
    self.rect.center = ((WIDTH / 2), (HEIGHT / 2))
    self.countx = False
    self.county = False
    self.speed = 5

  def update(self):
    if self.countx:
      self.rect.x += self.speed * koef
    else:
      self.rect.x -= self.speed * koef
    if self.county:
      self.rect.y += self.speed
    else:
      self.rect.y -= self.speed
    if self.rect.right >= WIDTH:
        self.countx = False
    if self.rect.left <= 0:
        self.countx = True
    if self.rect.bottom >= HEIGHT:
        self.speed = 0
    if self.rect.top <= 0:
        self.county = True

koef = 1.0
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
player = Player(1.0, BLACK, 150, 26)
qube = Qube()

all_sprites.add(player, qube)

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()
    
    screen.fill(WHITE)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()

