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
# import requests
import tkinter
import app

app.startApp()


scope = 'user-read-private user-read-playback-state user-modify-playback-state'
username = 'jakerivera32'
# jakerivera32

try:
    token = util.prompt_for_user_token(username, scope)
# except(AttributeError, JSONDecodeError):
except:
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username, scope)

spotifyObject = spotipy.Spotify(auth=token)

# https://open.spotify.com/user/jakerivera32?si=0b1824b4cf5c451a

# spotifyObject = spotipy.Spotify(auth=token)

devices = spotifyObject.devices()
print(json.dumps(devices, sort_keys=True, indent=4))
deviceID = devices['devices'][0]['id']

track = spotifyObject.current_user_playing_track()
print(json.dumps(track, sort_keys=True, indent=4))
print()
artist = track['item']['artists'][0]['name']
trackName = track['item']['name']

if artist != "":
    print("Currently playing " + artist + " - " + trackName)
    # print(artist)


user = spotifyObject.current_user()
displayName = user['display_name']
followers = user['followers']['total']


while True:
    # Main Menu
    print()
    print (">>> Welcome to Spotipy " + displayName + "!")
    print(">>> You have " + str(followers) + " followers.")
    print()
    print ("0 - Search for an artist")
    print ("1 - exit")
    print ()
    choice = input ("Your choice: ")
    if choice == "0":
        print ()
        print ()
        searchQuery = input ("Ok, what's their name?: ")
        # Get search results
        searchResults = spotifyObject.search (searchQuery, 1,0,"artist")
        # Artist details
        # print(searchResults)
        artist = searchResults ['artists']['items'][0]
        print (artist ['name'])
        print(str(artist ['followers']['total']) + " followers")
        print(artist['genres'] [0])
        print()
        webbrowser.open(artist['images'] [0] ['url'])
        artistID = artist['id']

        # Album and track details
        trackURIs = []
        trackArt = []
        z = 0
        # Extract album data
        albumResults = spotifyObject.artist_albums (artistID)
        albumResults = albumResults['items']
        for item in albumResults:
            print ("ALBUM: " + item ['name' ])
            albumID = item['id']
            albumArt = item['images'][0]['url']
            # Extract track data
            trackResults = spotifyObject.album_tracks(albumID)
            trackResults = trackResults['items']
            for item in trackResults:
                print(str(z) + ": " + item ['name'])
                trackURIs.append(item['uri'])
                trackArt.append(albumArt)
                z+=1
            print ()
        # See album art
        while True:
            songSelection = input ("Enter a song number to see album art and play the song (x to exit): ") # and play the song
            if songSelection == "x":
                break
            trackSelectionList = []
            trackSelectionList.append(trackURIs[int(songSelection)])
        spotifyObject.start_playback(deviceID, None, trackSelectionList) # added webbrowser.open(trackArt [int (songSelection) ])

    if choice == "1":
        break


    # print()
    # print(">>> Welcome to Spotipy " + displayName + "!")
    # print(">>> You have ", followers, " followers.")
    # print()
    # print("0 - Search for an artist")
    # print("1 - get current playing track")
    # print("2 - exit")
    # print()
    # choice = input("Your choice: ")

    # if choice == "0":
    #     print()
    #     searchQuery = input("Ok, whats their name? ")
    #     print()

    #     searchResults = spotifyObject.search(searchQuery,1,0,"artist")
    #     print(json.dumps(searchResults, sort_keys=True, indent=4))

    # if choice == "1":
    #     print()
    #     currentTrack = spotifyObject.current_user_playing_track()
    #     print("The current track playing is: ", currentTrack)

    # if choice == "2":
    #     break



# cache_handler = spotipy.cache_handler.CacheFileHandler()
# auth_manager = spotipy.oauth2.SpotifyOAuth(scope='user-read-currently-playing',
#                                            cache_handler=cache_handler,
#                                            show_dialog=True,
#                                            open_browser=True)
# # webbrowser.open()
# if not auth_manager.validate_token(cache_handler.get_cached_token()):
#     auth_url = auth_manager.get_authorize_url()
#     webbrowser.open(auth_url)
#     # auth_manager.get


#     x = requests.get(auth_url)
#     # print(json.dumps(x, sort_keys=True, indent=4))
#     print(x.content)