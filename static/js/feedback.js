function countFeedbackPerMonth(data) {
    const monthCounts = {};
    data.forEach(feedback => {
        // Extract the month and year from the feedback_date
        const monthYear = new Date(feedback.feedback_date).toLocaleString('default', { month: 'long', year: 'numeric' });
        monthCounts[monthYear] = (monthCounts[monthYear] || 0) + 1;
    });
    return monthCounts;
}

document.addEventListener('DOMContentLoaded', function() {
    fetch('/api/feedback')
        .then(response => response.json())
        .then(data => {
            const table = $('#feedbackTable').DataTable({
                data: data,
                columns: [
                    { data: 'feedback_id' },
                    { data: 'user_id' },
                    { data: 'product_id' },
                    { data: 'rating' },
                    { data: 'comment' }
                ]
            });

            // Count feedback per month
            const monthCounts = countFeedbackPerMonth(data);
            const months = Object.keys(monthCounts).sort();
            const counts = months.map(month => monthCounts[month]);

            // Feedback per Month chart
            const ctx = document.getElementById('feedbackChart').getContext('2d');
            const feedbackChart = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: months,
                    datasets: [{
                        label: 'Feedbacks per Month',
                        data: counts,
                        backgroundColor: 'rgba(54, 162, 235, 0.5)',
                        borderColor: 'rgba(54, 162, 235, 1)',
                        borderWidth: 1
                    }]
                },
                options: {
                    responsive: true,
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                }
            });
        })
        .catch(error => console.error('Error fetching feedback data:', error));
});
