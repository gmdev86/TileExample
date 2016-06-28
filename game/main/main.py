import pygame
import pygame.locals
from level import *


def load_tile_table(filename, width, height):
    image = pygame.image.load(filename).convert()
    image_width, image_height = image.get_size()
    tile_table = []
    for tile_x in range(0, image_width/width):
        line = []
        tile_table.append(line)
        for tile_y in range(0, image_height/height):
            rect = (tile_x*width, tile_y*height, width, height)
            line.append(image.subsurface(rect))
    return tile_table

if __name__ == "__main__":
    screen = pygame.display.set_mode((424, 320))

    MAP_TILE_WIDTH = 24
    MAP_TILE_HEIGHT = 16
    MAP_CACHE = {
        'ground.png': load_tile_table('Resources/ground.png', MAP_TILE_WIDTH,
                                      MAP_TILE_HEIGHT),
    }

    level = Level()
    level.load_file('Resources/level.map')

    clock = pygame.time.Clock()

    background, overlay_dict = level.render(MAP_CACHE, MAP_TILE_HEIGHT, MAP_TILE_WIDTH)
    overlays = pygame.sprite.RenderUpdates()
    for (x, y), image in overlay_dict.iteritems():
        overlay = pygame.sprite.Sprite(overlays)
        overlay.image = image
        overlay.rect = image.get_rect().move(x * 24, y * 16 - 16)
    screen.blit(background, (0, 0))
    overlays.draw(screen)
    pygame.display.flip()

game_over = False
while not game_over:

    # XXX draw all the objects here

    overlays.draw(screen)
    pygame.display.flip()
    clock.tick(15)
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            game_over = True
        elif event.type == pygame.locals.KEYDOWN:
            pressed_key = event.key
