import os
import json


class CacheSupportiveHandler:
    @staticmethod
    def path_ctor(name: str) -> str:
        return f"parser/cache/{name}.ctor"


    @staticmethod
    def valid_ctor(name: str) -> bool:
        return os.path.exists(CacheSupportiveHandler.path_ctor(name))


class CacheTorent:
    @staticmethod
    def add(name_cache: str, data: dict) -> None:
        if not os.path.exists(CacheSupportiveHandler.path_ctor(name_cache)):
            with open(CacheSupportiveHandler.path_ctor(name=name_cache), "w+") as cache:
                cache.write(json.dumps(data))
        
        
    @staticmethod
    def read(name_cache: str) -> dict:
        if CacheSupportiveHandler.valid_ctor(name_cache):
            with open(CacheSupportiveHandler.path_ctor(name_cache), "r") as cache:
                return json.loads(cache.read())
    
    
    @staticmethod 
    def remove(name_cache: str) -> bool:
        return os.remove(CacheSupportiveHandler.path_ctor(name_cache))