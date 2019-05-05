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
        'surprise': '52tVDYNwm1JcDGYfvju13g'
    }[feeling]

    print (playlist)

    size = len(response_list)
    randomnum = random.randint(0,size-1)

    answer = str(response_list[randomnum]["Response"]).replace("b'", ""
        ).replace("[", "").replace("']", "").replace("',", "").replace(",",""
        ).replace('b"',"").replace('"',"")

    print (answer)

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
