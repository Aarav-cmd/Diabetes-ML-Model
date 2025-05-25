document.getElementById('predictionForm').addEventListener('submit', function(event) {
  event.preventDefault(); // Prevent the default form submission
  
  var formData = new FormData(this);
  
  fetch('/predict', {
    method: 'POST',
    body: formData
  })
  .then(response => response.text()) // Assuming the response is plain text
  .then(data => {
    document.getElementById('resultContainer').innerText = data; // Assuming you have a div with id="resultContainer" in your result.html
  })
  .catch(error => console.error('Error:', error));
});
