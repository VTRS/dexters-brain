from keras.preprocessing.sequence import pad_sequences
from keras.layers.convolutional import MaxPooling1D
from keras.preprocessing.text import Tokenizer
from keras.layers.convolutional import Conv1D
from keras.utils.vis_utils import plot_model
from keras.layers import Embedding
from keras.layers import Dropout
from keras.layers import Flatten
from keras.layers import Dense
from keras.layers import Input
from keras.models import Model
from keras.layers.merge import concatenate
from nltk.corpus import stopwords
import pandas as pd
import numpy as np
import string
import re


# Retrieves just the text from each tweet and deletes stop words
def clean_tweet(tweet):
    tweet = re.sub('[^a-zA-z0-9\s]','',tweet.lower())
    stop_words = set(stopwords.words('english'))
    tweet = tweet.split(' ')
    tweet = [word for word in tweet if not word in stop_words]
    tweet = ' '.join(tweet)
    return tweet

# Loads the data from any given file and divides it to x and y
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

# Create a three channel convolutional neural network for sentiment analysis.
def create_model(length, max_features, embedding_size, filters):
    # Channel 1
    input1 = Input(shape=(length,))
    embedding1 = Embedding(max_features, embedding_size)(input1)
    conv1 = Conv1D(filters=filters, kernel_size=4, activation='relu')(embedding1)
    drop1 = Dropout(0.5)(conv1)
    pool1 = MaxPooling1D(pool_size=2)(drop1)
    flat1 = Flatten()(pool1)
    # Channel 2
    input2 = Input(shape=(length,))
    embedding2 = Embedding(max_features, embedding_size)(input2)
    conv2 = Conv1D(filters=filters, kernel_size=6, activation='relu')(embedding2)
    drop2 = Dropout(0.5)(conv2)
    pool2 = MaxPooling1D(pool_size=2)(drop2)
    flat2 = Flatten()(pool2)
    # Channel 3
    input3 = Input(shape=(length,))
    embedding3 = Embedding(max_features, embedding_size)(input3)
    conv3 = Conv1D(filters=filters, kernel_size=8, activation='relu')(embedding3)
    drop3 = Dropout(0.5)(conv3)
    pool3 = MaxPooling1D(pool_size=2)(drop3)
    flat3 = Flatten()(pool3)
    # merge
    merged = concatenate([flat1, flat2, flat3])
    # interpretation
    dense1 = Dense(8, activation='relu')(merged)
    outputs = Dense(11, activation='sigmoid')(dense1)
    model = Model(inputs=[input1, input2, input3], outputs=outputs)
    # compile
    model.compile(
                loss='binary_crossentropy',
                optimizer='adam',
                metrics=['accuracy'])
    print(model.summary())
    return model


def main():
    # Load datasets for training and testing
    x_train, y_train = load_data('training_data/2018-E-c-En-train.txt')
    x_test, y_test = load_data('training_data/2018-E-c-En-dev.txt')

    # Generate tokenizer
    tokenizer = create_tokenizer(x_train.values)
    # Calculate the maximum number of words per tweet
    maxlen = max_len(x_train.values)
    print('Len:' + str(maxlen))

    # Prepare data for training and testing
    x_train = encode_tweet(tokenizer, x_train, maxlen)
    x_test = encode_tweet(tokenizer, x_test, maxlen)

    # Training variables
    max_features = len(tokenizer.word_index) + 1
    embedding_size = 100
    batch_size = 16
    filters = 32
    epochs = 15

    # Create model using training variables
    model = create_model(maxlen, max_features, embedding_size, filters)
    # Train the model
    model.fit([x_train,x_train,x_train], y_train, epochs=epochs, batch_size=batch_size)
    # Ecaluate the model with the given train dataset,
    score, acc = model.evaluate([x_test,x_test,x_test], y_test, batch_size=batch_size)
    print('Test score:', score)
    print('Test accuracy:', acc)
    #Save model to file
    model.save('multichannelmodelv1.h5')

main()
