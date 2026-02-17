from math import inf

WIN_LINES = [
    (0,1,2),(3,4,5),(6,7,8),  # rows
    (0,3,6),(1,4,7),(2,5,8),  # cols
    (0,4,8),(2,4,6)           # diagonals
]

def winner(board):
    for a,b,c in WIN_LINES:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]
    return None
#board er state ik' glem det!

def is_draw(board):
    return winner(board) is None and all(cell != " " for cell in board)

def available_moves(board):
    return [i for i,cell in enumerate(board) if cell == " "]
#available moves er operationer

def evaluate(board, ai, human, depth=0):
    w = winner(board)
    if w == ai:
        return 10 - depth
    if w == human:
        return depth - 10
    return 0  # draw / non-terminal handled elsewhere

def minimax_ab(board, turn, ai, human, depth, alpha, beta): #metoden minimax_ab er minimax + alphabeta
    w = winner(board)
    if w or is_draw(board):
        return evaluate(board, ai, human, depth)

    if turn == ai:  # MAX
        best = -inf
        for m in available_moves(board):
            board[m] = ai
            score = minimax_ab(board, human, ai, human, depth+1, alpha, beta)
            board[m] = " "
            best = max(best, score)
            alpha = max(alpha, best)
            if alpha >= beta:
                break  # Når alpha er større end beta, så prune resten ( klip )
        return best
    else:  # MIN
        best = inf
        for m in available_moves(board):
            board[m] = human
            score = minimax_ab(board, ai, ai, human, depth+1, alpha, beta)
            board[m] = " "
            best = min(best, score)
            beta = min(beta, best)
            if alpha >= beta:
                break  # prune
        return best

def best_move(board, ai, human):
    best_score = -inf
    best_m = None
    for m in available_moves(board):
        board[m] = ai
        score = minimax_ab(board, human, ai, human, 0, -inf, inf)
        board[m] = " "
        if score > best_score:
            best_score = score
            best_m = m
    return best_m

def print_board(board):
    def row(i):
        return f" {board[i]} | {board[i+1]} | {board[i+2]} "
    print(row(0))
    print("---+---+---")
    print(row(3))
    print("---+---+---")
    print(row(6))

def play_terminal():
    board = [" "] * 9
    human = input("Vil du være X eller O? ").strip().upper()
    while human not in ("X","O"):
        human = input("Skriv X eller O: ").strip().upper()
    ai = "O" if human == "X" else "X"

    turn = "X"  # X starter altid
    print("\nFelter er 0-8 som:")
    print(" 0 | 1 | 2 ")
    print("---+---+---")
    print(" 3 | 4 | 5 ")
    print("---+---+---")
    print(" 6 | 7 | 8 \n")

    while True:
        print_board(board)
        w = winner(board)
        if w:
            print(f"\n{w} vandt!")
            break
        if is_draw(board):
            print("\nUafgjort!")
            break

        if turn == human:
            move = input(f"Din tur ({human}). Vælg felt 0-8: ")
            if not move.isdigit() or int(move) not in available_moves(board):
                print("Ugyldigt move. Prøv igen.")
                continue
            board[int(move)] = human
            turn = ai
        else:
            m = best_move(board, ai, human)
            board[m] = ai
            print(f"\nAI ({ai}) spiller: {m}\n")
            turn = human

if __name__ == "__main__":
    play_terminal()
