from application import app, db
from application.models import Games

@app.route('/add/<game_name>')
def add(game_name):
    new_game = Games(name=game_name)
    db.session.add(new_game)
    db.session.commit()
    return "Added new game to database"

@app.route('/read')
def read():
    all_games = Games.query.all()
    games_string = ""
    for game in all_games:
        games_string += "<br>"+ game.name
    return games_string

@app.route('/update/<name>')
def update(name):
    first_game = Games.query.first()
    first_game.name = name
    db.session.commit()
    return first_game.name

@app.route('/delete/<int:game_id>')
def delete(game_id):
    game_to_delete = Games.query.get(game_id)
    db.session.delete(game_to_delete)
    db.session.commit()
    return "Deleted game with id " + str(game_id)

@app.route('/count')
def count():
    number_of_games = Games.query.count()
    return str(number_of_games)
