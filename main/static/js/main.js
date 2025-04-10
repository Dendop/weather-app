document.getElementById('weather-form').addEventListener('submit', function (event) {
    event.preventDefault();  // Prevent page reload on form submit

    // Get the city and selected units from the form
    let city = document.querySelector('[name="city"]').value;
    let units = document.querySelector('input[name="units"]:checked')?.value || 'metric';

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
            document.getElementById('result').innerHTML = `
                <h3>Weather in ${data.city_name}</h3>
                <p>Temperature: ${data.temperature}</p>
                <p>Weather: ${data.description}</p>
                
            `;
        } else if (data.error_message) {
            document.getElementById('result').innerHTML = `<p>Error: ${data.error_message}</p>`;
        }
    })
    .catch(error => {
        console.error("Error:", error);
        document.getElementById('result').innerHTML = "<p>An error occurred. Please try again later.</p>";
    });
});