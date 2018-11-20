#     A bot that recomend music according to a given emotion
#     Copyright (C) 2018 Victor Hugo Torres Rivera
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>
from pyswip import Prolog
import time
import json
import tweepy
import random
import spotipy
import datetime
import spotipy.util as spotutil
from json.decoder import JSONDecodeError
from spotipy.oauth2 import SpotifyClientCredentials

json_data=open("secret.json").read()

data = json.loads(json_data)




api_key = data['api_key']
api_secret_key = data['api_secret_key']

access_token = data['access_token']
access_secret_token = data['access_secret_token']

auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_secret_token)
api = tweepy.API(auth)

def build_response(message):
    try:
        string = message

        string = string.replace("@dexterthebot ", "").replace(",", " ").replace(".", ""
            ).replace(" ", ",").replace(",,", ","
            ).replace("'",""
            ).replace("?","").replace("!","").lower()

        plinpupt = "answer(["+ string +"], Feeling, Response)"

        print (plinpupt)
        pl = Prolog()
        pl.consult("../brains/brain.pl")
        response = pl.query(plinpupt)
        response_list = list(response)

        feeling = response_list[0]['Feeling']

        print(feeling)

        playlist = {
            'fear'    : '20Jh7mT0KfGTSEnbDeqbvf',
            'love'    : '4NdkYnfrFDNsVz16AVXKtB',
            'joy'     : '1EFubxF2rhCspgngcyhKBT',
            'anger'   : '5VbdutkbqzGajC7J3TmDjY',
            'sadness' : '67iIzArSbzsIMnb2l7a41y',
            'surprise': 'playlist:52tVDYNwm1JcDGYfvju13g'
        }[feeling]

        print (playlist)

        size = len(response_list)
        randomnum = random.randint(0,size-1)

        answer = str(response_list[randomnum]["Response"]).replace("b'", ""
            ).replace("[", "").replace("']", "").replace("',", "").replace(",",""
            ).replace('b"',"").replace('"',"")

        print (answer)

        # export SPOTIPY_CLIENT_ID='ad4144c5bc114150ab428f04b305004f'
        # export SPOTIPY_CLIENT_SECRET='beff5d5a11804811ad1070f8971b31d0'
        # export SPOTIPY_REDIRECT_URI='http://localhost/'

        spotify = spotipy.Spotify()
        client_credentials_manager = SpotifyClientCredentials()
        sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

        results = sp.user_playlist_tracks('trsmusic.',playlist)
        tracks = results['items']
        while results['next']:
            results = sp.next(results)
            tracks.extend(results['items'])
        tracknum = (len(tracks))

        randomsong = (tracks[randomnum]['track']['external_urls']['spotify'])

        return (answer + " " + randomsong)
    except:
        return("sorry i failed you, im still learning. but here is a song that is good for anything https://open.spotify.com/track/2374M0fQpWi3dLnB54qaLX?si=Vus376VRR3--DsHp3BJitg")

currdate = datetime.datetime.now()
while(True):
    twts = api.search(q="@dexterthebot")
    for s in twts:
        if(s.created_at > currdate):
            response = build_response(s.text)
            username = s.user.screen_name
            newtwt = "@" + username + " " + response
            s = api.update_status(newtwt, s.id)
            currdate = s.created_at
    time.sleep(10)
