from data.manager import DataManager
from domain.links import Links
from domain.scraper import PropertyScraper
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor
#we can also implement , as_completed if we don't care about the order of the result and it will be faster than using map


def update_ranges():
    pass

def update_links() -> list[str]:
    links = Links()
    print("SCRAPING...")
    links_list = links.scrape()
    print("SCRAPED: OK")
    return links_list

def scrape_property(link):
    scraper = PropertyScraper(link)
    return scraper.scrape()

# links = update_links()
# DataManager.links_export(links)
# OR 
links = DataManager.links_import()
# links = links[:1000]
data_list = []
with ThreadPoolExecutor(max_workers=10) as executor:
    for data in tqdm(executor.map(scrape_property, links), total=len(links)):
        data_list.append(data)
for data in data_list:
    print(data)