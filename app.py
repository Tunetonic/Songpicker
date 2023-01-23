from algorithme import calculate_initial_distribution, calculate_update_distribution
from database_manager import get_connection, get_connection_url, create_tables
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from os import getenv
from algorithme_utilities import replace_dash
import model.user_distribution

load_dotenv()
prefix = "/api/v1/songpicker"
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = get_connection_url()

"""Returns user distribution based on userID"""
@app.route(f"{prefix}", methods=["GET"])
def get_distribution():
    userid = request.json["userId"]
    manual_connection = get_connection()
    
    connection = manual_connection.get("connection")
    distribution_table = manual_connection.get("distribution_table")
    # userid_col = column("userid")
    
    # return jsonify(connection.execute(select([distribution_table]).where(userid_col == userid)))
    return {}
    

"""Creates the first distribution with the following inputs:
    - Genres (list of genres)
    - UserID (unique id of the user)
    - preferedGenres (chosen genres by the user)
    """
@app.route(f"{prefix}/init", methods=["POST"])
def initialize_distribution():
    genresReq = request.json["genres"]
    userId = request.json["userId"]
    prefered_genres = request.json["preferedGenres"]
    
    if userId == None or genresReq == None:
        raise Exception("The required input params are not defined")
    
    genres = list(map(replace_dash, genresReq)) 
    distribution = calculate_initial_distribution(genres=genres, prefered_genres=prefered_genres)
    
    manual_connection = get_connection()
    
    connection = manual_connection.get("connection")
    
    distribution = distribution.pivot_table(columns=genres)
    distribution["userid"] = userId
    
    distribution.to_sql("user_distribution", connection, if_exists="append", chunksize=250, index=False)

    return distribution.to_json(orient="records")

"""This endpoint represent the algorithme. You can feed it
    likes and dislikes. The format of the data is in the algorthme.py file
    """
@app.route(f"{prefix}/update")
def change_distribution():
    # 1. get distribution from db
    # 2. get likes and dislikes (rating) from input parameter
    # 3. run content_algorithme function
    # 4. save distribution in database
    pass


if __name__ == "__main__":
    # create_tables(app, db)
    app.run()
