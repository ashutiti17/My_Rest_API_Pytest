import requests

from utils.config import Base_Url, REQUEST_TIMEOUT




class APIClient:
    def get(self , url, headers=None):
        return requests.get(url, headers=headers, timeout=REQUEST_TIMEOUT)
    
    def post(self , url, headers=None , payload=None):
        return requests.post(url, headers=headers, json=payload, timeout=REQUEST_TIMEOUT)
    
    def put(self,url,headers=None, payload=None):
        return requests.put(url, headers=headers, json=payload, timeout=REQUEST_TIMEOUT)
    
    def delete(self,url,headers=None):
        return requests.delete(url, headers=headers, timeout=REQUEST_TIMEOUT)

