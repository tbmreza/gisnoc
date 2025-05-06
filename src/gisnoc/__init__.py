from typing import Any, Dict, Iterable, Iterator, Mapping, Optional, Tuple, TypeVar, Union
import sqlite3, os
from . import std_consig
# from .std_consig import *

K = TypeVar('K')
V = TypeVar('V')

class Consig(Dict[K, V]):
    """
    A custom dictionary class that allows overriding the getter and setter methods.
    """
    db_conn = None
    def _connect_cache(self):
        CACHE_PATH = ".consig-cache/cache"
        self.db_conn = sqlite3.connect(CACHE_PATH)
    
    def __init__(self, *args, **kwargs):
        """Effects:
        1. Make .consig-cache folder.
        """
        super().__init__(*args, **kwargs)
        os.makedirs(".consig-cache", exist_ok=True)
        
    def __getitem__(self, key: K) -> V:
        """
        Override dictionary access with [] syntax.
        Called when you use: value = my_dict[key]
        """
        print(f"Getting value for key: {key}")
        
        
        # Get the actual value from the parent dictionary
        value = super().__getitem__(key)
        
        # Optional: Transform the value before returning it
        return value
    
    def __setitem__(self, key: K, value: V) -> None:
        """
        Override dictionary assignment with [] syntax.
        Called when you use: my_dict[key] = value
        """
        if self.db_conn == None:
            self._connect_cache()
        print(f"Setting key {key} to value: {value}")
        
        
        # Store the value in the parent dictionary
        # global tx
        # tx  = 12
        super().__setitem__(key, value)
    
    def __delitem__(self, key: K) -> None:
        """
        Override dictionary deletion with del syntax.
        Called when you use: del my_dict[key]
        """
        print(f"Deleting key: {key}")
        
        # Custom deletion logic here
        super().__delitem__(key)
    
    def get(self, key: K, default: Any = None) -> Union[V, Any]:
        """
        Override the get method to use our custom __getitem__.
        """
        try:
            return self[key]
        except KeyError:
            print(f"Key {key} not found, returning default")
            return default


# d = Consig(a=1, tx=2, c=3)
# d["tx"] = 20
# print(tx)

def lfilter(tx):
    pass
    # ??: dll.lfilter(tx)

# def globalTxSetter():
#     global tx
#     tx = 199

# globalTxSetter()
# print(tx)


# if __name__ == "__main__":
#     pass