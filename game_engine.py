import pygame
import numpy as np
import random


def generate_random_board():

    board = np.array([
        [2048, 2048, 32, 32],
        [2048, 2048, 32, 32],
        [16, 16, 512, 512],
        [16, 16, 512, 512]
    ])

    return board



class Game2048:
    def __init__(self):
        self.size = 4
        self.board_hist = []
        self.board = np.zeros((self.size, self.size), dtype=int)
        self.score_hist = []
        self.score = 0
        self.undo_counts = 0
        self.reset()

    def reset(self):
        self.board = np.zeros((self.size, self.size), dtype=int)
        self.add_tile()
        self.add_tile()
        return self.board

    def add_tile(self):
        empty_positions = list(zip(*np.where(self.board == 0)))
        if empty_positions:
            row, col = empty_positions[random.choice(range(len(empty_positions)))]
            self.board[row, col] = 2 if random.random() < 0.9 else 4

    def move(self, direction):
        old_board = self.board.copy()
        if direction == 'left':
            self.board, score = self.slide_left(self.board)
        elif direction == 'up':
            transposed_board, score = self.slide_left(self.board.T)
            self.board = transposed_board.T
        elif direction == 'right':
            flipped_board, score = self.slide_left(np.fliplr(self.board))
            self.board = np.fliplr(flipped_board)
        elif direction == 'down':
            flipped_transposed_board, score = self.slide_left(np.fliplr(self.board.T))
            self.board = np.fliplr(flipped_transposed_board).T

        if (self.board != old_board).sum() > 0:
            self.board_hist.append(old_board)
            self.score_hist.append(self.score)
            self.add_tile()
        self.score += score
        print(self.score)

    def slide_left(self, board):
        new_board = np.zeros_like(board)
        score = 0
        for i in range(self.size):
            tiles = board[i][board[i] != 0]
            new_row = []
            skip = False
            for j in range(len(tiles)):
                if skip:
                    skip = False
                    continue
                if j + 1 < len(tiles) and tiles[j] == tiles[j + 1]:
                    new_row.append(2 * tiles[j])
                    score += 2 * tiles[j]
                    skip = True
                else:
                    new_row.append(tiles[j])
            new_board[i, :len(new_row)] = new_row
        return new_board, score

    def is_game_over(self):
        if np.any(self.board == 0):
            return False
        for i in range(self.size):
            for j in range(self.size - 1):
                if self.board[i, j] == self.board[i, j + 1] or self.board[j, i] == self.board[j + 1, i]:
                    return False
        return True

    def undo(self):
        if len(self.score_hist):
            self.score = self.score_hist[-1]
            self.score_hist = self.score_hist[:-1]
            self.board = self.board_hist[-1]
            self.board_hist = self.board_hist[:-1]
            self.undo_counts += 1

class Game2048GUI:
    def __init__(self, game):
        self.game = game
        self.size = game.size
        self.width = 1200
        self.height = 1200
        self.tile_size = self.width // self.size
        # self.colors = {
        #     0: (205, 193, 180),
        #     2: (238, 228, 218),
        #     4: (237, 224, 200),
        #     8: (242, 177, 121),
        #     16: (245, 149, 99),
        #     32: (246, 124, 95),
        #     64: (246, 94, 59),
        #     128: (237, 207, 114),
        #     256: (237, 204, 97),
        #     512: (0, 128, 128),  # Updated color
        #     1024: (0, 100, 128),  # Updated color
        #     2048: (0, 76, 153),  # Updated color
        #     4096: (0, 51, 102),  # Updated color
        #     8192: (0, 25, 51),  # Updated color
        # }
        self.colors = {
            0: (205, 193, 180),
            2: (238, 228, 218),
            4: (237, 224, 200),
            8: (242, 177, 121),
            16: (245, 149, 99),
            32: (246, 124, 95),
            64: (246, 94, 59),
            128: (237, 207, 114),
            256: (237, 204, 97),
            512: (237, 200, 80),
            1024: (237, 197, 63),
            2048: (237, 194, 46),
        }

        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("2048")

    def draw_board(self):
        self.screen.fill((187, 173, 160))
        for row in range(self.size):
            for col in range(self.size):
                value = self.game.board[row][col]
                color = self.colors.get(value, (60, 58, 50))
                rect = pygame.Rect(col * self.tile_size, row * self.tile_size, self.tile_size, self.tile_size)
                pygame.draw.rect(self.screen, color, rect)
                if value != 0:
                    font = pygame.font.Font(None, 72)
                    text = font.render(str(value), True, (119, 110, 101))
                    text_rect = text.get_rect(center=rect.center)
                    self.screen.blit(text, text_rect)

    def run(self):
        clock = pygame.time.Clock()
        running = True

        while running:
            pygame.display.set_caption(f"2048, Score: {game.score}, Undo: {game.undo_counts}")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.game.move('left')
                    elif event.key == pygame.K_RIGHT:
                        self.game.move('right')
                    elif event.key == pygame.K_UP:
                        self.game.move('up')
                    elif event.key == pygame.K_DOWN:
                        self.game.move('down')
                    elif event.key == pygame.K_SPACE:
                        self.game.undo()
                    elif event.key == pygame.K_ESCAPE:
                        running = False
                    elif event.key == pygame.K_r:
                        game.__init__()
                    if self.game.is_game_over():
                        # running = False
                        print("Game Over")

            self.draw_board()
            pygame.display.flip()
            clock.tick(30)

        pygame.quit()

if __name__ == "__main__":
    game = Game2048()
    gui = Game2048GUI(game)
    gui.run()
