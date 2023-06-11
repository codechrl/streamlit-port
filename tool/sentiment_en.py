import pickle
import re
from pathlib import Path

import pandas as pd
import tensorflow as tf
from keras.models import model_from_json
from keras_preprocessing.sequence import pad_sequences
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import WordPunctTokenizer, word_tokenize
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

path = str(Path(__file__).parent.absolute())[:-6]

path_eng = path + "lib/sentimen/eng/"
path_indo = path + "lib/sentimen/indo/"


def tweet_cleaner(text):
    tok = WordPunctTokenizer()
    x = text
    # hapus rt
    cl = re.sub(r"\s*RT\s*@[^:]*:.*", "", x)
    cl = re.sub(r"\s*rt\s*@[^:]*:.*", "", cl)
    # hapus mention
    cl = re.sub(r"@[A-Za-z0-9]([^:\s]+)+", "", cl)
    # hapus link
    cl = re.sub(r"https?://[A-Za-z0-9./]+", "", cl)
    # hapus hashtag
    cl = re.sub(r"(?:\s|^)#[A-Za-z0-9\-\.\_]+(?:\s|$)", "", cl)
    # kata ulang
    cl = re.sub(r"\w*\d\w*", "", cl)
    cl = re.sub(r"\b(\w+)(\1\b)+", r"\1", cl)
    # hapus simbol
    cl = re.sub(r"[^a-zA-Z]", " ", cl)
    # lower
    cl = cl.lower()
    # format teks
    cl = tok.tokenize(cl)
    cl = " ".join(cl)
    return cl


def stopword(text):
    stopword_ = set(stopwords.words("english"))
    tokens = word_tokenize(text)
    result = [i for i in tokens if i not in stopword_]
    result = " ".join(result)
    return result


def stopword_indo(text):
    # stopwords sastrawi
    factory = StopWordRemoverFactory()

    # tambah stopwords ke dict sastrawi
    more_stopwords = [line.strip() for line in open(path_indo + "more_stopwords.txt")]
    factory.get_stop_words() + more_stopwords
    stopwords = factory.create_stop_word_remover()

    # hapus stopwords
    result = stopwords.remove(text)
    return result


def stem(text):
    stemmer = PorterStemmer()
    result = []
    text = word_tokenize(text)
    for word in text:
        result.append(stemmer.stem(word))
    result = " ".join(result)
    return result


def stem_indo(text):
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()
    result = stemmer.stem(text)
    return result


def tokenn(input_clean):
    with open(path_eng + "tokenizer_eng.pickle", "rb") as handle:
        tokenizer = pickle.load(handle)
    sequences = tokenizer.texts_to_sequences(input_clean)
    len(tokenizer.word_index)
    #
    length = []
    for x in input_clean:
        length.append(len(x.split()))
    max(length)
    return sequences


def tokenn_indo(input_clean):
    with open(path_indo + "tokenizer_indo.pickle", "rb") as handle:
        tokenizer = pickle.load(handle)
    sequences = tokenizer.texts_to_sequences(input_clean)
    len(tokenizer.word_index)
    #
    length = []
    for x in input_clean:
        length.append(len(x.split()))
    max(length)
    return sequences


def pad(sequences):
    x_train_seq = pad_sequences(sequences, maxlen=70)
    return x_train_seq


global graph
graph = tf.compat.v1.get_default_graph()
print("loading model sentiment eng")
with graph.as_default():
    # load model
    json_file = open(path_indo + "model.json", "r")
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model_indo = model_from_json(loaded_model_json)
    loaded_model_indo.load_weights(path_indo + "weights.hdf5")

with graph.as_default():
    # load model
    json_file = open(path_eng + "model.json", "r")
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model_eng = model_from_json(loaded_model_json)
    loaded_model_eng.load_weights(path_eng + "weights.hdf5")


def predict(text, clean):
    input_clean = text
    ## print(input_clean)

    if clean is not True:
        # text cleaning
        input_clean = tweet_cleaner(input_clean)
        # print(input_clean)
        # stopwords
        input_clean = stopword(input_clean)
        # print(input_clean)
        # stemming
        input_clean = stem(input_clean)
        # print(input_clean)
    # simpan ke dataframe
    df = pd.DataFrame([input_clean], columns=["text"])
    input_clean = df.text
    # tokenizing
    sequences = tokenn(input_clean)
    # padding
    input_ready = pad(sequences)
    # predict classes
    with graph.as_default():
        prediction = loaded_model_eng.predict(input_ready).tolist()
        return prediction[0]


def predict_indo(text, clean):
    input_clean = text

    if clean is not True:
        # text cleaning
        input_clean = tweet_cleaner(input_clean)
        # print(input_clean)
        # stopwords
        input_clean = stopword_indo(input_clean)
        # print(input_clean)
        # stemming
        input_clean = stem_indo(input_clean)
        # print(input_clean)

    # simpan ke dataframe
    df = pd.DataFrame([input_clean], columns=["text"])
    input_clean = df.text
    # tokenizing
    sequences = tokenn_indo(input_clean)
    # padding
    input_ready = pad(sequences)
    # predict classes
    with graph.as_default():
        prediction = loaded_model_indo.predict(input_ready).tolist()

    # return json.dumps(prediction)
    return prediction[0]
