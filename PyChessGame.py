import pygame
from pygame.locals import QUIT, MOUSEBUTTONDOWN
import sys
import random

# pygame 초기화
pygame.init()

width, height = 400, 360  # 한 칸 넓이 50, 45
border_size = 40  # 여백 크기

chessBoard = pygame.display.set_mode(
    (width + 2 * border_size, height + 2 * border_size))
pygame.display.set_caption("PyChessGame")

white = (255, 255, 255)
black = (100, 100, 100)

# 초기 화면 설정
initial_screen = True
play_button_rect = pygame.Rect(
    150+border_size, 200+border_size, 100, 50)  # Play 버튼 위치 및 크기 설정

# 사운드 추가
pygame.mixer.init()
winSound = "sounds/win_sound.wav"
moveSound = "sounds/move_sound.wav"
win_sound = pygame.mixer.Sound(winSound)
move_sound = pygame.mixer.Sound(moveSound)


# 초기 화면 함수
def draw_initial_screen():
    background = pygame.image.load("images/background.png")  # 파일 경로를 적절하게 수정
    background = pygame.transform.scale(background, (480, 440))
    chessBoard.blit(background, (0, 0))
    font = pygame.font.Font(None, 45)

    font_title = pygame.font.Font(None, 70)  # PyChessGame 제목 폰트 크기 키우기
    font_button = pygame.font.Font(None, 36)  # 버튼 폰트 크기 설정

    # PyChessGame 제목 표시
    title_text = font_title.render("PyChessGame", True, (255, 255, 255))
    title_rect = title_text.get_rect(
        center=(width // 2+border_size, height // 3+border_size))
    chessBoard.blit(title_text, title_rect)

    # Play 버튼 그리기
    play_text_color = (255, 0, 0) if play_button_rect.collidepoint(
        pygame.mouse.get_pos()) else (0, 0, 0)
    pygame.draw.rect(chessBoard, (255, 255, 255), play_button_rect)
    pygame.draw.rect(chessBoard, (0, 0, 0), play_button_rect, 3)

    play_text = font.render("Play", True, play_text_color)
    play_rect = play_text.get_rect(center=play_button_rect.center)
    chessBoard.blit(play_text, play_rect)

    # 업데이트된 초기 화면 표시
    pygame.display.flip()


# 체스 보드 그리기
def draw_chess_board():
    pygame.draw.rect(chessBoard, (180, 180, 180),
                     (0, 0, width + 2 * border_size, border_size))
    pygame.draw.rect(chessBoard, (180, 180, 180),
                     (0, 0, border_size, height + 2 * border_size))
    pygame.draw.rect(chessBoard, (180, 180, 180), (0, height +
                     border_size, width + 2 * border_size, border_size))
    pygame.draw.rect(chessBoard, (180, 180, 180), (width +
                     border_size, 0, border_size, height + 2 * border_size))

    for row in range(8):
        for col in range(8):
            # 번갈아가며 사각형 그리기
            color = white if (row + col) % 2 == 0 else black
            pygame.draw.rect(chessBoard, color, (col * (width//8) +
                             border_size, row * (height//8)+border_size, 50, 45))

    pygame.draw.lines(chessBoard, (0, 0, 0), True, [
        (border_size, border_size),
        (border_size + width, border_size),
        (border_size + width, border_size + height),
        (border_size, border_size + height),
        (border_size, border_size)], 4)

    # 좌표 추가
    font = pygame.font.Font(None, 28)

    for i, label in enumerate("abcdefgh"):  # 위쪽
        text = pygame.transform.rotate(
            font.render(label, True, (0, 0, 0)), 180)
        chessBoard.blit(
            text, (i * (width // 8) + border_size + 25, border_size - 30))

    for i, label in enumerate("abcdefgh"):  # 아래쪽
        text = font.render(label, True, (0, 0, 0))
        chessBoard.blit(
            text, (i * (width // 8) + border_size + 25, height + border_size + 10))

    for i, label in enumerate("87654321"):  # 오른쪽
        text = pygame.transform.rotate(
            font.render(label, True, (0, 0, 0)), 180)
        chessBoard.blit(text, (width + border_size + 15, i *
                        (height // 8) + border_size + 20))

    for i, label in enumerate("87654321"):  # 왼쪽
        text = font.render(label, True, (0, 0, 0))
        chessBoard.blit(text, (border_size - 25, i *
                        (height // 8) + border_size + 20))


# 말 이미지 로드
piece_images = {}
for color in ["white", "black"]:
    for piece in ["pawn", "rook", "knight", "bishop", "queen", "king"]:
        piece_key = f"{color}_{piece}"
        piece_filename = f"images/{piece_key}.png"
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


# 폰 이동 방식
def valid_moves_pawn(row, col, is_white):
    moves = []
    direction = 1 if is_white else -1

    if 0 <= row + direction < 8 and chess_board[row + direction][col] == 0:
        moves.append((row + direction, col))
        if (row == 1 and is_white) or (row == 6 and not is_white):
            if chess_board[row + 2 * direction][col] == 0:
                moves.append((row + 2 * direction, col))

    for col_offset in [-1, 1]:
        new_col = col + col_offset
        if 0 <= row + direction < 8 and 0 <= new_col < 8:
            target_piece = chess_board[row + direction][new_col]
            if target_piece != 0 and (is_white != target_piece.startswith("white")):
                moves.append((row + direction, new_col))

    return moves


# 룩 이동 방식
def valid_moves_rook(row, col):
    moves = []

    for row_offset, col_offset in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_row, new_col = row + row_offset, col + col_offset
        while 0 <= new_row < 8 and 0 <= new_col < 8:
            target_piece = chess_board[new_row][new_col]
            if target_piece == 0:
                moves.append((new_row, new_col))
            else:
                if target_piece.startswith("black") != chess_board[row][col].startswith("black"):
                    moves.append((new_row, new_col))
                break
            new_row, new_col = new_row + row_offset, new_col + col_offset

    return moves


# 비숍 이동 방식
def valid_moves_bishop(row, col):
    moves = []

    for row_offset, col_offset in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
        new_row, new_col = row + row_offset, col + col_offset
        while 0 <= new_row < 8 and 0 <= new_col < 8:
            target_piece = chess_board[new_row][new_col]
            if target_piece == 0:
                moves.append((new_row, new_col))
            else:
                if target_piece.startswith("black") != chess_board[row][col].startswith("black"):
                    moves.append((new_row, new_col))
                break
            new_row, new_col = new_row + row_offset, new_col + col_offset

    return moves


# 나이트 이동 방식
def valid_moves_knight(row, col):
    moves = []

    for row_offset in [-2, -1, 1, 2]:
        for col_offset in [-2, -1, 1, 2]:
            if abs(row_offset) + abs(col_offset) == 3:
                new_row, new_col = row + row_offset, col + col_offset
                if 0 <= new_row < 8 and 0 <= new_col < 8:
                    target_piece = chess_board[new_row][new_col]
                    if target_piece == 0 or (target_piece.startswith("black") != chess_board[row][col].startswith("black")):
                        moves.append((new_row, new_col))

    return moves


# 퀸 이동 방식
def valid_moves_queen(row, col):
    moves = valid_moves_bishop(row, col) + valid_moves_rook(row, col)

    return moves


# 킹 이동 방식
def valid_moves_king(row, col):
    moves = []

    for row_offset in [-1, 0, 1]:
        for col_offset in [-1, 0, 1]:
            new_row, new_col = row + row_offset, col + col_offset
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                target_piece = chess_board[new_row][new_col]
                if target_piece == 0 or (target_piece.startswith("black") != chess_board[row][col].startswith("black")):
                    moves.append((new_row, new_col))

    return moves


# 이동 가능 판별 함수
def get_valid_moves(row, col):
    piece_key = chess_board[row][col]

    if piece_key.startswith("white"):
        is_white = True
    else:
        is_white = False

    if piece_key.endswith("pawn"):
        return valid_moves_pawn(row, col, is_white)
    elif piece_key.endswith("rook"):
        return valid_moves_rook(row, col)
    elif piece_key.endswith("knight"):
        return valid_moves_knight(row, col)
    elif piece_key.endswith("bishop"):
        return valid_moves_bishop(row, col)
    elif piece_key.endswith("queen"):
        return valid_moves_queen(row, col)
    elif piece_key.endswith("king"):
        return valid_moves_king(row, col)
    else:
        return []


# 킹이 죽었을 때 게임 종료 여부 확인
def check_game_over():
    white_king_alive = False
    black_king_alive = False

    for row in range(8):
        for col in range(8):
            piece_key = chess_board[row][col]
            if piece_key == "white_king":
                white_king_alive = True
            elif piece_key == "black_king":
                black_king_alive = True

    return not (white_king_alive and black_king_alive)


# 턴을 전환하는 함수
def change_turn():
    global current_turn
    current_turn = "white" if current_turn == "black" else "black"


# 이긴 팀을 화면에 표시
def show_winner(winner_color):
    font = pygame.font.Font(None, 50)
    text_color = (0, 0, 0)  # 텍스트 색을 검은색으로 지정
    if winner_color == "black":
        text = font.render("White Team Wins!", True, text_color)
    else:
        text = font.render("Black Team Wins!", True, text_color)
    text_rect = text.get_rect(
        center=(width // 2+border_size, height // 2+border_size))
    chessBoard.blit(text, text_rect)

    # 게임 승리 사운드
    win_sound.play()

    pygame.display.flip()
    pygame.time.wait(3000)  # 3초 동안 결과를 보여준 후 게임 종료


# 폰 승급 여부를 기록하는 딕셔너리
promoted_pawns = {"white": set(), "black": set()}


# 폰 승급 프로모션 기능 추가
def promote_pawn(row, col):
    global current_turn
    piece_key = chess_board[row][col]
    is_white = chess_board[row][col].startswith("white")

    # 폰에 대해서만 승급 여부 확인
    if piece_key.endswith("pawn") and is_promotion_row(row, is_white) and row not in promoted_pawns["white" if is_white else "black"]:
        promotion_options = ["rook", "bishop", "knight", "queen"]
        selected_piece = random.choice(promotion_options)  # 랜덤으로 선택

        # 선택된 말로 폰을 대체합니다.
        chess_board[row][col] = f"{current_turn}_{selected_piece}"

        # 승급 여부 기록
        promoted_pawns["white" if is_white else "black"].add(row)


# 승급 가능한 행 확인
def is_promotion_row(row, is_white):
    if is_white:
        return row == 7
    else:
        return row == 0


# 게임 루프
running = True
selected_piece = None
is_piece_selected = False
current_turn = "black"  # 초기에는 검은색 말의 차례zz

while running:
    if check_game_over():

        # 이긴 팀 표시
        show_winner(current_turn)
        running = False  # 게임 종료

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # 마우스 클릭 위치 확인
            mouse_x, mouse_y = pygame.mouse.get_pos()
            clicked_row = (mouse_y-border_size) // (height // 8)
            clicked_col = (mouse_x-border_size) // (width // 8)

            if initial_screen:
                if play_button_rect.collidepoint(mouse_x, mouse_y):
                    initial_screen = False
                    break

            else:
                if selected_piece is None:
                    # 선택된 말이 없을 때, 현재 턴의 말을 선택
                    if (
                        current_turn == "black"
                        and chess_board[clicked_row][clicked_col] != 0
                        and chess_board[clicked_row][clicked_col].startswith("black")
                    ):
                        selected_piece = (clicked_row, clicked_col)
                        is_piece_selected = True
                    elif (
                        current_turn == "white"
                        and chess_board[clicked_row][clicked_col] != 0
                        and chess_board[clicked_row][clicked_col].startswith("white")
                    ):
                        selected_piece = (clicked_row, clicked_col)
                        is_piece_selected = True
                else:
                    # 선택된 말이 있을 때, 다른 말을 선택하면 해당 말로 변경
                    if (
                        chess_board[clicked_row][clicked_col] != 0
                        and (
                            (current_turn == "black" and chess_board[clicked_row][clicked_col].startswith(
                                "black"))
                            or (current_turn == "white" and chess_board[clicked_row][clicked_col].startswith("white"))
                        )
                    ):
                        selected_piece = (clicked_row, clicked_col)
                    else:
                        # 선택된 말의 이동 가능한 위치인지 확인하고 이동
                        valid_moves = get_valid_moves(
                            selected_piece[0], selected_piece[1])
                        # 이동 사운드
                        move_sound.play()

                        if (clicked_row, clicked_col) in valid_moves:
                            # 공격한 말의 이미지로 바꾸기
                            attacking_piece = chess_board[selected_piece[0]
                                                          ][selected_piece[1]]
                            chess_board[clicked_row][clicked_col] = attacking_piece
                            chess_board[selected_piece[0]
                                        ][selected_piece[1]] = 0
                            selected_piece = None
                            is_piece_selected = False

                           # 폰 승급 체크 및 처리
                            if is_promotion_row(clicked_row, current_turn == "white"):
                                promote_pawn(clicked_row, clicked_col)

                            # 턴 전환
                            change_turn()

    if initial_screen:
        # 초기 화면 그리기
        draw_initial_screen()

    else:
        # 체스 보드 그리기
        draw_chess_board()

        # 말 이미지 표시
        for row in range(8):
            for col in range(8):
                if chess_board[row][col] != 0:
                    piece_key = chess_board[row][col]
                    piece_position = (
                        col * (width // 8)+border_size, row * (height // 8)+border_size)

                    # 선택된 말 강조
                    if is_piece_selected and (row, col) == selected_piece:
                        pygame.draw.rect(
                            chessBoard, (255, 0, 0), (*piece_position, width // 8, height // 8), 5)

                    chessBoard.blit(piece_images[piece_key], piece_position)

        # 선택한 말의 이동 가능한 위치 표시
        if selected_piece is not None:
            selected_row, selected_col = selected_piece
            valid_moves = get_valid_moves(selected_row, selected_col)
            for move_row, move_col in valid_moves:
                # 이동 가능한 곳에 녹색 원 표시
                pygame.draw.circle(chessBoard, (0, 255, 0, 100), ((
                    move_col * (width // 8)+border_size) + width // 16, (move_row * (height // 8)+border_size) + height // 16), 12)

                # 상대 말이 있는 경우 해당 위치에 붉은 원 표시
                target_piece = chess_board[move_row][move_col]
                if (
                    target_piece != 0
                    and (
                        (current_turn == "black" and target_piece.startswith("white"))
                        or (current_turn == "white" and target_piece.startswith("black"))
                    )
                ):
                    pygame.draw.circle(chessBoard, (255, 0, 0, 100), ((
                        move_col * (width // 8))+border_size + width // 16, (move_row * (height // 8)+border_size) + height // 16), 12)

        # 업데이트된 화면을 표시
    pygame.display.flip()

# Pygame 종료
pygame.mixer.quit()
pygame.quit()
sys.exit()
