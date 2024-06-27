function processText() {
    const stringS = document.getElementById('string_s').value;
    const textT = document.getElementById('text_t').value;
    const charC = document.getElementById('char_c').value;
    fetch('/process_text', {
        method: 'POST',
        headers: {'Content-Type': 'application/x-www-form-urlencoded'},
        body: `string_s=${stringS}&text_t=${textT}&char_c=${charC}`
    }).then(response => response.json())
      .then(data => {
        document.getElementById('output10').textContent = JSON.stringify(data);
    });
}

function countWords() {
    const stringS = document.getElementById('string_s').value;
    const textT = document.getElementById('text_t').value;
    fetch('/count_words', {
        method: 'POST',
        headers: {'Content-Type': 'application/x-www-form-urlencoded'},
        body: `string_s=${stringS}&text_t=${textT}`
    }).then(response => response.json())
      .then(data => {
        document.getElementById('output11').textContent = JSON.stringify(data);
    });
}

function processStopwords() {
    const stringS = document.getElementById('string_s').value;
    const textT = document.getElementById('text_t').value;
    const stopwords = document.getElementById('stopwords').value.split(',');
    fetch('/process_stopwords', {
        method: 'POST',
        headers: {'Content-Type': 'application/x-www-form-urlencoded'},
        body: `string_s=${stringS}&text_t=${textT}&stopwords[]=${stopwords.join('&stopwords[]=')}`
    }).then(response => response.json())
      .then(data => {
        document.getElementById('output12').textContent = JSON.stringify(data);
    });
}
