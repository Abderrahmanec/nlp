document.addEventListener('DOMContentLoaded', function() {
    // DOM Elements
    const productsGrid = document.getElementById('productsGrid');
    const feedbackModal = document.getElementById('feedbackModal');
    const feedbackForm = document.getElementById('feedbackForm');
    const closeBtn = document.querySelector('.close-btn');
    const searchInput = document.getElementById('searchInput');
    const successToast = document.getElementById('successToast');

    
    
    // Product data with prices (can be replaced with API data)
   
    // Initialize the app
    initApp();
    
    function initApp() {
        // Load products (using local data in this example)
        displayProducts(productsData);
        
        // Event listeners
        closeBtn.addEventListener('click', closeModal);
        feedbackForm.addEventListener('submit', handleFeedbackSubmit);
        searchInput.addEventListener('input', handleSearch);
        
        // Close modal when clicking outside
        window.addEventListener('click', (e) => {
            if (e.target === feedbackModal) {
                closeModal();
            }
        });
    }
    
    function displayProducts(products) {
        if (products.length === 0) {
            productsGrid.innerHTML = `
                <div class="empty-state">
                    <i class="fas fa-box-open"></i>
                    <h3>No Products Found</h3>
                    <p>There are currently no products available.</p>
                </div>
            `;
            return;
        }
        
        
    }
    
    function handleSearch() {
        const searchTerm = searchInput.value.toLowerCase();
        const productCards = document.querySelectorAll('.product-card');
        
        productCards.forEach(card => {
            const productName = card.querySelector('h3').textContent.toLowerCase();
            const productDesc = card.querySelector('p:not(.price)').textContent.toLowerCase();
            
            if (productName.includes(searchTerm) || productDesc.includes(searchTerm)) {
                card.style.display = 'flex';
            } else {
                card.style.display = 'none';
            }
        });
    }
    
    function openFeedbackModal(productId) {
        document.getElementById('productId').value = productId;
        
        // Get product details to show in modal
        const product = productsData.find(p => p.id === productId);
        if (product) {
            const modalHeader = feedbackModal.querySelector('.modal-header');
            modalHeader.innerHTML = `
                <h2><i class="fas fa-edit"></i> Share Your Feedback</h2>
                <p>We value your opinion about ${product.name} ($${product.price.toFixed(2)})</p>
            `;
        }
        
        feedbackModal.style.display = 'flex';
        document.body.style.overflow = 'hidden';
    }
    
    function closeModal() {
        feedbackModal.style.display = 'none';
        document.body.style.overflow = 'auto';
        feedbackForm.reset();
    }
    
    async function handleFeedbackSubmit(e) {
        e.preventDefault();
        
        const productId = document.getElementById('productId').value;
        const comment = document.getElementById('comment').value;
        const rating = document.querySelector('input[name="rating"]:checked')?.value;
        
        if (!rating) {
            alert('Please select a rating');
            return;
        }
        
        try {
            // In a real app, you would send this to your backend API
            // For this example, we'll just log it and show a success message
            console.log('New feedback submitted:', {
                productId,
                comment,
                rating,
                date: new Date().toISOString()
            });
            
            // Show success toast
            showToast('Thank you for your feedback!');
            
            // Close modal and reset form
            closeModal();
        } catch (error) {
            console.error('Error submitting feedback:', error);
            alert('There was an error submitting your feedback. Please try again.');
        }
    }
    
    function showToast(message) {
        const toast = document.getElementById('successToast');
        const toastText = toast.querySelector('span');
        
        toastText.textContent = message;
        toast.style.display = 'flex';
        
        // Hide after 3 seconds
        setTimeout(() => {
            toast.style.display = 'none';
        }, 3000);
    }
});

// Make openModal globally available for onclick attributes
function openFeedbackModal(productId) {
    document.getElementById('productId').value = productId;
    document.getElementById('feedbackModal').style.display = 'flex';
    document.body.style.overflow = 'hidden';
}

