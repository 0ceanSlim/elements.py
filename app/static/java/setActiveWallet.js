// Function to set the active wallet in localStorage
function setActiveWallet(walletName) {
    localStorage.setItem('activeWallet', walletName);

    // Optionally, update UI to highlight/select the active wallet
    // For example, you can add a CSS class to highlight the selected wallet
    
    // Send the selected wallet to the backend to set it as active
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