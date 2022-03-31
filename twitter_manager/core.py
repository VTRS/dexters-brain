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
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer
from keras.models import load_model
from json.decoder import JSONDecodeError
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as spotutil
from nltk.corpus import stopwords
from pyswip import Prolog
import pandas as pd
import numpy as np
import datetime
import spotipy
import tweepy
import random
import emoji
import json
import sys
import time
import re

# Global varables used for rest apis auth
json_data=open("secret.json").read()

data = json.loads(json_data)

api_key = data['api_key']
api_secret_key = data['api_secret_key']

access_token = data['access_token']
access_secret_token = data['access_secret_token']

auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_secret_token)
api = tweepy.API(auth)

spotify = spotipy.Spotify()
client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Returns the intersection between two lists.
def intersection(list_a, list_b):
    return [value for value in list_a if value in list_b]

# Returns a random element from a list.
def random_element(list):
    size = len(list)
    rndm = random.randint(0, size-1)
    return list[rndm]

# Returns the tracks from a playlist given its id.
def get_tracks(playlist_id):
    results = sp.user_playlist_tracks('trsmusic.', playlist_id)
    items = results['items']
    tracks = []

    for item in items:
        tracks.append(item['track']['external_urls']['spotify'])

    return tracks

# Returns a random track from a playlist given its id.
def track_from_playlist(playlist_id):
    tracks = get_tracks(playlist_id)
    return random_element(tracks)

# Retunrs a random track from the intersection of 2 playlist given their ids.
def track_from_playlists(playlist_a_id, playlist_b_id):
    tracks_a = get_tracks(playlist_a_id)
    tracks_b = get_tracks(playlist_b_id)
    tracks_c = intersection(tracks_a, tracks_b)
    if(len(tracks_c) > 5):
        return random_element(tracks_c)
    else:
        return random_element(tracks_a)

# Retrieves just the text from each tweet and deletes stop words
def clean_tweet(tweet):
    tweet = re.sub('[^a-zA-z0-9\s]','',tweet.lower())
    stop_words = set(stopwords.words('english'))
    tweet = tweet.split(' ')
    tweet = [word for word in tweet if not word in stop_words]
    tweet = ' '.join(tweet)
    return tweet

# Loads data from any given file
def load_data(filename):
    data = pd.read_csv(filename, delimiter="\t")
    # Clean text from tweets
    data['Tweet'] = data['Tweet'].apply(clean_tweet)
    x= data['Tweet']
    data = data.drop('Tweet', axis=1)
    data = data.drop('ID', axis=1)
    y = data.values
    return x, y

# Creates tokenizer based on a list of tweets
def create_tokenizer(tweets):
    tokenizer = Tokenizer(num_words=20000 , split=' ')
    tokenizer.fit_on_texts(tweets)
    return tokenizer

# Calculates the maximum number of words in a tweet
def max_len(tweets):
    return max(len(tweet.split()) for tweet in tweets)

# Encodes all tweets using the previously created tokenizer and calculated len
def encode_tweet(tokenizer, tweets, len):
    encoded = tokenizer.texts_to_sequences(tweets)
    return pad_sequences(encoded, maxlen = len, padding = 'post')

# Analyses a tweet and retunr the list of the emotions detected
def get_emotions(tweet, model, tokenizer, maxlen):
    # Prepare tweet for the model
    plane_tweet = clean_tweet(tweet)
    experimental_tweet = np.array([plane_tweet])
    experimental_tweet = encode_tweet(tokenizer, experimental_tweet, maxlen)

    # Consult the model
    result = model.predict([experimental_tweet,
                            experimental_tweet,
                            experimental_tweet])
    results = [
        ['anger', "{:.2%}".format(result[0][0])],
        ['anticipation', "{:.2%}".format(result[0][1])],
        ['disgust', "{:.2%}".format(result[0][2])],
        ['fear', "{:.2%}".format(result[0][3])],
        ['joy', "{:.2%}".format(result[0][4])],
        ['love', "{:.2%}".format(result[0][5])],
        ['optimism', "{:.2%}".format(result[0][6])],
        ['pessimism', "{:.2%}".format(result[0][7])],
        ['sadness', "{:.2%}".format(result[0][8])],
        ['surprise', "{:.2%}".format(result[0][9])],
        ['trust', "{:.2%}".format(result[0][10])],
    ]
    try:
        pl = Prolog()
        pl.consult("brains/brain.pl")
        string = plane_tweet.replace("@dexterthebot ", ""
            ).replace(",", " ").replace(".", ""
            ).replace(" ", ",").replace(",,", ","
            ).replace("'",""
            ).replace("?","").replace("!","").lower()
        plinpupt = "answer(["+ string +"], Feeling)"
        response = pl.query(plinpupt)
        response_list = list(response)
        feeling = response_list[0]['Feeling']
    except:
        feeling = 'none'

    return results, feeling

