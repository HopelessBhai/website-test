---
layout: home
---
<div style="text-align: center; margin: 20px 0;">
    <h1 style="font-size: 4rem; font-weight: bold; color: #333; font-family: 'Fira Code', monospace; text-decoration: none;">{Welcome}</h1>
    <div id="output" style="font-family: 'Proggy', monospace; font-size: 1.5rem; color: #555; white-space: pre-wrap;"></div>
    <script>
        const outputDiv = document.getElementById("output");
        const messages = [
            "Hello, how are you?", 
            "Hola, ¿cómo estás?", 
            "Bonjour, comment ça va"
        ];
        let currentMessageIndex = 0;
        let charIndex = 0;

        function typeMessage() {
            const message = messages[currentMessageIndex];

            if (charIndex < message.length) {
                outputDiv.textContent += message[charIndex];
                charIndex++;
            } else {
                outputDiv.textContent = " "; // Clear the output for the next message

                // When the current message is complete, move to the next one
                charIndex = 0;
                currentMessageIndex = (currentMessageIndex + 1) % messages.length; // Cycle to the next message
                outputDiv.textContent = " "; // Clear the output for the next message
            }
        }
        setInterval(typeMessage, 200); // Adjust the speed by changing the interval (in ms)

    </script>
</div>

