import asyncio 
import aiohttp

from fake_useragent import UserAgent
from bs4 import BeautifulSoup

class MainPageInformate:
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
                    
                    data = { "title": [], "href": [], "text-game": [] }
                    
                    base = BeautifulSoup(html, "html.parser")    
                    base_titles = base.find_all("div", {"class", "main-news-title"})
                    base_news = base.find_all("div", {"class", "main-news-text"})
                    
                    for item in base_titles: 
                        base_info = item.find("a")
                        
                        if base_info is not None:
                            data["href"].append(base_info.get("href"))
                            data["title"].append(base_info.get_text().strip())
                            
                    for item in base_news:
                        data["text-game"].append(item.get_text())


                    return data
                                            
        except Exception as err:
            if self.debug: print(err)


class ProFoundInformate:
    def __init__(self, debug: bool = True):
        self.debug = debug
        self.data = []
        
    async def Task(self, url: str) -> None:
        try:
            pass
            
        except Exception as err:
            if self.debug: print(err)
    
    
    async def Queue(self, search_name: str):
        try:
            
            pages = await MainPageInformate().get_max_pages(search_name)
            tasks = []
             
            for i in range(1, pages + 1):
                href = await MainPageInformate().get_main_informations(i, search_name)
                
                if href is not None:
                    task = asyncio.create_task(
                        self.Task(href["href"])
                    )
                    tasks.append(task)
                
            return asyncio.gather(*tasks)
        
        except Exception as err:
            if self.debug: print(err)