def get_song(emotions, feeling):
    playlist = {
        'fear'    : '20Jh7mT0KfGTSEnbDeqbvf',
        'love'    : '4NdkYnfrFDNsVz16AVXKtB',
        'joy'     : '1EFubxF2rhCspgngcyhKBT',
        'anger'   : '5VbdutkbqzGajC7J3TmDjY',
        'sadness' : '67iIzArSbzsIMnb2l7a41y',
        'surprise': '52tVDYNwm1JcDGYfvju13g',
        'anticipation': '52tVDYNwm1JcDGYfvju13g',
        'optimism': '1EFubxF2rhCspgngcyhKBT',
        'pessimism': '67iIzArSbzsIMnb2l7a41y',
        'disgust' : '20Jh7mT0KfGTSEnbDeqbvf',
        'trust' : '4NdkYnfrFDNsVz16AVXKtB',
    }
    if(feeling != 'none'):
        if (float(emotions[0][1][:-1]) >= 50.0):
            if(emotions[0][0] != feeling):
                primary_emotion = emotions[0][0]
                return track_from_playlists(playlist[primary_emotion],
                                            playlist[feeling])
            else:
                secondary_emotion = emotions[1][0]
                return track_from_playlists(playlist[feeling],
                                            playlist[secondary_emotion])
        else:
            return track_from_playlist(playlist[feeling])

    else:
        if (float(emotions[0][1][:-1]) >= 40.0):
            primary_emotion = emotions[0][0]
            if (float(emotions[1][1][:-1]) >= 30.0):
                secondary_emotion = emotions[1][0]
                return track_from_playlists(playlist[primary_emotion],
                                            playlist[secondary_emotion])
            else:
                return track_from_playlist(playlist[primary_emotion])

    return 'none'

def build_response(emotions, feeling, song):
    possible_responses=open("answers.json").read()
    possible_responses = json.loads(possible_responses)
    if song != 'none':
        if (feeling != 'none'):
            if (float(emotions[0][1][:-1]) >= 50.0):
                feeling = emotions[0][0]
        else:
            feeling = emotions[random.randint(0,1)][0]

        if feeling in ["anticipation", "joy", "love", "optimism", "amazement"]:
            aux = "positive"
        else:
            aux = "negative"

        rand = random.randint(0, len(possible_responses[feeling])-1)
        answer = possible_responses[feeling][rand]
        rand = random.randint(0, len(possible_responses['recommend'][aux])-1)
        recommendation = possible_responses['recommend'][aux][rand]

        return answer + recommendation + song
    else:
        return ("sorry i failed you, im still learning. but here is a song that is good for anything https://open.spotify.com/track/2374M0fQpWi3dLnB54qaLX?si=Vus376VRR3--DsHp3BJitg")

def main():
    # Prepare Model for consulting
    model = load_model('brains/brain.h5')
    x_train, y_train = load_data('brains/data/2018-E-c-En-train.txt')
    tokenizer = create_tokenizer(x_train.values)
    maxlen = max_len(x_train.values)
    currdate = datetime.datetime.now()

    try:
        if api.update_status("hello world"):
            print("Posted")
    except tweepy.error.TweepError as e:
         print(e)

    # while (True):
    #     try:
    #         twts = api.search(q="@dexterthebot")
    #         for s in twts:
    #             if(s.created_at > currdate):
    #                 if (not s.retweeted) and ('RT @' not in s.text):
    #                     print("Tweet:")
    #                     print(s.text)
    #                     tweet = s.text
    #                     emotions, feeling = get_emotions(tweet, model, tokenizer, maxlen)
    #                     emotions.sort(key = lambda a: float(a[1][:-1]), reverse=True)
    #                     song = get_song(emotions, feeling)
    #                     response = build_response(emotions, feeling, song)
    #                     username = s.user.screen_name
    #                     newtwt = "@" + username + " " + response
    #                     print("Response:")
    #                     print(newtwt)
    #                     s = api.update_status(newtwt, s.id)
    #                     currdate = s.created_at
    #     except:
    #         api = tweepy.API(auth, wait_on_rate_limit=True)
    #     time.sleep(7)

main()
