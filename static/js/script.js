
// -------------------------------------Profile and Search Toggling--------------------------



// Select the body element
let body = document.body;

// Select the profile element in the header
let profile = document.querySelector('.header .flex .profile');

// When the user button is clicked, toggle the active class on the profile element and remove it from search
document.querySelector('user-btn').onclick = () => {
   profile.classList.toggle('active'); // Toggle visibility of the profile section
   search.classList.remove('active'); // Hide the search form if it's visible
}

// Select the search form element
let search = document.querySelector('.header .flex .search-form');

// When the search button is clicked, toggle the active class on the search form and hide the profile
document.querySelector('#search-btn').onclick = () => {
   search.classList.toggle('active'); // Toggle visibility of the search form
   profile.classList.remove('active'); // Hide the profile if it's visible
}

// Select the slide bar menu element
let slideBar = document.querySelector('.slide-bar');

// When the menu button is clicked, toggle the active class on the slide bar and body
document.querySelector('#menu-btn').onclick = () => {
   slideBar.classList.toggle('active'); // Toggle visibility of the slide menu
   body.classList.toggle('active'); // Add or remove a class from the body to control styling
}

// When the close slide button is clicked, remove the active class from the slide bar and body
document.querySelector('#close-slide-btn').onclick = () => {
   slideBar.classList.remove('active'); // Hide the slide menu
   body.classList.remove('active'); // Remove styling class from the body
}

// Handle scroll events to hide profile and search forms
window.onscroll = () => {
    profile.classList.remove('active'); // Hide the profile section
    search.classList.remove('active'); // Hide the search form

    // If the window width is less than 1200px, remove the slide bar and body active classes
    if (window.innerWidth < 1200) {
        slideBar.classList.remove('active'); // Hide the slide menu on small screens
        body.classList.remove('active'); // Remove styling class from the body
    }
}

// This is for debugging purposes, logs when the page is loaded
document.addEventListener("DOMContentLoaded", () => {
   console.log("Smart Art Chapter List loaded!"); // Log when the DOM is fully loaded
});






// -------------------------------Carousel Slide Functionality-------------------------------





// Variables to control carousel slide
let currentIndex = 0; // Track the current slide index
const slides = document.querySelectorAll('.carousel img'); // Select all carousel images

// Function to show the slide at the given index
function showSlide(index) {
    const totalSlides = slides.length; // Get the total number of slides
    if (index < 0) currentIndex = totalSlides - 1; // If the index is negative, show the last slide
    else if (index >= totalSlides) currentIndex = 0; // If the index exceeds total slides, show the first slide
    else currentIndex = index; // Otherwise, show the requested slide

    const offset = -currentIndex * 100; // Calculate the offset for translation
    document.querySelector('.carousel').style.transform = `translateX(${offset}%)`; // Apply the translation to show the correct slide
}

// Function to show the previous slide
function prevSlide() {
    showSlide(currentIndex - 1); // Decrease the index to go to the previous slide
}

// Function to show the next slide
function nextSlide() {
    showSlide(currentIndex + 1); // Increase the index to go to the next slide
}






// --------------------------------------Dynamic Stats Update---------------------------------






// Stats object to keep track of simulated values
let stats = {
    activeStudents: 0, // Number of active students
    interactiveCourses: 0, // Number of interactive courses
    graduateStudents: 0, // Number of graduate students
    certifiedTeachers: 0, // Number of certified teachers
};

// Set interval to simulate updates to stats every 2 seconds
setInterval(() => {
    stats.activeStudents += Math.floor(Math.random() * 3); // Simulate growth for active students
    stats.interactiveCourses += Math.floor(Math.random() * 2); // Simulate growth for interactive courses
    stats.graduateStudents += Math.floor(Math.random() * 1); // Simulate growth for graduate students
    stats.certifiedTeachers += Math.floor(Math.random() * 1); // Simulate growth for certified teachers

    // Update the text content of the HTML elements with the new stats
    document.getElementById("active-students").textContent = stats.activeStudents;
    document.getElementById("interactive-courses").textContent = stats.interactiveCourses;
    document.getElementById("graduate-students").textContent = stats.graduateStudents;
    document.getElementById("certified-teachers").textContent = stats.certifiedTeachers;
}, 2000); // Repeat this every 2000ms (2 seconds)
