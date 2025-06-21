# COLORS (r, g, b)
import pygame
import os

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
DARKGREEN = (0, 200, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BGCOLOUR = DARKGREY

# game settings
TILESIZE = 40
ROWS = 15
COLS = 15
AMOUNT_MINES = 15
WIDTH = TILESIZE * ROWS
HEIGHT = TILESIZE * COLS
FPS = 60
TITLE = "Heartbreaker"
pygame.font.init()
pygame.mixer.init()
CLICK = pygame.mixer.Sound(os.path.join("assets", "audio_assets", "mixkit-arcade-game-jump-coin-216.ogg"))
WIN = pygame.mixer.Sound(os.path.join("assets", "audio_assets", "retro-pop-beat-30063.ogg"))
BG_MUSIC = pygame.mixer.Sound(os.path.join("assets", "audio_assets", "mixkit-video-game-win-2016.ogg"))
LOSE = pygame.mixer.Sound(os.path.join("assets", "audio_assets", "mixkit-horror-lose-2028.ogg"))
FONT = pygame.font.Font(os.path.join("assets","fonts","PixelifySans-VariableFont_wght.ttf"), 60)
tile_numbers = []
for i in range(1, 9):
    tile_numbers.append(pygame.transform.scale(pygame.image.load(os.path.join("assets", f"no{i}.png")), (TILESIZE, TILESIZE)))

tile_empty = pygame.transform.scale(pygame.image.load(os.path.join("assets", "empty.png")), (TILESIZE, TILESIZE))
tile_exploded = pygame.transform.scale(pygame.image.load(os.path.join("assets", "broken_heart.png")), (TILESIZE, TILESIZE))
tile_flag = pygame.transform.scale(pygame.image.load(os.path.join("assets", "flag_heart.png")), (TILESIZE, TILESIZE))
tile_mine = pygame.transform.scale(pygame.image.load(os.path.join("assets", "red_heart.png")), (TILESIZE, TILESIZE))
tile_unknown = pygame.transform.scale(pygame.image.load(os.path.join("assets", "guess.png")), (TILESIZE, TILESIZE))
tile_not_mine = pygame.transform.scale(pygame.image.load(os.path.join("assets", "flag_heart.png")), (TILESIZE, TILESIZE))
full_cracked = pygame.transform.scale(pygame.image.load(os.path.join("assets", "animation", "full_cracked.png")), (50, 50))
full_board = pygame.transform.scale(pygame.image.load(os.path.join("assets", "animation", "heartbreaker.png")), (600, 600))
sprite_sheet = pygame.transform.scale(pygame.image.load(os.path.join("assets", "animation", "heart_sprite.png")), (600, 40))
win_red = pygame.transform.scale(pygame.image.load(os.path.join("assets", "animation","win-red.png")), (600, 600))
win_pink = pygame.transform.scale(pygame.image.load(os.path.join("assets", "animation","win-pink.png")), (600, 600))

crack_animation = []
crack_animation.append(pygame.transform.scale(pygame.image.load(os.path.join("assets", "animation", "full_heart.png")), (600, 600)))
for i in range(1,12):
    crack_animation.append(pygame.transform.scale(pygame.image.load(os.path.join("assets", "animation", f"almost{12-i}.png")), (600, 600)))

crack_animation.append(pygame.transform.scale(pygame.image.load(os.path.join("assets", "animation", "full_cracked.png")), (600, 600)))
crack_animation.append(pygame.transform.scale(pygame.image.load(os.path.join("assets", "animation", "full_cracked.png")), (600, 600)))
for i in range(1,8):
    crack_animation.append(pygame.transform.scale(pygame.image.load(os.path.join("assets", "animation", f"broken{i}.png")), (600, 600)))
# for i in range(1,10):
#     crack_animation.append(pygame.transform.scale(pygame.image.load(os.path.join("assets", "animation", "finaltext.png")), (600, 600)))

