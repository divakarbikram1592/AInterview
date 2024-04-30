from nltk.tokenize import sent_tokenize

from lang_translator.ComplexWords import ComplexWords
from lang_translator.TranslatorLibrary import TranslatorLibrary
from lang_translator.Utils import Utils


class NativeLangTranslatorMain:

    def __init__(self):
        self.utils = Utils()
        self.final_translated_txt = ""

    def get_translated(self, text):
        # en_sentences = sent_tokenize(text)
        #
        # for sentence in en_sentences:
        #
        #     en_complex_words = ComplexWords().get_complex_words(sentence)
        #
        #     hi_sentence = TranslatorLibrary().translate_to_hindi(sentence, "hi")
        #
        #     hi_en_tuples = Utils().get_eng_hindi_words(hi_sentence)
        #
        #     new_hi_sentence = hi_sentence
        #     for tupl in hi_en_tuples:
        #         if tupl[1] in en_complex_words:
        #             new_hi_sentence = new_hi_sentence.replace(" " + tupl[0], " " + tupl[1])
        #
        #     # print(new_hi_sentence)
        # return new_hi_sentence
        complex_words_txt = ComplexWords().get_complex_words(text)

        for sentence in sent_tokenize(text):
            # text = sentence

            complex_words = ComplexWords().get_complex_words(sentence)

            hi_text = TranslatorLibrary().translate_to_hindi(sentence, "hi")
            filtered_hi_words = Utils().remove_hindi_stopwords(hi_text)
            filtered_hi_text = ", ".join(filtered_hi_words)
            translated_text = TranslatorLibrary().translate_to_hindi(filtered_hi_text, "en", True)
            translated_words = translated_text.split(",")
            dictionary = {}
            if len(filtered_hi_words) == len(translated_words):
                dictionary = dict(zip(filtered_hi_words, translated_words))
                # print(dictionary)
            else:
                print("Translation eror: ", len(filtered_hi_words), len(translated_words))

            for hindi_word, english_word in dictionary.items():
                if english_word.lower().strip() in complex_words_txt:
                    hi_text = hi_text.replace(" " + hindi_word, " " + english_word.lower().strip())

            self.final_translated_txt = self.final_translated_txt + hi_text

        # print(final_translated_txt)
        return self.final_translated_txt






