from algorithme_validation import list_is_empty
import pandas as pd

def calculate_initial_distribution(genres, prefered_genres = None):
    if list_is_empty(genres):
        raise Exception("genres is empty!")
    
    df = pd.DataFrame(index=genres, columns=["chance"])
    genres_len = len(genres)
    total_chance = 100
    small_preferences_chance = 25
    large_preferences_chance = 40
    
    if list_is_empty(prefered_genres):
        df["chance"] = total_chance / genres_len
    else:
        priority_genre_len = len(prefered_genres)
        are_large_preferences = priority_genre_len > 2
        reserved_chance = large_preferences_chance if are_large_preferences else small_preferences_chance
        leftover_chance = total_chance - reserved_chance
        prio_chance = reserved_chance / priority_genre_len
        
        df["chance"] = leftover_chance / (genres_len - priority_genre_len)
        
        for i in prefered_genres:
            if not i in df.index:
                continue
            df.loc[i, "chance"] = prio_chance
    return df

"""
df: is the current distribution of preferences
genres: is an array of objects which look like {genre: rock, rating: 1}
"""
def calculate_update_distribution(df = pd.DataFrame, genres = []):
    maxPoints = 100
    increaseLikeWeight = 0.10
    decreaseLikeWeight = 0.10
    increaseWeight = 0.07
    decreaseWeight = 0.05
    genreList = list(map(lambda x:x['genre'], genres))
    
    for row in genres:
        if row.get("rating") == 1:
            df.loc[row.get("genre"), "chance"] = df.loc[row.get("genre"), "chance"] + increaseLikeWeight
        elif row.get("rating") == 0:
            df.loc[row.get("genre"), "chance"] = df.loc[row.get("genre"), "chance"] - decreaseLikeWeight
    
    while True:
        currentTotalPoints = df["chance"].sum()
        if currentTotalPoints > maxPoints + 1:
            df.loc[~df.index.isin(genreList), "chance"] = df.loc[~df.index.isin(genreList), "chance"] - decreaseWeight
            continue
        if currentTotalPoints < maxPoints - 1:
            df.loc[~df.index.isin(genreList), "chance"] = df.loc[~df.index.isin(genreList), "chance"] + increaseWeight
            continue
        break
        
    return df

genres = ["acoustic", "afrobeat", "alt-rock", "alternative", "ambient", "anime", "black-metal", "bluegrass", "blues", "bossanova", "brazil", "breakbeat", "british", "cantopop", "chicago-house", "children", "chill", "classical", "club", "comedy", "country", "dance", "dancehall", "death-metal", "deep-house", "detroit-techno", "disco", "disney", "drum-and-bass", "dub", "dubstep", "edm", "electro", "electronic", "emo", "folk", "forro", "french", "funk", "garage", "german", "gospel", "goth", "grindcore", "groove", "grunge", "guitar", "happy", "hard-rock", "hardcore", "hardstyle", "heavy-metal", "hip-hop", "holidays", "honky-tonk", "house", "idm", "indian", "indie", "indie-pop", "industrial", "iranian", "j-dance", "j-idol", "j-pop", "j-rock", "jazz", "k-pop", "kids", "latin", "latino", "malay", "mandopop", "metal", "metal-misc", "metalcore", "minimal-techno", "movies", "mpb", "new-age", "new-release", "opera", "pagode", "party", "philippines-opm", "piano", "pop", "pop-film", "post-dubstep", "power-pop", "progressive-house", "psych-rock", "punk", "punk-rock", "r-n-b", "rainy-day", "reggae", "reggaeton", "road-trip", "rock", "rock-n-roll", "rockabilly", "romance", "sad", "salsa", "samba", "sertanejo", "show-tunes", "singer-songwriter", "ska", "sleep", "songwriter", "soul", "soundtracks", "spanish", "study", "summer", "swedish", "synth-pop", "tango", "techno", "trance", "trip-hop", "turkish", "work-out", "world-music"]
prio_test = ["acoustic", "afrobeat", "ambient"]

algo_test = [{'genre': 'acoustic', 'rating': 1},
 {'genre': 'rock', 'rating': 1},
 {'genre': 'afrobeat', 'rating': 0},
 {'genre': 'rock', 'rating': 1},
 {'genre': 'rock', 'rating': 0},
 {'genre': 'afrobeat', 'rating': 0},
 {'genre': 'rock', 'rating': 1},
 {'genre': 'rock', 'rating': 0},
 {'genre': 'afrobeat', 'rating': 1},
 {'genre': 'rock', 'rating': 1},
 {'genre': 'rock', 'rating': 0},
 {'genre': 'afrobeat', 'rating': 0}]

# algo_result = content_algorithme(df, algo_test)
df = calculate_initial_distribution(genres, prio_test)
df.rename_axis.reset_index()
