// Function to fetch wallets and display them
function fetchWallets() {
  fetch('/wallets')
      .then(response => response.json())
      .then(data => {
          const wallets = data.wallets;

          // Display wallets in the frontend (e.g., as a list or dropdown)
          const walletsList = document.getElementById('walletList');
          walletsList.innerHTML = '';

          wallets.forEach(wallet => {
              const walletItem = document.createElement('div');
              walletItem.textContent = wallet;
              walletItem.classList.add(
                'p-1', // Padding
                'm-1', // Margin bottom
                'cursor-pointer', // Cursor style
                'hover:bg-blue-300', // Hover background color (change to suit your preference)
                'w-fit',
                'bg-blue-400',
                'rounded-md',
                'ml-2'
              );
            
              // Add event listener to set the wallet as active on click
              walletItem.addEventListener('click', () => setActiveWallet(wallet));
              
              walletsList.appendChild(walletItem);
          });
      })
      .catch(error => {
          console.error('Error:', error);
      });
}

// Call fetchWallets function on page load to get and display wallets
document.addEventListener('DOMContentLoaded', fetchWallets);