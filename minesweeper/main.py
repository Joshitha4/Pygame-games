import pygame
from settings import *
from sprites import *
import random
import asyncio
import os

# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# DARKGREY = (40, 40, 40)
# LIGHTGREY = (100, 100, 100)
# GREEN = (0, 255, 0)
# DARKGREEN = (0, 200, 0)
# BLUE = (0, 0, 255)
# RED = (255, 0, 0)
# YELLOW = (255, 255, 0)
# BGCOLOUR = DARKGREY

# # game settings
# TILESIZE = 40
# ROWS = 15
# COLS = 15
# AMOUNT_MINES = 15
# WIDTH = TILESIZE * ROWS
# HEIGHT = TILESIZE * COLS
# FPS = 60
# TITLE = "Heartbreaker"
# pygame.font.init()
# pygame.mixer.init()
# # CLICK = pygame.mixer.Sound(os.path.join("assets", "audio_assets", "mixkit-arcade-game-jump-coin-216.wav"))
# # WIN = pygame.mixer.Sound(os.path.join("assets", "audio_assets", "mixkit-video-game-win-2016.wav"))
# # BG_MUSIC = pygame.mixer.Sound(os.path.join("assets", "audio_assets", "mixkit-video-game-win-2016.wav"))
# # LOSE = pygame.mixer.Sound(os.path.join("assets", "audio_assets", "mixkit-horror-lose-2028.wav"))
# FONT = pygame.font.Font(os.path.join("assets","fonts","PixelifySans-VariableFont_wght.ttf"), 60)
# tile_numbers = []
# for i in range(1, 9):
#     tile_numbers.append(pygame.transform.scale(pygame.image.load(os.path.join("assets", f"no{i}.png")), (TILESIZE, TILESIZE)))

# tile_empty = pygame.transform.scale(pygame.image.load(os.path.join("assets", "empty.png")), (TILESIZE, TILESIZE))
# tile_exploded = pygame.transform.scale(pygame.image.load(os.path.join("assets", "broken_heart.png")), (TILESIZE, TILESIZE))
# tile_flag = pygame.transform.scale(pygame.image.load(os.path.join("assets", "flag_heart.png")), (TILESIZE, TILESIZE))
# tile_mine = pygame.transform.scale(pygame.image.load(os.path.join("assets", "red_heart.png")), (TILESIZE, TILESIZE))
# tile_unknown = pygame.transform.scale(pygame.image.load(os.path.join("assets", "guess.png")), (TILESIZE, TILESIZE))
# tile_not_mine = pygame.transform.scale(pygame.image.load(os.path.join("assets", "flag_heart.png")), (TILESIZE, TILESIZE))
# full_cracked = pygame.transform.scale(pygame.image.load(os.path.join("assets", "animation", "full_cracked.png")), (50, 50))
# full_board = pygame.transform.scale(pygame.image.load(os.path.join("assets", "animation", "heartbreaker.png")), (600, 600))
# sprite_sheet = pygame.transform.scale(pygame.image.load(os.path.join("assets", "animation", "heart_sprite.png")), (600, 40))
# win_red = pygame.transform.scale(pygame.image.load(os.path.join("assets", "animation","win-red.png")), (600, 600))
# win_pink = pygame.transform.scale(pygame.image.load(os.path.join("assets", "animation","win-pink.png")), (600, 600))

# crack_animation = []
# crack_animation.append(pygame.transform.scale(pygame.image.load(os.path.join("assets", "animation", "full_heart.png")), (600, 600)))
# for i in range(1,12):
#     crack_animation.append(pygame.transform.scale(pygame.image.load(os.path.join("assets", "animation", f"almost{12-i}.png")), (600, 600)))

# crack_animation.append(pygame.transform.scale(pygame.image.load(os.path.join("assets", "animation", "full_cracked.png")), (600, 600)))
# crack_animation.append(pygame.transform.scale(pygame.image.load(os.path.join("assets", "animation", "full_cracked.png")), (600, 600)))
# for i in range(1,8):
#     crack_animation.append(pygame.transform.scale(pygame.image.load(os.path.join("assets", "animation", f"broken{i}.png")), (600, 600)))
# # for i in range(1,10):
# #     crack_animation.append(pygame.transform.scale(pygame.image.load(os.path.join("assets", "animation", "finaltext.png")), (600, 600)))


# class Tile:
#     def __init__(self, x, y, image, type, revealed=False, flagged=False):
#         self.x, self.y = x * TILESIZE, y * TILESIZE
#         self.image = image
#         self.type = type
#         self.revealed = revealed
#         self.flagged = flagged

