'''
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import cred


scope = "user-read-recently-played"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.CLIENT_ID, client_secret= cred.CLIENT_SECRET, redirect_uri=cred.REDIRECT_URL, scope=scope))

# auth_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)
# sp = spotipy.Spotify(auth_manager=auth_manager)
'''

import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError
import requests

'''
username = sys.argv[1]
# jakerivera32

try:
    token = util.prompt_for_user_token(username)
except:
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username)

spotifyObject = spotipy.Spotify(auth=token)

# https://open.spotify.com/user/jakerivera32?si=0b1824b4cf5c451a

user = spotifyObject.current_user()

# print(json.dumps(user, sort_keys=True, indent=4))

displayName = user['display_name']
followers = user['followers']['total']


while True:
    print()
    print(">>> Welcome to Spotipy " + displayName + "!")
    print(">>> You have ", followers, " followers.")
    print()
    print("0 - Search for an artist")
    print("1 - get current playing track")
    print("2 - exit")
    print()
    choice = input("Your choice: ")

    if choice == "0":
        print()
        searchQuery = input("Ok, whats their name? ")
        print()

        searchResults = spotifyObject.search(searchQuery,1,0,"artist")
        print(json.dumps(searchResults, sort_keys=True, indent=4))

    if choice == "1":
        print()
        currentTrack = spotifyObject.current_user_playing_track()
        print("The current track playing is: ", currentTrack)

    if choice == "2":
        break

'''

cache_handler = spotipy.cache_handler.CacheFileHandler()
auth_manager = spotipy.oauth2.SpotifyOAuth(scope='user-read-currently-playing',
                                           cache_handler=cache_handler,
                                           show_dialog=True,
                                           open_browser=True)
# webbrowser.open()
if not auth_manager.validate_token(cache_handler.get_cached_token()):
    auth_url = auth_manager.get_authorize_url()
    webbrowser.open(auth_url)
    # auth_manager.get


    x = requests.get(auth_url)
    # print(json.dumps(x, sort_keys=True, indent=4))
    print(x.content)