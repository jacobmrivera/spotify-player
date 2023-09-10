import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError
import requests
import application

RUN_APP = 1

DB = 1


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
    if DB: print(json.dumps(devices, sort_keys=True, indent=4))
    deviceID = devices['devices'][0]['id']
    return devices['devices'][0]

def getCurrentlyPlaying(spotifyObj):
    track = spotifyObj.current_user_playing_track()
    if DB: print(json.dumps(track, sort_keys=True, indent=4))    # Could get a lot more info!
    if track:
        artist = track['item']['artists'][0]['name']
        trackName = track['item']['name']
        print("Currently playing " + artist + " - " + trackName)
    else:
        print("Nothing is currently playing")

def main():
    spotifyObj = setUpSpotify()
    getCurrentDeviceInfo(spotifyObj=spotifyObj)
    getCurrentlyPlaying(spotifyObj)

    if (RUN_APP):
        app = application.App()
        app.mainloop()


if __name__ == "__main__":
         main()