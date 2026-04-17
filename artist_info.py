import pandas as pd

df = pd.read_csv("dataset/artists.csv")

def get_artist_info(name):
    artist = df[df["name"] == name]

    if artist.empty:
        return {
            "name": name,
            "years": "N/A",
            "genre": "N/A",
            "nationality": "N/A",
            "bio": "No detailed info available"
        }

    artist = artist.iloc[0]

    return {
        "name": artist["name"],
        "years": artist["years"],
        "genre": artist["genre"],
        "nationality": artist["nationality"],
        "bio": artist["bio"]
    }