from toolbox.nlp import clean_text
import pandas as pd


def test_clean_text():
    type(clean_text(pd.Series(['texte123', 'ALLO']),
                    'english')) == pd.core.series.Series
