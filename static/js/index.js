document.addEventListener('DOMContentLoaded', function() {
    var form = document.getElementById('sentiment-form');
    var resultDiv = document.getElementById('result');
    var resultImage = document.getElementById('result-image');

    form.addEventListener('submit', function(event) {
        event.preventDefault();

        var text = document.getElementById('text').value;

        fetch('/predict-sentiment', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ text: text })
        })
        .then(response => response.json())
        .then(data => {
            resultDiv.innerHTML = 'The sentiment of the text is: ' + data.sentiment;
            resultImage.src = '/static/images/' + data.sentiment + '.jpg';
            resultImage.style.display = 'block';
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
});