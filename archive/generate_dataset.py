import pandas as pd
import numpy as np
import os
import random

"""This code will generate the following format:
    Genre
    Like/dislike
    
    for example
    acoustic-rock-pop
    0         1     0
    1         1     0
    1         1     1
    """
def generate_fake_data(columns, size):
    fake_data_dataframe = pd.DataFrame(columns=columns)
    
    for i in genres:
        fake_data_dataframe[i] = np.random.randint(2, size=size)
    
    return fake_data_dataframe

"""Genre - Like/dislike
    rock - 1
    pop  - 0
    """
def generate_fake_data_with_titled_columns(genres, size):
    # dislike = 0 | like = 1
    data = []
    index = 0
    for _ in range(size):
        if (index == len(genres)):
            index = 0

        payload = {'genre': genres[index], 'like/dislike': random.randint(0, 1)}
        data.append(payload)
        index += 1
    return pd.DataFrame(data=data, columns=["genre", "like/dislike"])

def generate_specific_genre_likes(column, size):
    data = []
    for _ in range(size):
        payload = {'genre': column, "like/dislike": 1}
        data.append(payload)
        
    return pd.DataFrame(data=data, columns=["genre", "like/dislike"])

def save_train_data(fileName):
    return os.path.join(os.path.dirname(__file__), "data", fileName)

genres = ["acoustic", "afrobeat", "alt-rock", "alternative", "ambient", "anime", "black-metal", "bluegrass", "blues", "bossanova", "brazil", "breakbeat", "british", "cantopop", "chicago-house", "children", "chill", "classical", "club", "comedy", "country", "dance", "dancehall", "death-metal", "deep-house", "detroit-techno", "disco", "disney", "drum-and-bass", "dub", "dubstep", "edm", "electro", "electronic", "emo", "folk", "forro", "french", "funk", "garage", "german", "gospel", "goth", "grindcore", "groove", "grunge", "guitar", "happy", "hard-rock", "hardcore", "hardstyle", "heavy-metal", "hip-hop", "holidays", "honky-tonk", "house", "idm", "indian", "indie", "indie-pop", "industrial", "iranian", "j-dance", "j-idol", "j-pop", "j-rock", "jazz", "k-pop", "kids", "latin", "latino", "malay", "mandopop", "metal", "metal-misc", "metalcore", "minimal-techno", "movies", "mpb", "new-age", "new-release", "opera", "pagode", "party", "philippines-opm", "piano", "pop", "pop-film", "post-dubstep", "power-pop", "progressive-house", "psych-rock", "punk", "punk-rock", "r-n-b", "rainy-day", "reggae", "reggaeton", "road-trip", "rock", "rock-n-roll", "rockabilly", "romance", "sad", "salsa", "samba", "sertanejo", "show-tunes", "singer-songwriter", "ska", "sleep", "songwriter", "soul", "soundtracks", "spanish", "study", "summer", "swedish", "synth-pop", "tango", "techno", "trance", "trip-hop", "turkish", "work-out", "world-music"]

generation_size=100000

# General DF
titled_train_df = generate_fake_data_with_titled_columns(genres=genres, size=generation_size)

# Specific preferences
rock_df = generate_specific_genre_likes("rock", generation_size)
pop_df = generate_specific_genre_likes("pop", generation_size)
acoustic_df = generate_specific_genre_likes("acoustic", generation_size)
afro_df = generate_specific_genre_likes("afrobeat", generation_size)

titled_train_df = titled_train_df[titled_train_df["genre"] != "rock"]
titled_train_df = titled_train_df[titled_train_df["genre"] != "pop"]
titled_train_df = titled_train_df[titled_train_df["genre"] != "acoustic"]
titled_train_df = titled_train_df[titled_train_df["genre"] != "afrobeat"]

# Combining preferences and general DF
titled_train_df = pd.concat([titled_train_df, rock_df, pop_df, acoustic_df, afro_df])

# Saving the model
titled_train_df.to_csv(save_train_data("titled_train_data.csv"), index=False)
