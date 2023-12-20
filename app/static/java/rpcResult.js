fetch('/get_rpc_config')
    .then(response => response.json())
    .then(data => {
        document.getElementById('rpcHost').value = data.rpcHost;
        document.getElementById('rpcPort').value = data.rpcPort;
        document.getElementById('rpcUser').value = data.rpcUser;
        document.getElementById('rpcPassword').value = data.rpcPassword;
    })
    .catch(error => {
        console.error('Error:', error);
    });

    document.getElementById('rpcConfigForm').addEventListener('submit', function(event) {
        event.preventDefault();
        const form = event.target;
        const formData = new FormData(form);

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
    });