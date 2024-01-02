// Function to delete the active wallet
function deleteActiveWallet() {
    const activeWallet = localStorage.getItem('activeWallet');
  
    fetch('/delete_active_wallet', {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ walletName: activeWallet }),
    })
    .then(response => {
      if (response.ok) {
        console.log('Active wallet deleted successfully');
        // Optionally, perform any additional actions after successful deletion
      } else {
        console.error('Failed to delete active wallet');
      }
    })
    .catch(error => {
      console.error('Error:', error);
    });
  }
  
  // Attach a click event listener to the delete wallet button
  const deleteButton = document.getElementById('deleteWalletButton');
  deleteButton.addEventListener('click', deleteActiveWallet);
  