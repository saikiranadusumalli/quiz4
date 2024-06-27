from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process_text', methods=['POST'])
def process_text():
    S = request.form['string_s']
    T = request.form['text_t']
    C = request.form['char_c']
    count_chars = {char: T.count(char) for char in S}
    total_chars = len(T)
    freq_chars = {char: count_chars.get(char, 0) / total_chars for char in S}
    replaced_text = ''.join([C if char in S else char for char in T])
    return jsonify(counts=count_chars, frequencies=freq_chars, replaced=replaced_text)

@app.route('/count_words', methods=['POST'])
def count_words():
    S = request.form['string_s']
    T = request.form['text_t']
    words = T.split()
    word_count = len(words)
    starts_with = {char: [word for word in words if word.startswith(char)] for char in S}
    return jsonify(word_count=word_count, starts_with=starts_with)

@app.route('/process_stopwords', methods=['POST'])
def process_stopwords():
    S = request.form['string_s']
    T = request.form['text_t']
    P = request.form.getlist('stopwords[]')
    words = T.split()
    filtered_words = [word for word in words if word.lower() not in P]
    removal_count = len(words) - len(filtered_words)
    updated_text = ' '.join(filtered_words)
    bigrams = {}
    for i, word in enumerate(filtered_words):
        if word[0] in S:
            before = ' '.join(filtered_words[max(i-1, 0):i+1])
            after = ' '.join(filtered_words[i:i+2])
            bigrams[word] = [before, after]
    return jsonify(removal_count=removal_count, updated_text=updated_text, bigrams=bigrams)

if __name__ == '__main__':
    app.run(debug=True)
