// Select elements from the DOM

const navLinks = document.querySelectorAll('nav a');
const form = document.querySelector('form');
const successMessage = document.querySelector('#success-message');
const errorMessage = document.querySelector('#error-message');

// Handle form submission

form.addEventListener('submit', (event) => {
  event.preventDefault();

  // Get form data

  const itemType = form.elements['item-type'].value;
  const itemDescription = form.elements['item-description'].value;
  const itemLocation = form.elements['item-location'].value;
  const itemDate = form.elements['item-date'].value;
  const itemImage = form.elements['item-image'].value;

  // Validate form data

  if (!itemType || !itemDescription || !itemLocation || !itemDate || !itemImage) {
    errorMessage.textContent = 'Please fill out all fields.';
    errorMessage.style.display = 'block';
    return;
  }

  // Submit form data

  // Here you would make an AJAX request to submit the form data to a server-side script
  // For the sake of simplicity, we'll just display a success message

  successMessage.style.display = 'block';
  form.reset();
});

// Handle navigation

navLinks.forEach((link) => {
  link.addEventListener('click', (event) => {
    event.preventDefault();

    // Get section ID from link href

    const sectionId = link.getAttribute('href').slice(1);

    // Scroll to section

    const section = document.getElementById(sectionId);

    section.scrollIntoView({ behavior: 'smooth' });
  });
});
