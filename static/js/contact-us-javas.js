// let utterance;

// document.getElementById("read-aloud").addEventListener("click", () => {
//   // Get the text content of the page
//   const pageText = document.body.innerText;  // This retrieves all text content of the body
  
//   // Create a new SpeechSynthesisUtterance object to convert text to speech
//   utterance = new SpeechSynthesisUtterance(pageText);
  
//   // Set some options for the voice (optional)
//   utterance.lang = "en-US";  // Set the language
//   utterance.volume = 1;      // Volume (0 to 1)
//   utterance.rate = 1;        // Speech speed (0.1 to 10)
//   utterance.pitch = 1;       // Pitch (0 to 2)
  
//   // Use the SpeechSynthesis API to speak the text
//   window.speechSynthesis.speak(utterance);
// });

// document.getElementById("stop-reading").addEventListener("click", () => {
//   // Stop any ongoing speech
//   window.speechSynthesis.cancel();
// });

// Select all FAQ items on the page with the class 'faq-item'
const faqItems = document.querySelectorAll('.faq-item');

// Loop through each FAQ item
faqItems.forEach(item => {
    // Select the question and answer elements within each FAQ item
    const question = item.querySelector('.faq-question');
    const answer = item.querySelector('.faq-answer');
    // Select the icon inside the question (usually an arrow)
    const icon = question.querySelector('i');
    
    // Add a click event listener to the question
    question.addEventListener('click', () => {
        // Toggle the 'active' class on the answer, showing or hiding it
        answer.classList.toggle('active');
        
        // If the answer is now visible (active), change the arrow direction
        if (answer.classList.contains('active')) {
            // Remove the down arrow and add the up arrow
            icon.classList.remove('fa-chevron-down');
            icon.classList.add('fa-chevron-up');
        } else {
            // Remove the up arrow and add the down arrow when the answer is hidden
            icon.classList.remove('fa-chevron-up');
            icon.classList.add('fa-chevron-down');
        }
    });
});

// Add a click event listener to the chat button
document.querySelector('.chat-btn').addEventListener('click', function() {
    // Alert the user that live chat is starting
    alert('Starting Live Chat...');
    // Here you can integrate a live chat service, like Intercom or another
});
