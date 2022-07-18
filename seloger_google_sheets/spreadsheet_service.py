from abc import ABC, abstractmethod
from typing import List

from seloger_google_sheets.real_estate import RealEstate

class SpreadsheetsService(ABC):
    """Meant to be inherited"""
    
    def __init__(self) -> None:
        """Connect to the third service when instantiating"""
        self.creds = None
        self.auth()
    
    @abstractmethod
    def auth(self):
        """Connect to the chosen third service"""
        
    @abstractmethod
    def insert(self, real_estates: List[RealEstate]):
        """Insert real estates data inside the spreadsheet""" 
    
    @abstractmethod
    def clear(self):
        """Clears the whole spreadsheet"""