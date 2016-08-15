import requests

class HiveMarketService:
    
    def __init__(self, api_url, token):
        self.api_url = api_url
        self.token = token
        
    def send_reoccuring(self):
        url = "{api_url}/v1/reoccurring-order/action/process".format(api_url=self.api_url)
        headers = {
            'Authorization': 'JWT {token}'.format(token=self.token)
        }
        
        return requests.get(
            url=url,
            headers=headers)