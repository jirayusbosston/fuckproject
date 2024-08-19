function fetchData() {
    fetch('/api/robot/data')
        .then(response => response.json())
        .then(data => {
            document.getElementById('position').textContent = data.position;
            document.getElementById('energy').textContent = data.energy;
            document.getElementById('speed').textContent = data.speed;
            document.getElementById('torque').textContent = data.torque;
        })
        .catch(error => console.error('Error fetching data:', error));
}

fetchData();
setInterval(fetchData, 5000); // Update data every 5 seconds