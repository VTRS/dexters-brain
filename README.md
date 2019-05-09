# [@dexterthebot](https://twitter.com/dexterthebot)

<p align="center">
  <img width="460" src="imgs/face_nobg.png">
</p>

Dexter is a friendly Twitter bot that promotes sentiment expression by analyzing feelings from people he interacts with, building a response and sharing a song that might help them.

Once Dexter is tagged in a tweet, he analyzes the emotions that are present in the text using a Multichannel Convolutional Neural Network and then builds a response given a set of predefined answers and then tweets back to the user with a song that might express the same emotion.

## Your own smart friendly bot

Dexter is open source which means that you can build your own version, also if you have any ideas on how to improve it, contact us and we can work together on something new and better.

### Prerequisites

You will need to create a couple developer accounts for the bot to work.
1. [Twitter develoer account](https://developer.twitter.com/en/apply-for-access)
2. [Spotify for developers](https://developer.spotify.com/)

You should also have installed

Python3
```bash
$ sudo apt-get install python3
```
Virtualenv
```bash
$ sudo apt-get install virtualenv
```
Prolog
```bash
$ sudo add-apt-repository ppa:swi-prolog/stable
$ sudo apt-get update
$ sudo apt-get install swi-prolog
```

### Installing

First of all, it is recommended to create a virtual environment for the project and activate it.
```bash
$ virtualenv -p Python3 venv
$ source venv/bin/activate
```
Install all the required packages
```bash
$ pip install -r requirements.txt
```
Since stopwords from nltk will be used later for the project you shoul install it from python
```bash
$ python
>>> import nltk
>>> nltk.download('stopwords')
```
Next you should prepare your developer credentials for the bot to work properly
```bash
$ export SPOTIPY_CLIENT_ID='your_client_id'
$ export SPOTIPY_CLIENT_SECRET='your_client_secret'
$ export SPOTIPY_REDIRECT_URI='http://localhost/'
```
For the twitter integration you shuld create a json file with the necessary credentials. (This file must be named secret.json in order to be ignored by git)

Example of secret.json
```json
{
  "api_key": "your_api_key",
  "api_secret_key" : "your_api_secret_key",
  "access_token" : "your_access_token",
  "access_secret_token" : "your_access_secret_token",
}
```

Finally for it to work properly you should edit the main function from the core.py file that is in twitter_manager folder.

~~``` twts = api.search(q="@dexterthebot") ```~~

```twts = api.search(q="@yourbotsname")```

Now everything should be ready for the bot to work properly,
so simply run the core.py file from twitter_manager folder and is ready to go.
```bash
$ python twitter_manager/core.py
```

## Authors

* **Victor Hugo Torres Rivera** - [VTRS](https://github.com/VTRS)
* **Carlos Román Rivera** - [croman96](https://github.com/croman96)

## License

This project is licensed under the [GNU AFFERO GENERAL PUBLIC LICENSE](LICENSE)

## Acknowledgments
* Inspired in [jonny sun's work](https://twitter.com/jonnysun)
