from algorithme_utilities import list_is_empty, replace_dash
import pandas as pd

def calculate_initial_distribution(genres, prefered_genres = None):
    if list_is_empty(genres):
        raise Exception("genres is empty!")
    
    genres = list(map(replace_dash, genres)) 
    
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
    genreListNames = list(map(lambda x:x['genre'], genres))
    genreList = list(map(replace_dash), genreListNames)
    
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