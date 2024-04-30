import string

from nltk.tokenize import word_tokenize, sent_tokenize
from stopwords_hindi import hindi_sw as sw
import numpy as np
# import re
import regex as reg

from lang_translator.TranslatorLibrary import TranslatorLibrary


class Utils:

    @staticmethod
    def str2bool(v):
        if v.lower() in ('yes', 'true', 't', 'y', '1'):
            return True

    def remove_en_stopwords(self, text):
        pass

    def remove_hindi_stopwords(self, text):
        stopwords = sw.get_hindi_sw()

        pattern = r'[^\w\s\.,:;]+'
        text = reg.sub(pattern, ' ', text)

        tokens = np.unique(word_tokenize(text))
        result_hi_words = [word for word in tokens if word not in stopwords and len(word) > 3]
        return result_hi_words

    def get_eng_hindi_words(self, text):
        filtered_hi_words = self.remove_hindi_stopwords(text)
        hi_en_tuples = [(word, TranslatorLibrary().translate_to_hindi(word, "en").lower()) for word in filtered_hi_words]

        return hi_en_tuples
