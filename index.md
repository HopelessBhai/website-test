---
layout: home
---

<div style="text-align: center; margin: 20px 0;">
    <h1 id="welcome" style="font-size: 4rem; font-weight: bold; color: var(--text-color); font-family: 'Fira Code', monospace; text-decoration: none;"></h1>
    <br>
    <p id="output" style="font-family: 'Proggy', monospace; font-size: 1.5rem; color: var(--text-color); white-space: pre-wrap; visibility: visible;">Navigate below to find my blogs</p>
    <script>
        const welcomeDiv = document.getElementById("welcome");
        const outputParagraph = document.getElementById("output");

        const blinkText = [".", "|"];
        const halloText = "Hello";
        const welcomeText = "Welcome to my blog.";

        let phase = 0;
        let charIndex = 0;
        let tempText = "";

        let blinked = false;

        function typeHeading() {
            if (phase === 0) {
                // Phase 0: Blink dots
                tempText = blinkText[charIndex % blinkText.length];
                welcomeDiv.textContent = "{" + tempText + "}";
                charIndex++;
                if (charIndex === blinkText.length * 2) { // Blink dots twice
                    phase++;
                    charIndex = 0;
                    tempText = "";
                    setTimeout(typeHeading, 200); // Move to next phase
                } else {
                    setTimeout(typeHeading, 300); // Continue blinking
                }
            } else if (phase === 1) {
                // Phase 1: Type Hallo
                if (charIndex < halloText.length) {
                    tempText += halloText[charIndex];
                    charIndex++;
                    welcomeDiv.textContent = "{" + tempText + "}";
                    setTimeout(typeHeading, 100);
                } else {
                    phase++;
                    setTimeout(typeHeading, 500); // Pause before erasing
                }
            } else if (phase === 2) {
                // Phase 2: Erase Hallo
                if (charIndex > 0) {
                    tempText = tempText.slice(0, -1);
                    charIndex--;
                    welcomeDiv.textContent = "{" + tempText + "}";
                    setTimeout(typeHeading, 100);
                } else {
                    phase++;
                    setTimeout(typeHeading, 300); // Move to next phase
                }
            } else if (phase === 3) {
                // Phase 3: Type Welcome to my blog
                if (charIndex < welcomeText.length) {
                    tempText += welcomeText[charIndex];
                    charIndex++;
                    welcomeDiv.textContent = "{" + tempText + "}";
                    setTimeout(typeHeading, 100);
                } else {
                    phase++;
                    typeHeading();
                }
            }else if (phase==4){
                if (blinked){
                    welcomeDiv.textContent = "{"+tempText+".}";
                    blinked = false;
                }
                else{
                    welcomeDiv.textContent = "{"+tempText+"|}";
                    blinked = true;
                }
                setTimeout(typeHeading, 500);
            }
        }
        typeHeading(); // Start the animation
    </script>
</div>


