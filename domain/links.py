import requests
from bs4 import BeautifulSoup as bs

class Links():
    TEST_LINK = [
        ("https://immovlan.be/en/real-estate?transactiontypes=for-sale&prop"
        "ertytypes=house,apartment&propertysubtypes=residence,villa,mixed-b"
        "uilding,master-house,cottage,bungalow,chalet,mansion,apartment,pen"
        "thouse,ground-floor,duplex,studio,loft,triplex&minprice="), 
        "&maxprice=", "&page=", "&noindex=1"
        ]
    
    def __init__(price_ranges: dict[str:int]):
        self.price_ranges: dict[str:int] = price_ranges
        self.links: list[str] = []

    def scrape(self):
        
    
    def cleaner():
        pass
