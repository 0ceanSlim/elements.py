// Function to fetch and display RPC config
function fetchRPCConfig() {
    fetch('/get_rpc_config')
        .then(response => response.json())
        .then(data => {
            // Check if the config exists in localStorage, if not, use the fetched data
            const rpcHost = localStorage.getItem('rpcHost') || data.rpcHost;
            const rpcPort = localStorage.getItem('rpcPort') || data.rpcPort;
            const rpcUser = localStorage.getItem('rpcUser') || data.rpcUser;
            const rpcPassword = localStorage.getItem('rpcPassword') || data.rpcPassword;

            document.getElementById('rpcHost').value = rpcHost;
            document.getElementById('rpcPort').value = rpcPort;
            document.getElementById('rpcUser').value = rpcUser;
            document.getElementById('rpcPassword').value = rpcPassword;
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

// Function to save RPC config to localStorage and update the server
function saveRPCConfig() {
    const rpcHost = document.getElementById('rpcHost').value;
    const rpcPort = document.getElementById('rpcPort').value;
    const rpcUser = document.getElementById('rpcUser').value;
    const rpcPassword = document.getElementById('rpcPassword').value;

    // Save to localStorage
    localStorage.setItem('rpcHost', rpcHost);
    localStorage.setItem('rpcPort', rpcPort);
    localStorage.setItem('rpcUser', rpcUser);
    localStorage.setItem('rpcPassword', rpcPassword);

    // Update the server with the new config
    const formData = new FormData();
    formData.append('rpcHost', rpcHost);
    formData.append('rpcPort', rpcPort);
    formData.append('rpcUser', rpcUser);
    formData.append('rpcPassword', rpcPassword);

    fetch('/update_rpc_config', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('rpcResult').innerHTML = data.message;
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

// Call fetchRPCConfig function on page load to get the config
document.addEventListener('DOMContentLoaded', function() {
    fetchRPCConfig();
});

// Listen for form submission to update config
document.getElementById('rpcConfigForm').addEventListener('submit', function(event) {
    event.preventDefault();
    saveRPCConfig();
});
