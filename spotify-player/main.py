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


def setUpSpotify():
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

    return spotifyObject


def getCurrentDeviceInfo(spotifyObj):
    devices = spotifyObj.devices()
    print(json.dumps(devices, sort_keys=True, indent=4))
    deviceID = devices['devices'][0]['id']
    return devices['devices'][0]


def main():
    spotifyObj = setUpSpotify()
    getCurrentDeviceInfo(spotifyObj=spotifyObj)



if __name__ == "__main__":
         main()