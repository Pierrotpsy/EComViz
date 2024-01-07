function aggregateSalesByMonth(data) {
    const monthlySales = {};
    data.forEach(sale => {
        // Extract the month and year from the sale_date
        const monthYear = new Date(sale.sale_date).toLocaleString('default', { month: 'long', year: 'numeric' });
        monthlySales[monthYear] = (monthlySales[monthYear] || 0) + sale.quantity;
    });
    return monthlySales;
}

document.addEventListener('DOMContentLoaded', function() {
    fetch('/api/sales')
        .then(response => response.json())
        .then(data => {
            // Process and display the data in the table
            const table = $('#salesTable').DataTable({
                data: data,
                columns: [
                    { data: 'sale_id' },
                    { data: 'user_id' },
                    { data: 'product_id' },
                    { data: 'quantity' },
                    { data: 'sale_date' }
                ]
            });

            // Aggregate sales by month
            const monthlySales = aggregateSalesByMonth(data);
            const months = Object.keys(monthlySales).sort();
            const salesCounts = months.map(month => monthlySales[month]);

            // Sales per Month chart
            const ctx = document.getElementById('salesChart').getContext('2d');
            const salesChart = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: months,
                    datasets: [{
                        label: 'Sales Quantity per Month',
                        data: salesCounts,
                        backgroundColor: 'rgba(0, 123, 255, 0.5)',
                        borderColor: 'rgba(0, 123, 255, 1)',
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
        .catch(error => console.error('Error fetching sales data:', error));
});
