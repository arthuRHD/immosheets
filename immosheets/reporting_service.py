from abc import ABC, abstractmethod

from .real_estate import RealEstate

class ReportingService(ABC):
    """Meant to be inherited"""
    
    def __init__(self) -> None:
        """Connect to the third service when instantiating"""
        self.creds = None
        self.auth()
    
    @abstractmethod
    def auth(self):
        """Connect to the chosen third service"""
        
    @abstractmethod
    def insert(self, real_estates: list[RealEstate]):
        """Insert real estates data""" 
    
    @abstractmethod
    def clear(self):
        """Clears data"""