#     def draw(self, board_surface):
#         if not self.flagged and self.revealed:
#             board_surface.blit(self.image, (self.x, self.y))
#         elif self.flagged and not self.revealed:
#             board_surface.blit(tile_flag, (self.x, self.y))
#         elif not self.revealed:
#             board_surface.blit(tile_unknown, (self.x, self.y))
#     def __repr__(self):
#         return self.type


# class Board:
#     def __init__(self):
#         self.board_surface = pygame.Surface((WIDTH, HEIGHT))
#         self.board_list = [[Tile(col, row, tile_empty, ".") for row in range(ROWS)] for col in range(COLS)]
#         self.place_mines()
#         self.place_clues()
#         self.dug = []

#     def place_mines(self):
#         for _ in range(AMOUNT_MINES):
#             while True:
#                 x = random.randint(0, ROWS-1)
#                 y = random.randint(0, COLS-1)

#                 if self.board_list[x][y].type == ".":
#                     self.board_list[x][y].image = tile_mine
#                     self.board_list[x][y].type = "X"
#                     break

#     def place_clues(self):
#         for x in range(ROWS):
#             for y in range(COLS):
#                 if self.board_list[x][y].type != "X":
#                     total_mines = self.check_neighbours(x, y)
#                     if total_mines > 0:
#                         self.board_list[x][y].image = tile_numbers[total_mines-1]
#                         self.board_list[x][y].type = "C"

#     def win_animation(self):
#         clock = pygame.time.Clock()
#         window = pygame.display.set_mode((600,600))
#         window.blit(full_board, (0, 0))
#         pygame.display.flip()
#         x = 280
#         y = 280
#         for k in range(0,8):
#             round_min = 280 - k*40
#             round_max = 280 + k*40
#             # print((2*k+1)**2)
#             if k == 0:
#                 clock.tick(5)
#                 pink = win_pink.subsurface(x,y,40,40)
#                 window.blit(pink, (x,y))
#                 pygame.display.flip()
#                 x+=40
#                 # start_x = x+40
#                 # start_y = y
#             count = 0
#             for l in range(0,8*k):
#                 clock.tick(10+5*k)
#                 pink = win_pink.subsurface(x,y,40,40)
#                 window.blit(pink, (x,y))
#                 pygame.display.flip()
#                 # print(k)
#                 # print(f"This x {x} & y {y} & r_max {round_max}& r_min {round_min}")
#                 if x == round_max and y == round_min:
#                     print("mxmi")
#                     x+=40
#                 elif x == round_max and y == round_max:
#                     print("mxmx")
#                     x-=40
#                 elif x == round_min and y == round_max:
#                     print("mimx")
#                     y-=40
#                 elif x == round_min and y == round_min:
#                     print("mimi")
#                     x+=40
#                 elif x == round_max and y < round_max:
#                     print("mxx")
#                     y+=40
#                 elif y == round_max and x > round_min:
#                     print("mxy")
#                     x-=40
#                 elif x == round_min and y > round_min:
#                     print("mix")
#                     y-=40
#                 elif y == round_min and x < round_max:
#                     print("miy")
#                     x+=40

#         odd = True
#         while True:
#             clock.tick(1)
#             if odd:
#                 window.blit(win_red, (0,0))
#                 pygame.display.flip()
#                 odd = False
#             else:
#                 window.blit(win_pink, (0,0))
#                 pygame.display.flip()
#                 odd = True
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     pygame.quit()
#                     quit(0)
#                 if event.type == pygame.MOUSEBUTTONDOWN:
#                     return

            
#     def heartbreak_animation(self):
#         window = pygame.display.set_mode((600, 600))
#         clock = pygame.time.Clock()
#         value = 0
#         print(value)
#         run = True
#         while run:
#             # print("hiii")
#             clock.tick(5)
#             if value >=len(crack_animation):
#                 break
#             image = crack_animation[value]
#             window.blit(image, (0, 0))
#             pygame.display.update()
#             if value == len(crack_animation)-1:
#                 self.text_animation(window)
#             window.fill((0, 0, 0))
#             value += 1


