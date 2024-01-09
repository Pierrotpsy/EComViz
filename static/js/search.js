document.getElementById('searchButton').addEventListener('click', () => {
  const query = document.getElementById('searchInput').value;
  fetch(`/api/search?query=${encodeURIComponent(query)}`)
      .then(response => response.json())
      .then(data => {
          const resultsContainer = document.getElementById('searchResults');
          resultsContainer.innerHTML = '';  // Clear previous results
          data.forEach(doc => {
              // Display each document as a block of text or a card
              const docDiv = document.createElement('div');
              docDiv.className = 'search-result';
              docDiv.textContent = JSON.stringify(doc, null, 2);
              resultsContainer.appendChild(docDiv);
          });
      })
      .catch(error => console.error('Error fetching search results:', error));
});
