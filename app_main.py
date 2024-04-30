from flask import Flask, render_template, request, redirect, url_for, jsonify

# from lang_translator.NativeLangTranslatorMain import NativeLangTranslatorMain as nlt
from nltk.tokenize import sent_tokenize

from lang_translator.ComplexWords import ComplexWords
from lang_translator.TranslatorLibrary import TranslatorLibrary
from lang_translator.Utils import Utils
from lang_translator.NativeLangTranslatorMain import NativeLangTranslatorMain as nlt

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_data()
    print("data: ", data)
    return redirect(url_for('translate.html', data=data))

@app.route('/translate/', methods=['GET', 'POST'])
def translate():
    text = request.form['htmlContent']
    print("HTML: ", text)
    text = nlt().get_translated(text)
    print("HINDI: ", text)
    return render_template('translate_page.html', data=text)
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

        # print(new_hi_sentence)
    # return new_hi_sentence
    # data = ntl().get_translated(text)
    # print("data: ", data)
    # render_template('translate_page.html', data="data")




if __name__ == '__main__':
    app.run(debug=False, port=8000)
