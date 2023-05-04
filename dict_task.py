from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('dict_home.html')


@app.route('/api/v1/<word>')
def dict_foo(word):
    definition = pd.read_csv('dictionary.csv')
    word1 = definition.loc[definition['word'] == word]['definition'].squeeze()
    return {'definition': word1, 'word': word}


if __name__ == '__main__':
    app.run(debug=True, port=5002)
