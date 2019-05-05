import random
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

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
    if(len(tracks_c) > 0):
        return random_element(tracks_c)
    else:
        return random_element(tracks_a)

song = track_from_playlists('5VbdutkbqzGajC7J3TmDjY', '67iIzArSbzsIMnb2l7a41y')
