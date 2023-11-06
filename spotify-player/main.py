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
import time

RUN_APP = 1
DB = 1

APP_WIDTH = 400
APP_HEIGHT = 400
    # 0 = 640x640
    # 1 = 300x300
    # 2 = 64x64
ALBUM_SIZE = 1

RUN = True


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

    # 0 = 640x640
    # 1 = 300x300
    # 2 = 64x64
    albumURL = track['item']['album']['images'][ALBUM_SIZE]['url']
    response = requests.get(albumURL)

    if response.status_code == 200:
        with open("album.png", "wb") as f:
            f.write(response.content)
    else:
        print("Failed to download the image")

    return 0

def get_pixel_num_for_album():

    if (ALBUM_SIZE == 0):
        return 640
    elif (ALBUM_SIZE == 1):
        return 300
    elif (ALBUM_SIZE == 2):
        return 64
    else:
        raise Exception("ALBUM_SIZE not a valid number. Please set to 0 || 1 || 2\n")

def detect_new_song(sp, previous):

    current_track = sp.current_playback()

    if current_track is not None:
        # Get the current track's ID
        current_track_id = current_track['item']['id']

        if current_track_id != previous:
            print("Song has changed to:", current_track['item']['name'])
            # Do something when the song changes
            return True
        print("same song")


def main():
    load_dotenv()
    spotifyObj = setUpSpotify()
    getCurrentDeviceInfo(spotifyObj)
    getCurrentlyPlaying(spotifyObj)
    getAlbumImage(spotifyObj)

    if (RUN_APP):
        root = tk.Tk()
        app = application.App(root, spotifyObj, ALBUM_SIZE)
        app.start()
        # detect_new_song(spotifyObj)
        RUN = True

    current_track = spotifyObj.current_playback()
    while (RUN):

        if detect_new_song(spotifyObj, current_track):
            getAlbumImage(spotifyObj)
            app.set_new_album_art()

        time.sleep(1)

if __name__ == "__main__":
         main()