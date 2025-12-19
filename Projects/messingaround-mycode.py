class player(pygame.sprite.Sprite):
    def __init__(self, color, width, height, x, y):
        pygame.sprite.Sprite.__init__(self)
        self,image=pygame.surface((16,8),pygame.SRCALPHA)
        self.image.fill((0,255,0))
        self.image=pygame.transform.rotate(self.image, direction)
        self.pos=(x,y)        
        self.rect.x = 100
        self.rect.y = 10