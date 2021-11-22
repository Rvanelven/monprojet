import nltk

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def remove_punct(text):
    for punctuation in string.punctuation:
        text = text.replace(punctuation, '')
    return text


def lower_text(text):
    text = text.lower()
    return text


def remove_numbers(text):
    text = ''.join(char for char in text if not char.isdigit())
    return text


def remove_stopwords(text, langage):
    stop_words = set(stopwords.words(langage))
    word_tokens = word_tokenize(text)
    text = ' '.join(w for w in word_tokens if not w in stop_words)
    return text


def lemmat(text):
    lemmatizer = WordNetLemmatizer()
    word_tokens = word_tokenize(text)
    lemmatized = [lemmatizer.lemmatize(word) for word in word_tokens]
    return ' '.join(lemmatized)


def clean_text(df_col, langage):
    df_col = df_col.apply(remove_punct)
    df_col = df_col.apply(lower_text)
    df_col = df_col.apply(remove_numbers)
    df_col = df_col.apply(lambda x: remove_stopwords(x, langage))
    df_col = df_col.apply(lemmat)
    return df_col
