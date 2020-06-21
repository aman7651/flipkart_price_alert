import requests as r
from bs4 import BeautifulSoup as bs
import time


URL = input("Enter Url")

while True:
    page = r.get(URL)
    soup = bs(page.content, "html.parser")
    
    # Use whatever you see in Inspect Element of the website this keeps changing from web page to webpage
    price = soup.find("div", {"class": "_3qQ9m1"}).text
    # Uncomment above line if you use Flipkart website
    
    # This is used to remove the ₹ symbol and get the price
    price = price[1:]
    
    # This is used to remove the , in between the prices to make it a number
    price_ar = price.split(",")
    price = ''.join(price_ar)
    
    # Conver the price which is string to an integer to compare
    price = int(price)
    
    print(price)
    
    # Use your comparing logic here below
    # Example:
    # if price < 11000:
    # w.open(URL) this opens the web page in a browser
    # break