#     def text_animation(self, window):
#         clock = pygame.time.Clock()
#         speed = 3
#         counter = 0
#         message =  ""
#         word_lst = ["Game", "Over!"]
#         font = FONT
#         snip = font.render('', True, (162,25,25)) 
#         odd = True 
#         while True:
#             count = 0
#             if counter>=len(word_lst):
#                 clock.tick(3)
#                 if odd:
#                     for i in range(0,12):
#                             image = full_cracked
#                             window.blit(image, (50*i,0))
#                             window.blit(image, (50*i, 550))
#                     pygame.display.flip()
#                     odd = False
#                 else:
#                     for i in range(0,12):
#                         image = pygame.transform.scale(pygame.image.load(os.path.join("assets", "animation", f"broken4.png")), (50, 50))
#                         window.blit(image, (50*i,0))
#                         window.blit(image, (50*i, 550))
#                     pygame.display.flip()
#                     odd = True
#                 for event in pygame.event.get():
#                     if event.type == pygame.QUIT:
#                         pygame.quit()
#                         quit(0)
#                     if event.type == pygame.MOUSEBUTTONDOWN:
#                         return
#             else:
#                 while True:
#                     clock.tick(30)
#                     if count < speed*len(word_lst[counter]):
#                         count+=1
#                     else:
#                         break
#                     snip = font.render(word_lst[counter][0:count//speed], True, (162,25,25))
#                     pygame.draw.rect(window, (255,175,175), [210, 210+80*counter, 190, 80])
#                     if counter==0:
#                         x=230
#                     elif counter==1:
#                         x=230
#                     elif counter == 2:
#                         x=280
#                     elif counter == 3:
#                         x=290
#                     elif counter == 4:
#                         x=260
#                     window.blit(snip, (x,220+80*counter))
#                     for i in range(0,12):
#                         image = full_cracked
#                         window.blit(image, (50*i,0))
#                         window.blit(image, (50*i, 550))
#                         # pygame.display.update()
#                     pygame.display.flip()
#                 counter+=1

#     @staticmethod
#     def is_inside(x, y):
#         return 0 <= x < ROWS and 0 <= y < COLS

#     def check_neighbours(self, x, y):
#         total_mines = 0
#         for x_offset in range(-1, 2):
#             for y_offset in range(-1, 2):
#                 neighbour_x = x + x_offset
#                 neighbour_y = y + y_offset
#                 if self.is_inside(neighbour_x, neighbour_y) and self.board_list[neighbour_x][neighbour_y].type == "X":
#                     total_mines += 1

#         return total_mines

#     def draw(self, screen):
#         for row in self.board_list:
#             for tile in row:
#                 tile.draw(self.board_surface)
#         screen.blit(self.board_surface, (0, 0))

#     def dig(self, x, y):
#         self.dug.append((x, y))
#         if self.board_list[x][y].type == "X":
#             self.board_list[x][y].revealed = True
#             self.board_list[x][y].image = tile_exploded
#             return False
#         elif self.board_list[x][y].type == "C":
#             self.board_list[x][y].revealed = True
#             return True

#         self.board_list[x][y].revealed = True

#         for row in range(max(0, x-1), min(ROWS-1, x+1) + 1):
#             for col in range(max(0, y-1), min(COLS-1, y+1) + 1):
#                 if (row, col) not in self.dug:
#                     self.dig(row, col)
#         return True

#     def display_board(self):
#         for row in self.board_list:
#             print(row)
        

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.animation_lst = crack_animation

    def new(self):
        self.board = Board()
        self.board.display_board()

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.draw()
        else:
            self.end_screen()

    def draw(self):
        self.screen.fill(BGCOLOUR)
        self.board.draw(self.screen)
        pygame.display.flip()

    def check_win(self):
        for row in self.board.board_list:
            for tile in row:
                if tile.type != "X" and not tile.revealed:
                    return False
        WIN.play()
        # BG_MUSIC.play()
        return True

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                CLICK.play()
                mx, my = pygame.mouse.get_pos()
                mx //= TILESIZE
                my //= TILESIZE

                if event.button == 1:
                    if not self.board.board_list[mx][my].flagged:
                        # dig and check if exploded
                        if not self.board.dig(mx, my):
                            # explode
                            for row in self.board.board_list:
                                for tile in row:
                                    if tile.flagged and tile.type != "X":
                                        tile.flagged = False
                                        tile.revealed = True
                                        tile.image = tile_not_mine
                                    elif tile.type == "X":
                                        tile.revealed = True
                            # self.animation = Animation(self.animation_lst)
                            LOSE.play()
                            # BG_MUSIC.play()
                            self.board.heartbreak_animation()
                            # self.animation.draw(self.board.board_surface)
                            self.playing = False

                if event.button == 3:
                    if not self.board.board_list[mx][my].revealed:
                        self.board.board_list[mx][my].flagged = not self.board.board_list[mx][my].flagged

                if self.check_win():
                    self.win = True
                    self.playing = False
                    for row in self.board.board_list:
                        for tile in row:
                            if not tile.revealed:
                                tile.flagged = True
                    self.board.win_animation()
                    WIN.stop()
                
                

    def end_screen(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit(0)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # BG_MUSIC.stop()
                    return

game = Game()
async def main():
    while True:
        game.new()
        game.run()
        await asyncio.sleep(0)  # Wait for 1 second before restarting the game
asyncio.run(main())

