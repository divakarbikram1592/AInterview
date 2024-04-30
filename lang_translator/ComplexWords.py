import nltk
import re
import numpy as np
from nltk.corpus import cmudict


class ComplexWords:

    def __init__(self):
        self.pronouncing_dict = cmudict.dict()

    def count_syllables(self, word):
        """
        Count syllables in a word using the CMU Pronouncing Dictionary.
        """

        if word.lower() in self.pronouncing_dict:
            return [len(list(y for y in x if y[-1].isdigit())) for x in self.pronouncing_dict[word.lower()]]
        else:
            # If word not found in dictionary, return -1
            return -1


    def is_complex(self, word, threshold=2):
        """
        Check if a word is complex based on the number of syllables.
        """
        syllable_count = self.count_syllables(word)
        if syllable_count == -1:
            # Word not found in dictionary
            return False
        return max(syllable_count) >= threshold

    def get_complex_words(self, text, threshold=2, ignore_punctuation=True):
        """
        Get a list of complex words from the given text.
        """
        # Remove all specia character
        text = re.sub('[^a-zA-Z0-9 \n\.]', ' ', text)

        # Tokenize text into words
        words = nltk.word_tokenize(text)

        # Initialize list to store complex words
        complex_words = []

        for word in words:
            # Remove punctuation
            if ignore_punctuation:
                word = re.sub(r'[^\w\s]', '', word)

            # Skip empty strings and single characters
            if len(word) < 2:
                continue

            # Check if word is complex
            if self.is_complex(word, threshold):
                complex_words.append(word)

        return np.unique(complex_words)
