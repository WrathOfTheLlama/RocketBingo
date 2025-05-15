import random # to randomly pick what is on the board
import numpy # type: ignore
import timer # type: ignore
import tkinter as tk
from tkinter import messagebox
from flask import Flask, jsonify, request

app = Flask(__name__)

bingo_board = {} # dictionary used to store bingo board
bingo_users = {}

@app.route('/create-board/<user_id>', methods=['POST'])
def create_board(userid):
    # Generate a bingo board (replace with actual bingo board logic)
    board = ["Square"*25]
    bingo_board[userid] = board
    return jsonify({'message': 'Board created', 'board': board})


@app.route('/mark-square', methods=['POST'])
def mark_square():
    # Get user id and the square number that user is marking from the request
    user_id = request.json['user_id']
    square_num = request.json['square_number']
    ... # use the square_num to navigate the bingo board and mark the square for that player

@app.route('/check-bingo', methods=['POST'])
def check_bingo():
    # Get user id from the request
    user_id = request.json['user_id']
    # Logic to check for bingo
    return jsonify({'message': 'Bingo checked', 'user_id': user_id, 'bingo': True})

@app.route('/get-board/<user_id>', methods=['GET'])
def get_board(user_id):
    if user_id in bingo_board:
      return jsonify({'board': bingo_board[user_id]})
    return jsonify({'message': 'No board found for this user'})


if __name__ == 'main':
    app.run(debug=True)