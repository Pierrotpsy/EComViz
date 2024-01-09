document.addEventListener('DOMContentLoaded', function() {
  fetch('/api/products')
      .then(response => response.json())
      .then(data => {
          const table = $('#productsTable').DataTable({
              data: data,
              columns: [
                  { data: 'product_id' },
                  { data: 'name' },
                  { data: 'description' },
                  { data: 'price' },
                  { data: 'category' }
              ]
          });

          const ctx = document.getElementById('productsChart').getContext('2d');
          const productsChart = new Chart(ctx, {
              type: 'bar',
              data: {
                  labels: data.map(item => item.name),
                  datasets: [{
                      label: 'Price',
                      data: data.map(item => item.price),
                      backgroundColor: 'rgba(54, 162, 235, 0.2)',
                      borderColor: 'rgba(54, 162, 235, 1)',
                      borderWidth: 1
                  }]
              },
              options: {
                  scales: {
                      y: { beginAtZero: true }
                  }
              }
          });
      })
      .catch(error => console.error('Error fetching product data:', error));
});
