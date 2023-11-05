import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError
import requests
import application
from dotenv import load_dotenv
import tkinter as tk

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
        # os.remove(f".cache-{username}")
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
    return track

def getAlbumImage(spotO):

    track = getCurrentlyPlaying(spotO)
    albumURL = track['item']['album']['images'][0]['url']
    response = requests.get(albumURL)

    if response.status_code == 200:
        with open("album.png", "wb") as f:
            f.write(response.content)
    else:
        print("Failed to download the image")

    return 0



def main():
    load_dotenv()
    spotifyObj = setUpSpotify()
    getCurrentDeviceInfo(spotifyObj=spotifyObj)
    getCurrentlyPlaying(spotifyObj)
    getAlbumImage(spotifyObj)
    if (RUN_APP):
        root = tk.Tk()
        root.geometry("400x300")
        app = application.App(root)
        app.start()


if __name__ == "__main__":
         main()