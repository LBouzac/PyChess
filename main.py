import pygame
import chess
import random

def initialize_chess_board():
    return chess.Board()

def make_move(board, move):
    if move in [m.uci() for m in board.legal_moves]:
        board.push(chess.Move.from_uci(move))
    else:
        print("Mouvement invalide")

def ai_move(board):
    legal_moves = list(board.legal_moves)
    move = random.choice(legal_moves)
    board.push(move)
    return move

def main():
    pygame.init()
    screen = pygame.display.set_mode((480, 480))
    pygame.display.set_caption("Jeu d'échecs")
    board = initialize_chess_board()

    selected_square = None
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                handle_player_move(board, mouse_pos, selected_square)
                selected_square = get_square(mouse_pos)

        screen.fill(pygame.Color("black"))
        draw_board(screen, board)
        pygame.display.flip()

        if board.turn == chess.BLACK:  # Tour de l'IA
            ai_move(board)

    pygame.quit()

def get_square(mouse_pos):
    col = mouse_pos[0] // 60
    row = 7 - (mouse_pos[1] // 60)
    return chess.square(col, row)

def handle_player_move(board, mouse_pos, selected_square):
    square = get_square(mouse_pos)
    if selected_square is None:
        if board.piece_at(square) and board.piece_at(square).color == board.turn:
            return square
    else:
        move = chess.Move(selected_square, square)
        if move in board.legal_moves:
            board.push(move)
        return None

def draw_board(screen, board):
    colors = [pygame.Color("white"), pygame.Color("gray")]
    for row in range(8):
        for col in range(8):
            color = colors[(row + col) % 2]
            pygame.draw.rect(screen, color, pygame.Rect(col * 60, row * 60, 60, 60))
            piece = board.piece_at(chess.square(col, 7 - row))
            if piece:
                font = pygame.font.Font(None, 36)
                text = font.render(piece.symbol(), True, pygame.Color("black"))
                screen.blit(text, (col * 60 + 20, row * 60 + 10))

if __name__ == "__main__":
    main()