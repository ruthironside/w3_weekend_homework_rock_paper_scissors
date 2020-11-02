from flask import render_template, request
from app import app
from app.models.players import players
from app.models.player import *
from app.models.game import *

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<player1_choice>/<player2_choice>') 
def play(player1_choice, player2_choice): 
    player1 = Player(name='player1', choice=player1_choice)
    player2 = Player(name='player2', choice=player2_choice)
    game1 = Game(player1, player2)
    return game1.play_game(player1_choice, player2_choice) 

@app.route('/play-game', methods=['POST'])
def play_game():
    player1_name = request.form['player1_name']
    player1_choice = request.form['player1_choice']
    player1 = Player(name=player1_name, choice=player1_choice)

    player2_name = request.form['player2_name']
    player2_choice = request.form['player2_choice']
    player2 = Player(name=player2_name, choice=player2_choice)

    game1 = Game(player1, player2)
    result = game1.play_game(player1_choice, player2_choice)  
    print(result)
    return render_template('index.html', result=result)
    
    
    
    # return redirect('/')


