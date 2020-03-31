import chess
import chess.svg
import chess.polyglot
import random
import AI
import book
import boardset

book.LoadOpeingBook()
board = chess.Board()
board_info = {}
boardset.board_start(board, board_info)
Search_Depth = 4  # 搜索深度，越大AI越强


def check_human_move(Human_Move):  # 检测走法合法性
    try:
        board.push_san(Human_Move)
        board.pop()
    except:
        return False
    return True


def humanMove(s):
    Human_Move = input("\n%s:" % s)
    while check_human_move(Human_Move) != True:
        Human_Move = input("The move is illegal, please input again.\n%s:" % s)
    boardset.board_info_set(board, Human_Move, board_info)
    board.push_san(Human_Move)


def aiMove():
    AI_Move = book.book_move(board)  # 读入开局库
    if not AI_Move == None:
        board.push_san(AI_Move)
    else:
        AI_Move = AI.do_search(board, board_info, Search_Depth)
        boardset.board_info_set(board, AI_Move, board_info)
        board_info["hash"] = chess.polyglot.zobrist_hash(board)
        board.push_san(AI_Move)
    return AI_Move


color = input("Choose Your Color (White/Black):")  # 选择黑白方

if color == "white" or color == "White" or color == "w" or color == "W":
    board_info["color_AI"] = 0
    while not board.is_game_over():
        humanMove("White")
        AI_Move = aiMove()
        print("Black: " + AI_Move + "\nValue: " + str(AI.evaluate(board, board_info)))
        print(board)

elif color == "black" or color == "Black" or color == "b" or color == "B":
    board_info["color_AI"] = 1
    while not board.is_game_over():
        AI_Move = aiMove()
        print("Black: " + AI_Move + "\nValue: " + str(AI.evaluate(board, board_info)))
        print(board)
        humanMove("Black")

else:
    print("The choice is illegal.")
