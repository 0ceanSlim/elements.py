// Assuming you have a variable that holds the active wallet
let activeWallet = ''; // Replace this with your active wallet variable


function setActiveWallet(walletName) {
  activeWallet = walletName; // Update the activeWallet variable with the clicked wallet
  updateActiveWalletDisplay(); // Update the displayed content

  localStorage.setItem('activeWallet', walletName);

  fetch('/set_active_wallet', {
    method: 'POST',
    body: new URLSearchParams({ walletName })
})
.then(response => response.json())
.then(data => {
    console.log(data.message); // Log success message from the backend
})
.catch(error => {
    console.error('Error:', error);
});
}

function updateActiveWalletDisplay() {
  const activeWalletDisplay = document.getElementById('activeWalletDisplay');
  activeWalletDisplay.textContent = `Active Wallet: ${activeWallet}`;
}

// Call the function to initially update the display
updateActiveWalletDisplay();

