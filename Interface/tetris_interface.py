import pygame
from Game import tetris
from Interface import music


class TetrisGameInterface:
    def __init__(self):
        pygame.init()
        self.music = music.Music()
        self.music.set_volume(0.4)
        self.active_mode = 0
        self.FPS = 3
        self.top_left_x = 100
        self.top_left_y = 30
        self.sc = pygame.display.set_mode((640, 600))
        self.sc.fill((0, 0, 0))
        self.start_button = pygame.Surface((200, 80))
        self.start_button.fill((178, 102, 255))
        self.start_button_rect = self.start_button.get_rect(topleft=(220, 250))
        self.f = pygame.font.Font(None, 80)
        self.sc.blit(self.start_button, self.start_button_rect)
        self.text_start = self.f.render('START', 1, (20, 20, 20))
        self.sc.blit(self.text_start, (230, 265))
        self.button_next_level = pygame.Surface((170, 40))
        self.button_next_level.fill((102, 255, 102))
        self.button_next_level_rect = self.button_next_level.get_rect(topleft=(100, 250))
        self.button_new_game = pygame.Surface((170, 40))
        self.button_new_game.fill((102, 178, 255))
        self.button_new_game_rect = self.button_new_game.get_rect(topleft=(370, 250))
        self.clock = pygame.time.Clock()
        self.game_logic = tetris.TetrisGameLogic()
        pygame.display.update()

    def draw_playing_area(self):
        pygame.draw.rect(self.sc, (204, 0, 255), (97, 27, 306, 516))
        pygame.draw.rect(self.sc, (0, 0, 0), (100, 30, 300, 510))
        return

    def show_score(self):
        pygame.draw.rect(self.sc, (0, 0, 0), (430, 40, 200, 100))
        f1 = pygame.font.Font(None, 36)
        text1 = f1.render('SCORE: ', 1, (204, 0, 0))
        text_score = f1.render(str(self.game_logic.score), 1, (255, 255, 255))
        self.sc.blit(text1, (430, 40))
        self.sc.blit(text_score, (530, 40))
        return

    def show_level(self):
        pygame.draw.rect(self.sc, (0, 0, 0), (430, 100, 200, 50))
        f2 = pygame.font.Font(None, 36)
        text_level = f2.render('LEVEL: ', 1, (0, 0, 204))
        text_num_level = f2.render(str(self.game_logic.level), 1, (255, 255, 255))
        self.sc.blit(text_level, (430, 100))
        self.sc.blit(text_num_level, (530, 100))

    def draw_frame_for_next_shape(self):
        pygame.draw.rect(self.sc, (0, 0, 0), (430, 150, 170, 200))
        f3 = pygame.font.Font(None, 36)
        text_next_shape = f3.render('NEXT SHAPE:', 1, (0, 220, 0))
        self.sc.blit(text_next_shape, (430, 160))
        for i in self.game_logic.next_shape.coordinates:
            x, y = (i[1]-2), i[0]
            pygame.draw.rect(self.sc, self.game_logic.next_shape.color, (x*30 + 440, y*30 + 210, 30, 30))
            pygame.draw.rect(self.sc, (140, 140, 140), (x*30 + 440, y*30 + 210, 30, 30), 1)
        return

    def draw_squares(self, active_mode):
        if active_mode:
            supposed_coordinates = self.game_logic.find_where_fall()
            for i in range(len(self.game_logic.field.grid)):
                for j in range(len(self.game_logic.field.grid[i])):
                    x, y = j * 30, i * 30
                    # maybe add  (and active_mode) in the if
                    if [i, j] in self.game_logic.current_shape.coordinates:
                        pygame.draw.rect(self.sc, self.game_logic.current_shape.color, (x + self.top_left_x, y + self.top_left_y, 30, 30))
                        pygame.draw.rect(self.sc, (140, 140, 140), (x + self.top_left_x, y + self.top_left_y, 30, 30), 1)
                    else:
                        if [i, j] in supposed_coordinates:
                            pygame.draw.rect(self.sc, (25, 25, 25), (x + self.top_left_x, y + self.top_left_y, 30, 30))
                        else:
                            pygame.draw.rect(self.sc, self.game_logic.field.grid[i][j], (x + self.top_left_x, y + self.top_left_y, 30, 30))
                            if self.game_logic.field.grid[i][j] != (0, 0, 0):
                                pygame.draw.rect(self.sc, (140, 140, 140), (x + self.top_left_x, y + self.top_left_y, 30, 30),1)

    def query_about_next_level(self):
        surf = pygame.Surface((640, 140))
        surf.fill((180, 180, 180))
        surf.set_alpha(220)
        surf_rect = surf.get_rect(topleft=(0, 200))
        self.sc.blit(surf, surf_rect)
        self.sc.blit(self.button_next_level, self.button_next_level_rect)
        pygame.draw.rect(self.sc, (90, 90, 90), (100, 250, 170, 40), 3)
        f_next_level = pygame.font.Font(None, 36)
        text_next_level = f_next_level.render('NEXT LEVEL', 1, (50, 50, 50))
        self.sc.blit(text_next_level, (110, 260))
        self.sc.blit(self.button_new_game, self.button_new_game_rect)
        pygame.draw.rect(self.sc, (90, 90, 90), (370, 250, 170, 40), 3)
        f_new_game = pygame.font.Font(None, 36)
        text_new_game = f_new_game.render('NEW GAME', 1, (50, 50, 50))
        self.sc.blit(text_new_game, (384, 260))
        pygame.display.update()

    def start_next_level(self):
        pygame.draw.rect(self.sc, (0, 0, 0), (0, 0, 640, 600))
        self.game_logic.next_level()
        self.draw_playing_area()
        self.draw_frame_for_next_shape()
        pygame.display.update()
        self.FPS += 3
        active_mode = True
        return active_mode

    def start_new_game(self):
        self.game_logic.__init__()
        pygame.draw.rect(self.sc, (0, 0, 0), (0, 0, 640, 600))
        self.draw_playing_area()
        self.draw_frame_for_next_shape()
        pygame.display.update()
        self.FPS = 3
        active_mode = True
        return active_mode

    def start(self):
        active_mode = False
        while True:
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    exit()
                elif i.type == pygame.MOUSEBUTTONDOWN:
                    if self.start_button_rect.collidepoint(i.pos):
                        active_mode = self.start_new_game()
                    if self.button_next_level_rect.collidepoint(i.pos):
                        active_mode = self.start_next_level()
                    if self.button_new_game_rect.collidepoint(i.pos):
                        active_mode = self.start_new_game()
                elif i.type == pygame.KEYDOWN:
                    if i.key == pygame.K_LEFT:
                        if self.game_logic.current_shape.check_the_left_position(self.game_logic.field):
                            self.draw_squares(active_mode)
                            pygame.display.update()
                            self.draw_playing_area()
                    elif i.key == pygame.K_RIGHT:
                        if self.game_logic.current_shape.check_the_right_position(self.game_logic.field):
                            self.draw_squares(active_mode)
                            pygame.display.update()
                            self.draw_playing_area()
                    elif i.key == pygame.K_DOWN:
                        step = 3
                        if 15 - self.game_logic.current_shape.coordinates[3][0] < 3:
                            step = 15 - self.game_logic.current_shape.coordinates[3][0]
                        if self.game_logic.move(step):
                            self.draw_squares(active_mode)
                            pygame.display.update()
                            self.draw_playing_area()
                    elif i.key == pygame.K_UP:
                        self.game_logic.current_shape.change_shape(self.game_logic.field)
                        self.draw_squares(active_mode)
                        pygame.display.update()
                        self.draw_playing_area()

            if active_mode:
                if self.game_logic.move(1):
                    self.draw_squares(active_mode)
                    self.draw_frame_for_next_shape()
                    self.clock.tick(self.FPS)
                    self.show_score()
                    self.show_level()
                    pygame.display.update()
                    if self.game_logic.delete_filled_lines():
                        self.music.sound_play()
                        self.draw_playing_area()
                        self.draw_squares(active_mode)
                        pygame.display.update()
                    self.draw_playing_area()
                else:
                    self.draw_squares(active_mode)
                    pygame.display.update()
                    active_mode = False
                    self.query_about_next_level()
