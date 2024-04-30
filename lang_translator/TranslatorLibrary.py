from googletrans import Translator


class TranslatorLibrary:
    def __init__(self):
        pass


    def translate_to_hindi(self, text, target_language, is_lowercase=False):
        translator = Translator()
        translation = translator.translate(text, dest=target_language)
        if is_lowercase:
            return translation.text.lower()
        else:
            return translation.text

