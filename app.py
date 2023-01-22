from algorithme import calculate_initial_distribution, calculate_update_distribution
from database_manager import get_connection, get_connection_url, create_tables
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from os import getenv
from sqlalchemy import select, column
from model.user_distribution import UserDistribution, db


load_dotenv()
prefix = "/api/v1/songpicker"
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = get_connection_url()
db.init_app(app=app)

@app.route(f"/", methods=["GET", "POST"])
def hello():
    firstname = request.json["firstName"]
    lastname = request.json["lastName"]
    age = request.json["age"]
    
    return jsonify({"firstname": firstname}, {"lastname": lastname}, {"age": age}, {"env": getenv("API_URL")})

@app.route(f"{prefix}", methods=["GET"])
def get_distribution():
    userid = request.json["userId"]
    manual_connection = get_connection()
    
    connection = manual_connection.get("connection")
    distribution_table = manual_connection.get("distribution_table")
    userid_col = column("userid")
    
    return jsonify(connection.execute(select([distribution_table]).where(userid_col == userid)))
    

@app.route(f"{prefix}/init",)
def initialize_distribution():
    # userId = request.json["userId"]
    genres = request.json["genres"]
    prefered_genres = request.json["preferedGenres"]
    
    distribution = calculate_initial_distribution(genres=genres, prefered_genres=prefered_genres)
    
    manual_connection = get_connection()
    
    connection = manual_connection.get("connection")
    
    distribution.to_sql("distribution_table", connection, if_exists="replace", chunksize=250)
    
    # get genres from db
    # get prio genres from parameter
    # run initvalues function
    # save distribution in db
    return distribution.to_json(orient="index")

@app.route(f"{prefix}/update")
def change_distribution():
    # get distribution from db
    # get likes and dislikes (rating) from input parameter
    # run content_algorithme function
    # save distribution in database
    pass


if __name__ == "__main__":
    create_tables(app, db)
    app.run()



# genres = ["acoustic", "afrobeat", "alt-rock", "alternative", "ambient", "anime", "black-metal", "bluegrass", "blues", "bossanova", "brazil", "breakbeat", "british", "cantopop", "chicago-house", "children", "chill", "classical", "club", "comedy", "country", "dance", "dancehall", "death-metal", "deep-house", "detroit-techno", "disco", "disney", "drum-and-bass", "dub", "dubstep", "edm", "electro", "electronic", "emo", "folk", "forro", "french", "funk", "garage", "german", "gospel", "goth", "grindcore", "groove", "grunge", "guitar", "happy", "hard-rock", "hardcore", "hardstyle", "heavy-metal", "hip-hop", "holidays", "honky-tonk", "house", "idm", "indian", "indie", "indie-pop", "industrial", "iranian", "j-dance", "j-idol", "j-pop", "j-rock", "jazz", "k-pop", "kids", "latin", "latino", "malay", "mandopop", "metal", "metal-misc", "metalcore", "minimal-techno", "movies", "mpb", "new-age", "new-release", "opera", "pagode", "party", "philippines-opm", "piano", "pop", "pop-film", "post-dubstep", "power-pop", "progressive-house", "psych-rock", "punk", "punk-rock", "r-n-b", "rainy-day", "reggae", "reggaeton", "road-trip", "rock", "rock-n-roll", "rockabilly", "romance", "sad", "salsa", "samba", "sertanejo", "show-tunes", "singer-songwriter", "ska", "sleep", "songwriter", "soul", "soundtracks", "spanish", "study", "summer", "swedish", "synth-pop", "tango", "techno", "trance", "trip-hop", "turkish", "work-out", "world-music"]
# prio_test = ["acoustic", "afrobeat", "ambient"]

# algo_test = [{'genre': 'acoustic', 'rating': 1},
#  {'genre': 'rock', 'rating': 1},
#  {'genre': 'afrobeat', 'rating': 0},
#  {'genre': 'rock', 'rating': 1},
#  {'genre': 'rock', 'rating': 0},
#  {'genre': 'afrobeat', 'rating': 0},
#  {'genre': 'rock', 'rating': 1},
#  {'genre': 'rock', 'rating': 0},
#  {'genre': 'afrobeat', 'rating': 1},
#  {'genre': 'rock', 'rating': 1},
#  {'genre': 'rock', 'rating': 0},
#  {'genre': 'afrobeat', 'rating': 0}]

# df = initial_values(genres, priority_genres=prio_test)
# algo_result = content_algorithme(df, algo_test)