import pygame
import sys
import os
pygame.init()

width, height = 400, 360  # 한 칸 넓이 50, 45
chessBoard = pygame.display.set_mode((width, height))
pygame.display.set_caption("PyChessGame")

white = (255, 255, 255)
black = (100, 100, 100)

# 체스 보드 그리기


def draw_chess_board():
    for row in range(8):
        for col in range(8):
            # 번갈아가며 사각형 그리기
            color = white if (row + col) % 2 == 0 else black
            pygame.draw.rect(chessBoard, color,
                             (col * (width//8), row * (height//8), 50, 50))


# 말 이미지 로드
piece_images = {}
for color in ["white", "black"]:
    for piece in ["pawn", "rook", "knight", "bishop", "queen", "king"]:
        piece_key = f"{color}_{piece}"
        piece_filename = f"{piece_key}.png"  # 파일 경로를 적절하게 수정
        piece_images[piece_key] = pygame.image.load(
            piece_filename).convert_alpha()
        piece_images[piece_key] = pygame.transform.scale(
            piece_images[piece_key], (width // 8, height // 8))

# 초기 말 이미지 표시 위치
piece_position = (width // 2 - piece_images["white_pawn"].get_width(
) // 2, height // 2 - piece_images["white_pawn"].get_height() // 2)

# 체스 보드 초기화


def initialize_board():
    board = [[0] * 8 for _ in range(8)]

    # 검은 말 초기화
    for col in range(8):
        board[6][col] = "black_pawn"
    board[7][0] = board[7][7] = "black_rook"
    board[7][1] = board[7][6] = "black_knight"
    board[7][2] = board[7][5] = "black_bishop"
    board[7][3] = "black_queen"
    board[7][4] = "black_king"

    # 흰 말 초기화
    for col in range(8):
        board[1][col] = "white_pawn"
    board[0][0] = board[0][7] = "white_rook"
    board[0][1] = board[0][6] = "white_knight"
    board[0][2] = board[0][5] = "white_bishop"
    board[0][3] = "white_queen"
    board[0][4] = "white_king"

    return board


# 각 말의 초기 위치를 나타내는 2차원 리스트
chess_board = initialize_board()

# 체스 보드 그리기
draw_chess_board()

# 말 이미지 표시
for row in range(8):
    for col in range(8):
        if chess_board[row][col] != 0:
            piece_key = chess_board[row][col]
            piece_position = (col * (width // 8), row * (height // 8))
            chessBoard.blit(piece_images[piece_key], piece_position)

# 업데이트된 화면을 표시
pygame.display.flip()


# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Pygame 종료
pygame.quit()
sys.exit()
