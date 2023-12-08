import os
import json

class __cache__handler__:
    @staticmethod
    def get_path_ctor(self, name: str) -> str:
        return f"parser/cache/{name}.ctor"

    @staticmethod
    def valid_ctor(self, name: str) -> bool:
        return os.path.exists(self.get_path_ctor(name))


class __cache__:
    def __init__(self, debug: bool = True):
        self.debug = debug
        
    def write_data(self, name_cache: str, data: dict) -> None:
        try:
            if __cache__handler__.valid_ctor(name_cache):
                with open(__cache__handler__.get_path_ctor(name_cache), "w+") as cache:
                    cache.write(json.dumps(data))
                    
        except Exception as err:
            if self.debug: print(err)
            
    def read_data(self, name_cache: str):
        try:
            if __cache__handler__.valid_ctor(name_cache):
                with open(__cache__handler__.get_path_ctor(name_cache), "r") as cache:
                    return json.loads(cache.read())
                
        except Exception as err:
            if self.debug: print(err)