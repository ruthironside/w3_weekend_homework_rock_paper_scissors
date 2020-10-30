from flask import render_template
from app import app
from app.models.players import players
from app.models.player import *

@app.route('/')
def index():
    return render_template('index.html', title='Home', players=players)

@app.route('/<choice>') 
def play(choice): 
    return f"Player 1 wins by playing {choice}!"