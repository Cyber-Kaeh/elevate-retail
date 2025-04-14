document.addEventListener('DOMContentLoaded', function() {
    const storageKey = 'selectedProducts';
    const paginationLinks = document.querySelectorAll('.pagination a');
    
    // Clear storage on initial page load
    if (!new URLSearchParams(window.location.search).has('page')) {
        localStorage.removeItem(storageKey);
    }

    const checkboxes = document.querySelectorAll('.product-checkbox');
    const counter = document.getElementById('selected-count');
    const form = document.querySelector('form');

    // Persist products over page loads with localStorage
    let selectedProducts = new Set(JSON.parse(localStorage.getItem(storageKey) || '[]'));

    // Get selected checkboxes on page load
    function updateUI() {
        checkboxes.forEach(checkbox => {
            checkbox.checked = selectedProducts.has(checkbox.value);
        });
        counter.textContent = selectedProducts.size;
    }
    updateUI();

    // Update localStorage on checkbox change and update button counter
    function handleCheckboxChange(e) {
        const productId = e.target.value;
        selectedProducts[e.target.checked ? 'add' : 'delete'](productId);
        localStorage.setItem(storageKey, JSON.stringify([...selectedProducts]));
        counter.textContent = selectedProducts.size;
    }

    // Pagination link handler
    paginationLinks.forEach(link => {
        link.addEventListener('click', () => {
            sessionStorage.setItem('preserveSelections', 'true');
        });
    });

    // Modified form submission handler
    form.addEventListener('submit', function(e) {
        // Convert Set to Array
        const selectedArray = Array.from(selectedProducts);

        // Add hidden input with all selected IDs
        const input = document.createElement('input');
        input.type = 'hidden';
        input.name = 'selected_products';
        input.value = selectedArray.join(',');
        form.appendChild(input);

        // Clear storage on successful submission
        localStorage.removeItem(storageKey);
    });

    // Event listeners
    checkboxes.forEach(checkbox => {
        checkbox.addEventListener('change', handleCheckboxChange);
    });

    // Storage cleanup
    window.addEventListener('beforeunload', () => {
        if (!sessionStorage.getItem('preserveSelections')) {
            localStorage.removeItem(storageKey);
        }
        sessionStorage.removeItem('preserveSelections');
    });
});
