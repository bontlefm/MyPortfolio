import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
TILE_SIZE = SCREEN_WIDTH // 8

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_BROWN = (118, 150, 86)
LIGHT_BROWN = (238, 238, 210)

# Load images
pieces = {
    'wP': pygame.image.load('WhitePawn.jpeg'), 
    'wR': pygame.image.load('WhiteRook.jpeg'),
    'wN': pygame.image.load('WhiteKnight.jpeg'),
    'wB': pygame.image.load('WhiteBishop.jpeg'),
    'wQ': pygame.image.load('WhiteQueen.jpeg'),
    'wK': pygame.image.load('WhiteKing.jpeg'),
    'bP': pygame.image.load('BlackPawn.jpeg'),
    'bR': pygame.image.load('BlackRook.jpg'),
    'bN': pygame.image.load('BlackKnight.jpeg'),
    'bB': pygame.image.load('BlackBishop.jpeg'),
    'bQ': pygame.image.load('BlackQueen.jpeg'),
    'bK': pygame.image.load('BlackKing.jpeg')
}

# Resize images
for key in pieces:
    pieces[key] = pygame.transform.scale(pieces[key], (TILE_SIZE, TILE_SIZE))

# Initial board setup
board = [
    ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
    ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
    ["--", "--", "--", "--", "--", "--", "--", "--"],
    ["--", "--", "--", "--", "--", "--", "--", "--"],
    ["--", "--", "--", "--", "--", "--", "--", "--"],
    ["--", "--", "--", "--", "--", "--", "--", "--"],
    ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
    ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
]

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Chess")

def draw_board():
    for row in range(8):
        for col in range(8):
            color = LIGHT_BROWN if (row + col) % 2 == 0 else DARK_BROWN
            pygame.draw.rect(screen, color, (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE))

def draw_pieces(board):
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if piece != "--":
                screen.blit(pieces[piece], (col * TILE_SIZE, row * TILE_SIZE))

def main():
    selected_piece = None
    running = True
    while running:
        draw_board()
        draw_pieces(board)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                col = pos[0] // TILE_SIZE
                row = pos[1] // TILE_SIZE
                if selected_piece:
                    board[row][col] = selected_piece
                    selected_piece = None
                else:
                    selected_piece = board[row][col]
                    board[row][col] = "--"

        pygame.display.flip()

if __name__ == "__main__":
    main()
