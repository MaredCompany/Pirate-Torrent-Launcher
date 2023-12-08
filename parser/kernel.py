import asyncio 
import aiohttp

from fake_useragent import UserAgent
from bs4 import BeautifulSoup


class Kernel:


    def __init__(self, debug: bool = True):
        self.url = "https://tuttop.com/"
        self.debug = debug


    async def get_max_pages(self, name_search: str) -> int:
        try:
          async with aiohttp.ClientSession(headers={"User-Agent": UserAgent().random}) as session:
            async with session.post(self.url + f"index.php?do=search&subaction=search&search_start=1&full_search=0&story={name_search}") as response:
                  html = await response.text()
                  
                  bs = BeautifulSoup(html, "html.parser")
                  
                  pages = bs.find("div", {"class": "navigation-center"})
                  counter = pages.find_all("a", {"href": "#"})
                  
                  return len(counter) + 1
                  
        except Exception as err:
            if self.debug: print(err)
            
            
    async def get_main_informations(self, page: int, name_search: str) -> dict:
        try:
            async with aiohttp.ClientSession(headers={"User-Agent": UserAgent().random}) as session:
                async with session.post(self.url + f"index.php?do=search&subaction=search&search_start=&full_search=0&story={name_search}") as response:
                    html = await response.text()
                    
                    base = BeautifulSoup(html, "html.parser")
                    
                    Titles = base.find_all("div", {"class", "main-news-title"})
                     
            
            
        except Exception as err:
            if self.debug: print(err)
            
            
print(asyncio.run(Kernel().get_max_pages("war")))


