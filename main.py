import pygame as pg

def main():
  WINDOW_WIDTH = 800
  WINDOW_HEIGHT = 600
  FONT = pg.font.Font("/font/font.ttf", 20)

  pg.init()
  SCREEN = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
  CLOCK = pg.time.Clock()

  while 1:
    for event in pg.event.get():
      if event.type == pg.QUIT:
        pg.quit()
        exit()

    pg.display.update()
    CLOCK.tick(60)

if __name__ == '__main__':
  main()