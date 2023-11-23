import requests
from bs4 import BeautifulSoup

def scrape_etherscan_address(address):
    # Construct the URL for the Ethereum address on Etherscan
    url = f'https://etherscan.io/address/{address}'

    # Send an HTTP request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract relevant information (replace 'your-tag' with the actual tag you want to extract)
        # Example: Extracting the balance
        balance_tag = soup.find('span', class_='text-success')
        balance = balance_tag.text.strip() if balance_tag else 'Not available'

        # Print the extracted information
        print(f'Ethereum Address: {address}')
        print(f'Balance: {balance}')

    else:
        print(f'Error: Unable to fetch data. Status code: {response.status_code}')

# Example usage
eth_address = '0x742d35Cc6634C0532925a3b844Bc454e4438f44e'
scrape_etherscan_address(eth_address)
