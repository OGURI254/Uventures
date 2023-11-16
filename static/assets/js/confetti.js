const body = document.getElementById("success-body")

function createConfetti() {
    const confetti = document.createElement('div');
    confetti.className = 'confetti';
    confetti.style.left = Math.random() * window.innerWidth + 'px';
    body.appendChild(confetti);

    // Remove the confetti element after animation completes
    confetti.addEventListener('animationend', () => {
      confetti.remove();
    });
  }

  function confettiRain() {
    setInterval(createConfetti, 200); // Adjust the interval as needed
  }

  // Start the confetti rain when the page loads
  window.addEventListener('load', confettiRain);

  console.log("hfuihaifhij")