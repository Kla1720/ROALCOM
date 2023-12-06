#librerias para el procesamiento de lenguaje natural
import numpy as np

#NLTK Punkt es un módulo de la biblioteca de procesamiento de lenguaje natural NLTK de Python que se utiliza para dividir un texto en una lista de oraciones.
import nltk
#nltk.download('punkt')
from nltk.stem import SnowballStemmer
stemmer = SnowballStemmer('spanish')

def tokenize(sentence):
    return nltk.word_tokenize(sentence)


def stem(word):
    
    return stemmer.stem(word.lower())


def bag_of_words(tokenized_sentence, words):

    # stem each word
    sentence_words = [stem(word) for word in tokenized_sentence]
    # initialize bag with 0 for each word
    bag = np.zeros(len(words), dtype=np.float32)
    for idx, w in enumerate(words):
        if w in sentence_words: 
            bag[idx] = 1

    return bag