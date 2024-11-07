# -*- coding: utf-8 -*-
"""TicTacToe.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ACyI4akaNy-9HRscDQS95SpBtrR9_Zfh
"""

import random

# Initial game board
board = ["_","_","_",
         "_","_","_",
         "_","_","_"]

play = True
winner = None

def printBoard(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])

def playerInput(board):
    inp = int(input("Enter a number from 1-9: "))
    if inp >= 1 and inp <= 9 and board[inp - 1] == "_":
        board[inp - 1] = "X"
    else:
        print("Invalid Input")

def checkHorizontals(board):
    if board[0] == board[1] == board[2] and board[0] != "_":
        return board[0]
    elif board[3] == board[4] == board[5] and board[3] != "_":
        return board[3]
    elif board[6] == board[7] == board[8] and board[6] != "_":
        return board[6]
    return None

def checkRows(board):
    if board[0] == board[3] == board[6] and board[0] != "_":
        return board[0]
    elif board[1] == board[4] == board[7] and board[1] != "_":
        return board[1]
    elif board[2] == board[5] == board[8] and board[2] != "_":
        return board[2]
    return None

def checkDiags(board):
    if board[0] == board[4] == board[8] and board[0] != "_":
        return board[0]
    elif board[2] == board[4] == board[6] and board[2] != "_":
        return board[2]
    return None

def checkWinner(board):
    global winner
    winner = checkHorizontals(board) or checkRows(board) or checkDiags(board)
    return winner

def checkTie(board):
    return "_" not in board

def evaluate(board):
    if checkWinner(board) == "O":
        return 1
    elif checkWinner(board) == "X":
        return -1
    elif checkTie(board):
        return 0
    return None


def minimax(board, is_maximizing):
    score = evaluate(board)
    if score is not None:
        return score

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == "_":
                board[i] = "O"
                score = minimax(board, False)
                board[i] = "_"
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == "_":
                board[i] = "X"
                score = minimax(board, True)
                board[i] = "_"
                best_score = min(score, best_score)
        return best_score


def computer(board):
    best_score = -float('inf')
    best_move = None
    for i in range(9):
        if board[i] == "_":
            board[i] = "O"
            score = minimax(board, False)
            board[i] = "_"
            if score > best_score:
                best_score = score
                best_move = i
    board[best_move] = "O"


while play:
    printBoard(board)
    playerInput(board)
    if checkWinner(board):
        printBoard(board)
        print("Player wins!")
        break
    if checkTie(board):
        printBoard(board)
        print("It's a tie!")
        break
    computer(board)
    if checkWinner(board):
        printBoard(board)
        print("AI wins!")
        break
    if checkTie(board):
        printBoard(board)
        print("It's a tie!")
        break
