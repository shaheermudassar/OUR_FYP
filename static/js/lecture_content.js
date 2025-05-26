document.getElementById("read-aloud").addEventListener("click", () => {
    // Get the text content of the page
    const pageText = document.body.innerText;  // This retrieves all text content of the body
    
    // Create a new SpeechSynthesisUtterance object to convert text to speech
    const utterance = new SpeechSynthesisUtterance(pageText);
    
    // Set some options for the voice (optional)
    utterance.lang = "en-US";  // Set the language
    utterance.volume = 1;      // Volume (0 to 1)
    utterance.rate = 1;        // Speech speed (0.1 to 10)
    utterance.pitch = 1;       // Pitch (0 to 2)
    
    // Use the SpeechSynthesis API to speak the text
    window.speechSynthesis.speak(utterance);
  });
  