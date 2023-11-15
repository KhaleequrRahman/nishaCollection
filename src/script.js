function showCategory(category) {
    // Hide all categories
    const categories = document.querySelectorAll('.category');
    categories.forEach(cat => {
      cat.style.display = 'none';
    });

    // Show the selected category
    document.getElementById(category).style.display = 'block';
  }

 // Smooth scroll when clicking the "Shop Now" button
 document.querySelector('.shop-now-button').addEventListener('click', function() {
  document.getElementById('mainBody').scrollIntoView({ behavior: 'smooth' });
});




