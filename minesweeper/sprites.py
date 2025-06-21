import random
import pygame
from settings import *

# types list
# "." -> unknown
# "X" -> mine
# "C" -> clue
# "/" -> empty

class Tile:
    def __init__(self, x, y, image, type, revealed=False, flagged=False):
        self.x, self.y = x * TILESIZE, y * TILESIZE
        self.image = image
        self.type = type
        self.revealed = revealed
        self.flagged = flagged

    def draw(self, board_surface):
        if not self.flagged and self.revealed:
            board_surface.blit(self.image, (self.x, self.y))
        elif self.flagged and not self.revealed:
            board_surface.blit(tile_flag, (self.x, self.y))
        elif not self.revealed:
            board_surface.blit(tile_unknown, (self.x, self.y))
    def __repr__(self):
        return self.type


class Board:
    def __init__(self):
        self.board_surface = pygame.Surface((WIDTH, HEIGHT))
        self.board_list = [[Tile(col, row, tile_empty, ".") for row in range(ROWS)] for col in range(COLS)]
        self.place_mines()
        self.place_clues()
        self.dug = []

    def place_mines(self):
        for _ in range(AMOUNT_MINES):
            while True:
                x = random.randint(0, ROWS-1)
                y = random.randint(0, COLS-1)

                if self.board_list[x][y].type == ".":
                    self.board_list[x][y].image = tile_mine
                    self.board_list[x][y].type = "X"
                    break

    def place_clues(self):
        for x in range(ROWS):
            for y in range(COLS):
                if self.board_list[x][y].type != "X":
                    total_mines = self.check_neighbours(x, y)
                    if total_mines > 0:
                        self.board_list[x][y].image = tile_numbers[total_mines-1]
                        self.board_list[x][y].type = "C"

    def win_animation(self):
        clock = pygame.time.Clock()
        window = pygame.display.set_mode((600,600))
        window.blit(full_board, (0, 0))
        pygame.display.flip()
        x = 280
        y = 280
        for k in range(0,8):
            round_min = 280 - k*40
            round_max = 280 + k*40
            # print((2*k+1)**2)
            if k == 0:
                clock.tick(5)
                pink = win_pink.subsurface(x,y,40,40)
                window.blit(pink, (x,y))
                pygame.display.flip()
                x+=40
                # start_x = x+40
                # start_y = y
            count = 0
            for l in range(0,8*k):
                clock.tick(10+5*k)
                pink = win_pink.subsurface(x,y,40,40)
                window.blit(pink, (x,y))
                pygame.display.flip()
                # print(k)
                # print(f"This x {x} & y {y} & r_max {round_max}& r_min {round_min}")
                if x == round_max and y == round_min:
                    print("mxmi")
                    x+=40
                elif x == round_max and y == round_max:
                    print("mxmx")
                    x-=40
                elif x == round_min and y == round_max:
                    print("mimx")
                    y-=40
                elif x == round_min and y == round_min:
                    print("mimi")
                    x+=40
                elif x == round_max and y < round_max:
                    print("mxx")
                    y+=40
                elif y == round_max and x > round_min:
                    print("mxy")
                    x-=40
                elif x == round_min and y > round_min:
                    print("mix")
                    y-=40
                elif y == round_min and x < round_max:
                    print("miy")
                    x+=40

        odd = True
        while True:
            clock.tick(1)
            if odd:
                window.blit(win_red, (0,0))
                pygame.display.flip()
                odd = False
            else:
                window.blit(win_pink, (0,0))
                pygame.display.flip()
                odd = True
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit(0)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return

            
    def heartbreak_animation(self):
        window = pygame.display.set_mode((600, 600))
        clock = pygame.time.Clock()
        value = 0
        print(value)
        run = True
        while run:
            # print("hiii")
            clock.tick(5)
            if value >=len(crack_animation):
                break
            image = crack_animation[value]
            window.blit(image, (0, 0))
            pygame.display.update()
            if value == len(crack_animation)-1:
                self.text_animation(window)
            window.fill((0, 0, 0))
            value += 1


    def text_animation(self, window):
        clock = pygame.time.Clock()
        speed = 3
        counter = 0
        message =  ""
        word_lst = ["Game", "Over!"]
        font = FONT
        snip = font.render('', True, (162,25,25)) 
        odd = True 
        while True:
            count = 0
            if counter>=len(word_lst):
                clock.tick(3)
                if odd:
                    for i in range(0,12):
                            image = full_cracked
                            window.blit(image, (50*i,0))
                            window.blit(image, (50*i, 550))
                    pygame.display.flip()
                    odd = False
                else:
                    for i in range(0,12):
                        image = pygame.transform.scale(pygame.image.load(os.path.join("assets", "animation", f"broken4.png")), (50, 50))
                        window.blit(image, (50*i,0))
                        window.blit(image, (50*i, 550))
                    pygame.display.flip()
                    odd = True
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit(0)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        return
            else:
                while True:
                    clock.tick(30)
                    if count < speed*len(word_lst[counter]):
                        count+=1
                    else:
                        break
                    snip = font.render(word_lst[counter][0:count//speed], True, (162,25,25))
                    pygame.draw.rect(window, (255,175,175), [210, 210+80*counter, 190, 80])
                    if counter==0:
                        x=230
                    elif counter==1:
                        x=230
                    elif counter == 2:
                        x=280
                    elif counter == 3:
                        x=290
                    elif counter == 4:
                        x=260
                    window.blit(snip, (x,220+80*counter))
                    for i in range(0,12):
                        image = full_cracked
                        window.blit(image, (50*i,0))
                        window.blit(image, (50*i, 550))
                        # pygame.display.update()
                    pygame.display.flip()
                counter+=1

    @staticmethod
    def is_inside(x, y):
        return 0 <= x < ROWS and 0 <= y < COLS

    def check_neighbours(self, x, y):
        total_mines = 0
        for x_offset in range(-1, 2):
            for y_offset in range(-1, 2):
                neighbour_x = x + x_offset
                neighbour_y = y + y_offset
                if self.is_inside(neighbour_x, neighbour_y) and self.board_list[neighbour_x][neighbour_y].type == "X":
                    total_mines += 1

        return total_mines

    def draw(self, screen):
        for row in self.board_list:
            for tile in row:
                tile.draw(self.board_surface)
        screen.blit(self.board_surface, (0, 0))

    def dig(self, x, y):
        self.dug.append((x, y))
        if self.board_list[x][y].type == "X":
            self.board_list[x][y].revealed = True
            self.board_list[x][y].image = tile_exploded
            return False
        elif self.board_list[x][y].type == "C":
            self.board_list[x][y].revealed = True
            return True

        self.board_list[x][y].revealed = True

        for row in range(max(0, x-1), min(ROWS-1, x+1) + 1):
            for col in range(max(0, y-1), min(COLS-1, y+1) + 1):
                if (row, col) not in self.dug:
                    self.dig(row, col)
        return True

    def display_board(self):
        for row in self.board_list:
            print(row)

# class Animation:
#     def __init__(self):


