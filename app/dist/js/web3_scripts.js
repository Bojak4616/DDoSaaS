const ethereum = window.ethereum
$('#connectMetaMask').click(async function(){
    ethereum.request({ method: 'eth_requestAccounts' });
});

String.prototype.convertToHex = function (delim) {
    return this.split("").map(function(c) {
        return ("0" + c.charCodeAt(0).toString(16)).slice(-2);
    }).join(delim || "");
};

$('#ethereumButton').click(async function(){
    var domain = $('#url').val()
    var paddedUrl = String(domain).convertToHex().padEnd(64, '0')
    var domainLen = url.length.toString(16)
    
    const accounts = await ethereum.request({ method: 'eth_accounts' });
    const c2ContractAddress = "0x7b8459ca6CAabC727354eeF294B6349d3aC28E27"

    const transactionParameters = {
        to: c2ContractAddress, // Required except during contract publications.
        from: accounts[0], // must match user's active address.
        value: '0200000000000000', // Only required to send ether to the recipient from the initiating external account.
        data:
          `0x036fc6a7000000000000000000000000000000000000000000000000000000000000002000000000000000000000000000000000000000000000000000000000000000${domainLen}${paddedUrl}`, // Optional, but used for defining smart contract creation and interaction.
        chainId: '0x3', // Used to prevent transaction reuse across blockchains. Auto-filled by MetaMask.
      };
      
      // txHash is a hex string
      // As with any RPC call, it may throw an error
      const txHash = await ethereum.request({
        method: 'eth_sendTransaction',
        params: [transactionParameters],
      });

      $('#txHash').html(`<a href="https://ropsten.etherscan.io/tx/${txHash}" target="_blank">https://ropsten.etherscan.io/tx/${txHash}</a>`)

});



