import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from colorama import Fore, Back, Style, init

#initialization for colorama
init(autoreset=True)

class PriceComparator:
    def __init__(self):
        #Created user agent
        self.user_agent = UserAgent()

        #Flipkart header
        self.flipkart_headers = {
            'authority': 'www.google.in',
            'pragma': 'no-cache',
            'cache-control': 'no-cache',
            'dnt': '1',
            'upgrade-insecure-requests': '1',
            'user-agent': self.user_agent.random,  #random user agent using fake-useragent
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'none',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-dest': 'document',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        }

    def search_product(self, product_name):
        #product search message
        print(Fore.BLUE + "\nSearching for product on Amazon and Flipkart...\n" + Style.RESET_ALL)

        #Search product on amazon and flipkart
        amazon_info = self.search_amazon(product_name)
        flipkart_info = self.search_flipkart(product_name)

        #result amazon
        print(Fore.GREEN + "Amazon Product:")
        if amazon_info:
            print(amazon_info)
        else:
            print(Fore.RED + "Product not found on Amazon.")
        print(Style.RESET_ALL)

        #result flipkart
        print(Fore.GREEN + "Flipkart Product:")
        if flipkart_info:
            print(flipkart_info)
        else:
            print(Fore.RED + "Product not found on Flipkart.")
        print(Style.RESET_ALL)

    def search_amazon(self, product_name):
        #headers and parameters for amazon
        headers = {'User-Agent': self.user_agent.random}
        params = {'field-keywords': product_name}
        url = 'https://www.amazon.in/s'
        
        #request to amazon
        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            results = soup.find_all('div', {'data-component-type': 's-search-result'})
            
            if results:
                top_result = results[0]
                title = top_result.find('span', {'class': 'a-text-normal'}).text
                price = top_result.find('span', {'class': 'a-price'}).find('span', {'class': 'a-offscreen'}).text
                link = top_result.find('a', {'class': 'a-link-normal'})['href']
                
                amazon_info = (
                    f"Title: {title}\nPrice: {price}\nAmazon Link: {Fore.BLUE}https://www.amazon.in{link}{Style.RESET_ALL}"
                )
                return Fore.CYAN + amazon_info + Style.RESET_ALL
        return None

    def search_flipkart(self, product_name):
        #parameters for flipkart
        url = 'https://www.flipkart.com/search'
        params = {'q': product_name, 'otracker': 'search'}
        
        #request to flipkart
        response = requests.get(url, headers=self.flipkart_headers, params=params)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            results = soup.find_all('div', {'class': '_2kHMtA'})
            
            if results:
                top_result = results[0]
                title = top_result.find('div', {'class': '_4rR01T'}).text
                price = top_result.find('div', {'class': '_30jeq3 _1_WHN1'}).text[1:]
                link = top_result.find('a', {'class': '_1fQZEK'})['href']
                
                flipkart_info = (
                    f"Title: {title}\nPrice: Rs {price}\nFlipkart Link: {Fore.BLUE}https://www.flipkart.com{link}{Style.RESET_ALL}"
                )
                return Fore.CYAN + flipkart_info + Style.RESET_ALL
        return None

if __name__ == "__main__":
    comparator = PriceComparator()
    
    #Prompts user for product name
    product_name = input(Fore.MAGENTA + "Enter the product name: " + Style.RESET_ALL)
    
    #perform product search and output display
    comparator.search_product(product_name)
