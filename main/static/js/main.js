document.getElementById('weather-form').addEventListener('submit', function (event) {
    event.preventDefault();  // Prevent page reload on form submit

    // Get the city and selected units from the form
    let city = document.querySelector('[name="city"]').value;
    let units = document.querySelector('input[name="units"]:checked')?.value || 'metric';

    const resultDiv = document.getElementById('result');
    

    //hide result, untill data is received
    resultDiv.style.visibility = 'hidden';
    resultDiv.innerHTML = "";
 
    // Send a POST request to the backend
    fetch('/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ city: city, units: units })
    })
    .then(response => response.json())  // Convert the response to JSON
    .then(data => {
        // Handle response data here
        if (data.temperature) {
            const iconPath = `/static/images/icons/${data.icon_filename}`;

            document.getElementById('result').innerHTML = `
                <h2>Today</h2>
                <img src="${iconPath}" alt="weather icon" class = "weather-icon" />
                <p>${data.temperature}${units === 'metric' ? 'C' : 'F'}</p>
                <p>${data.description}</p>
                
                
            `;
        } else if (data.error_message) {
            document.getElementById('result').innerHTML = `<p>Error: ${data.error_message}</p>`;
        }
        resultDiv.style.visibility = 'visible';
    })
    .catch(error => {
        console.error("Error:", error);
        document.getElementById('result').innerHTML = "<p>Could not find the city. Try again.</p>";
        resultDiv.style.visibility = 'visible';
    });
});