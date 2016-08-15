import json, click, boto3, yaml, requests

# from service import KmsService, JwtService, HttpService

from service import HttpService

def handler(event, context):
    with open('config.yml', 'r') as config_file:
        config = yaml.load(config_file)
    
    # session = boto3.Session(*config['aws'])
    
    # kmsService = KmsService(session=session)
    
    http_service = HttpService()
    
    for request in config['requests']:
        response = http_service.send(request)
        print json.dumps(response.json())
    

if __name__ == '__main__':
    handler(None, None)
