import underthesea
from flask import Flask, jsonify, request

app = Flask(__name__)


def get_text():
    data = request.get_json()
    return data.get('text', '')


def get_domain():
    data = request.get_json()
    return data.get('domain')


@app.route('/segment_sentence', methods=['POST'])
def segment_sentence():
    text = get_text()
    sentences = underthesea.sent_tokenize(text)
    return jsonify(sentences)


@app.route('/tokenize_word', methods=['POST'])
def tokenize_word():
    text = get_text()
    words = underthesea.word_tokenize(text)
    return jsonify(words)


@app.route('/pos_tag', methods=['POST'])
def pos_tag():
    text = get_text()
    tags = underthesea.pos_tag(text)
    tags = [{'word': tag[0], 'tag': tag[1]} for tag in tags]
    return jsonify(tags)


@app.route('/chunk', methods=['POST'])
def chunk():
    text = get_text()
    tags = underthesea.chunk(text)
    tags = [{
                'word': tag[0],
                'pos_tag': tag[1],
                'chunk_tag': tag[2],
            } for tag in tags]
    return jsonify(tags)


@app.route('/ner', methods=['POST'])
def ner():
    text = get_text()
    tags = underthesea.ner(text)
    tags = [{
                'word': tag[0],
                'pos_tag': tag[1],
                'chunk_tag': tag[2],
                'ner_tag': tag[3],
            } for tag in tags]
    return jsonify(tags)


@app.route('/classify', methods=['POST'])
def classify():
    text = get_text()
    domain = get_domain()
    categories = underthesea.classify(text, domain)
    return jsonify(categories)


@app.route('/sentiment', methods=['POST'])
def sentiment():
    text = get_text()
    domain = get_domain()
    result = underthesea.sentiment(text, domain)
    return jsonify(result)


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
