from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    with open('index.html', 'r') as file:
        return file.read()

@app.route('/process_text', methods=['POST'])
def process_text():
    text_s = request.form['string_s']
    char_c = request.form['char_c']

    # Count each character in S
    count_chars = {char: text_s.count(char) for char in set(text_s)}

    # Calculate frequency of each character in S
    total_chars = len(text_s)
    freq_chars = {char: count / total_chars for char, count in count_chars.items()}

    # Replace all characters in S with C
    replaced_text = ''.join([char_c if char in text_s else char for char in text_s])

    result = f"Counts: {count_chars}, Frequencies: {freq_chars}, Replaced Text: {replaced_text}"
    return result

if __name__ == '__main__':
    app.run(debug=True)
