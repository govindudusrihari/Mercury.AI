const messageInput = document.getElementById("message-input");
const sendButton = document.getElementById("send-button");
const messagesContainer = document.querySelector(".chat-messages");

sendButton.addEventListener("click", sendMessage);

function sendMessage() {
  const userMessage = messageInput.value;
  if (userMessage.trim() !== "") {
    displayMessage("user", userMessage); // Add your code for user authentication here
    messageInput.value = ""; 

    // ** Gemini API Interaction (Replace with your Gemini integration): **
    // Example with a fake Gemini API call:
    // 
    // function fakeGeminiResponse(userInput) {
    //   const randomResponse = [
    //     "I understand you're feeling overwhelmed. Take deep breaths.",
    //     "Remember, you're not alone. Talk to a trusted friend or counselor.",
    //     "You are doing great. Keep up the hard work." 
    //   ][Math.floor(Math.random() * 3)]; 
    //   return randomResponse;
    // }
    // const geminiResponse = fakeGeminiResponse(userMessage);

    // You will use your own Gemini integration here.

    // const geminiResponse = await geminiApi.respondToMessage(userMessage);
    // You will likely need an asynchronous fetch request or similar approach to communicate with the API.
    // For example:

    // const geminiResponse = await fetch('/your-gemini-api-endpoint', {
    //   method: 'POST', 
    //   body: JSON.stringify({ message: userMessage }),
    // }).then(response => response.json());


    displayMessage("bot", geminiResponse); // Or whatever response you received from the API
  }
}

function displayMessage(type, message) {
  const messageElement = document.createElement("div");
  messageElement.classList.add("message", `${type}-message`);
  messageElement.textContent = message;
  messagesContainer.appendChild(messageElement);

  messagesContainer.scrollTop = messagesContainer.scrollHeight; // Scroll to bottom
}
