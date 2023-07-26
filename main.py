
import pygame

WIDTH = 800
HEIGHT = 650
FPS = 30

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Board(pygame.sprite.Sprite):
    def __init__(self, cells):
        self.cells = cells

    def move(self, numb, symb):
        if self.cells[numb - 1].symb == ' ':
            self.cells[numb - 1].symb = symb
            return True
        else:
            print('Эта клетка уже занята, введите другое значение.')
            return False
            # self.move(numb, symb)         #PASS

    def grafic(self):
        print('[{}][{}][{}]'
              '\n[{}][{}][{}]'
              '\n[{}][{}][{}]'
              '\n'.format(
            self.cells[6].symb, self.cells[7].symb, self.cells[8].symb,
            self.cells[3].symb, self.cells[4].symb, self.cells[5].symb,
            self.cells[0].symb, self.cells[1].symb, self.cells[2].symb
        )
        )

    def end_game(self):
        if (self.cells[0].symb == self.cells[1].symb == self.cells[2].symb) and (self.cells[2].symb != '_'):
            return True
        elif (self.cells[3].symb == self.cells[4].symb == self.cells[5].symb) and (self.cells[5].symb != '_'):
            return True
        elif (self.cells[6].symb == self.cells[7].symb == self.cells[8].symb) and (self.cells[7].symb != '_'):
            return True
        elif (self.cells[0].symb == self.cells[3].symb == self.cells[6].symb) and (self.cells[6].symb != '_'):
            return True
        elif (self.cells[1].symb == self.cells[4].symb == self.cells[7].symb) and (self.cells[4].symb != '_'):
            return True
        elif (self.cells[2].symb == self.cells[5].symb == self.cells[8].symb) and (self.cells[5].symb != '_'):
            return True
        elif (self.cells[0].symb == self.cells[4].symb == self.cells[8].symb) and (self.cells[0].symb != '_'):
            return True
        return bool(self.cells[2].symb == self.cells[4].symb == self.cells[6].symb and self.cells[6].symb != '_')
    def check(self, cell1, cell2, cell3):
        if (cell1 != '_') and (cell2 != '_') and (cell3 != '_'):
            return True
        return False


class Cell(pygame.sprite.Sprite):
    def __init__(self, cel_x, cel_y):
      pygame.sprite.Sprite.__init__(self)
      self.image = pygame.Surface((40, 20))
      self.image.fill(BLUE)
      self.rect = self.image.get_rect()
      self.rect.center = ((WIDTH - cel_x), (HEIGHT - cel_y))
      self.symb = '_'

    def check(self):
        return self.symb == '_'


# class Xzc(pygame.sprite.Sprite):
  


class Player(pygame.sprite.Sprite):
  def __init__(self, kof, color, x, y):
      pygame.sprite.Sprite.__init__(self)
      self.image = pygame.Surface((x, y))
      self.image.fill(color)
      self.rect = self.image.get_rect()
      self.rect.center = ((WIDTH / 2), (HEIGHT - 100))
      # if cen == 1:
      #   self.rect.center = (((WIDTH / 2) - 50), (HEIGHT - 100))
      # if cen == 2:
      #   self.rect.center = ((WIDTH / 2), (HEIGHT - 100))
      # if cen == 3:
      #   self.rect.center = (((WIDTH / 2) + 50), (HEIGHT - 100))
      # self.countx = x
      # self.county = y
      self.speed = 8
      self.kof = kof
      # self.cen = cen
      
      
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

  # def updx(self):
  #   if self.countx:
  #     self.countx = False
  #   else:
  #     self.countx = True
      
  # def updy(self):
  #   if self.county:
  #     self.county = False
  #   else:
  #     self.county = True
    

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
    # if (player.rect.bottom >= self.rect.bottom >= player.rect.top) and (self.rect.right <= player.rect.right and self.rect.left >= player.rect.left):
    #   self.county = False
    if self.rect.top <= 0:
        self.county = True
    # print(self.rect.center[0], self.rect.center[1])

# Создаем игру и окно
koef = 1.0
pygame.init()
# pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
my_speed = 10
# player_left = Player(2.0, BLACK, 50, 26, 1)
player = Player(1.0, BLACK, 150, 26)
# player_right = Player(2.0, BLACK, 50, 26, 3)
qube = Qube()
cell1 = Cell(200, 200)
# cell2 = Cell()
# cell3 = Cell()
# cell4 = Cell()
# cell5 = Cell()
# cell6 = Cell()
# cell7 = Cell()
# cell8 = Cell()
# cell9 = Cell()

# list_cell = [cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9]
# board = Board(list_cell)
# player2 = Player(my_speed, BLUE, False, True)
# player3 = Player(my_speed, GREEN, False, False)
all_sprites.add(player, qube, cell1) #, player1, player2, player3

# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Обновление
    all_sprites.update()
    
    # Рендеринг
    screen.fill(WHITE)
    all_sprites.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()

