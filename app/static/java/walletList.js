window.onload = function () {
    fetch("/wallets")
      .then((response) => response.json())
      .then((data) => {
        const walletList = document.getElementById("walletList");
        if (data.wallets && data.wallets.length > 0) {
          const wallets = data.wallets;
          const walletsHTML = wallets
            .map((wallet) => `<p>${wallet}</p>`)
            .join("");
          walletList.innerHTML = walletsHTML;
        } else {
          walletList.innerHTML = "<p>No wallets found.</p>";
        }
      })
      .catch((error) => {
        console.error("Error fetching wallet list:", error);
        const walletList = document.getElementById("walletList");
        walletList.innerHTML = "<p>Error fetching wallets.</p>";
      });
  };