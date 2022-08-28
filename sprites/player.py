import pygame as pg

class Player(pg.sprite.Sprite):
  def __init__(self):
    self.image = pg.image.load("/assets/player.png")
    self.rect = self.image.get_rect()

  def update():
    pass