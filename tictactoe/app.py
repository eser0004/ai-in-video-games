from flask import Flask, render_template, request, redirect, url_for

# Importér spil-logik fra tictactoe.py
from tictactoe import winner, is_draw, available_moves, best_move

app = Flask(__name__)

# Super simpel "session": gem spillet i globale variabler
board = [" "] * 9
human = "X"
ai = "O"
turn = "X"  # X starter altid


def reset_game():
    global board, turn
    board = [" "] * 9
    turn = "X"


@app.route("/")
def index():
    w = winner(board)
    draw = is_draw(board)

    if w:
        status = f"{w} vandt!"
    elif draw:
        status = "Uafgjort!"
    else:
        status = f"Tur: {turn}"

    return render_template("index.html", board=board, status=status, w=w, draw=draw)


@app.route("/move", methods=["POST"])
def move():
    global board, turn

    # hvis spil er slut, ignorer klik
    if winner(board) or is_draw(board):
        return redirect(url_for("index"))

    pos = int(request.form["pos"])

    # menneske spiller kun hvis det er menneskets tur og feltet er tomt
    if turn == human and pos in available_moves(board):
        board[pos] = human
        turn = ai

    # AI spiller hvis spillet ikke er slut
    if not winner(board) and not is_draw(board) and turn == ai:
        m = best_move(board, ai, human)
        if m is not None:
            board[m] = ai
        turn = human

    return redirect(url_for("index"))


@app.route("/reset", methods=["POST"])
def reset():
    reset_game()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
