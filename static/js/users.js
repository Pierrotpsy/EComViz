function countUsersPerCity(data) {
    const cityCounts = {};
    data.forEach(user => {
        // Assuming city is at the end of the address string after a comma
        const city = user.address.split(',').pop().trim();
        cityCounts[city] = (cityCounts[city] || 0) + 1;
    });
    return cityCounts;
}

document.addEventListener('DOMContentLoaded', function() {
    fetch('/api/users')
        .then(response => response.json())
        .then(data => {
            const table = $('#usersTable').DataTable({
                data: data,
                columns: [
                    { data: 'user_id' },
                    { data: 'name' },
                    { data: 'email' },
                    { data: 'address' },
                    { data: 'join_date' }
                ]
            });

            // Count users per city
            const cityCounts = countUsersPerCity(data);
            const cities = Object.keys(cityCounts);
            const counts = Object.values(cityCounts);

            // Users per City chart
            const ctx = document.getElementById('usersChart').getContext('2d');
            const usersChart = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: cities,
                    datasets: [{
                        label: 'Users per City',
                        data: counts,
                        backgroundColor: 'rgba(0, 123, 255, 0.5)',
                        borderColor: 'rgba(0, 123, 255, 1)',
                        borderWidth: 1
                    }]
                },
                options: {
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                }
            });
        })
        .catch(error => console.error('Error fetching user data:', error));
});
