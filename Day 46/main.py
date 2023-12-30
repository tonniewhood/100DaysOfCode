
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth
import spotipy
import requests
import os
import base64

URL = "https://www.billboard.com/charts/hot-100/"
SPOTIFY_CLIENT_ID = "fcc6e6be82044f41ae0383d877009cb7"
SPOTIFY_API_KEY = "7d2eb10752f443b79e60ce3d22c6d866"
AUTH_CODE = "ZnIJUcYHeg93"

def main():

    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")

    songs = [song.getText().strip() for song in soup.select(".o-chart-results-list__item > h3")]

    scope = ["playlist-modify-private", "playlist-modify-public", "playlist-read-private"]

    sp = SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_API_KEY, redirect_uri="http://127.0.0.1:5500/index.html", scope=scope)
    token = sp.get_access_token(as_dict=False)

    client = spotipy.Spotify(auth=token)
    playListID = "3EfQPYXS4X7xX2TJRIcs7X"
    userID = "f16squidget"

    songsToAdd = []
    for song in songs:
        songResults = client.search(q=song, limit=1, offset=0, type="track")
        songURI = songResults["tracks"]["items"][0]["uri"]
        songsToAdd.append(songURI)

        
    response = client.user_playlist_add_tracks(user=userID, playlist_id=playListID, tracks=songsToAdd)
    print(response)

    # mariahURI = client.search(q="All I Want For Christmas Is You", limit=1, offset=0, type="track")["tracks"]["items"][0]["uri"]

    # response = client.user_playlist_add_tracks(user=userID, playlist_id=playListID, tracks=[mariahURI])
    # print(response)

    # query = "All I Want For Christmas Is You"
    # limit = 1
    # offset = 0
    # type = "track"





    # songResults = client.search(q=query, limit=limit, offset=offset, type=type)
    # song = songResults["tracks"]["items"][0]["uri"]

    # print(song)




if __name__ == "__main__":
    main()