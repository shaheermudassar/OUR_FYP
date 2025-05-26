// Function to toggle the visibility of the chat box
function toggleChat() {
    // Get the chatBox element using its ID
    let chatBox = document.getElementById("chatBox");
    
    // Toggle the display style between 'none' and 'block'
    // If it's currently hidden (display: none), show it (display: block), else hide it
    chatBox.style.display = chatBox.style.display === "none" ? "block" : "none";
}

// Function to open the chat box (always display it)
function openChat() {
    // Get the chatBox element and set its display style to 'block' to show it
    document.getElementById("chatBox").style.display = "block";
}

// Function to send a message from the user and receive a response from the AI
async function sendMessage() {
    // Get references to the input box and chat message container
    let userInput = document.getElementById("userInput");
    let chatMessages = document.getElementById("chatMessages");
    let spinner = document.getElementById("loadingSpinner");

    // Get the trimmed message entered by the user
    let messageText = userInput.value.trim();
    
    // If the message is empty, return early and do nothing
    if (messageText === "") return;

    // Create a new paragraph element to display the user's message
    let userMsg = document.createElement("p");
    userMsg.textContent = "You: " + messageText; // Set the text to include the user message
    chatMessages.appendChild(userMsg); // Append the user's message to the chat container

    // Clear the user input field after sending the message
    userInput.value = "";
    
    // Show the loading spinner while waiting for the AI's response
    spinner.style.display = "block"; 

    // Send a POST request to the Django backend to process the AI chat
    let response = await fetch("/ai-chat/", {
        method: "POST", // Specify the HTTP method as POST
        headers: { "Content-Type": "application/json" }, // Set the content type to JSON
        body: JSON.stringify({ message: messageText }) // Send the user message in the request body
    });

    // Wait for the response to be returned from the backend
    let data = await response.json(); // Parse the JSON response

    // Create a new paragraph element to display the AI's response
    let botMsg = document.createElement("p");
    botMsg.textContent = "AI: " + (data.response || "Error fetching response"); // If the response exists, show it, else show an error message
    chatMessages.appendChild(botMsg); // Append the AI's message to the chat container

    // Hide the loading spinner once the response is received
    spinner.style.display = "none"; 
}
