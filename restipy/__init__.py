import json, yaml, boto3, requests, base64, time

from service import KmsService

from jinja2 import Environment, FileSystemLoader
from jose import jwt

class RestipyService:
    def __init__(self, templateFilename):
        session = boto3.session.Session()

        jinja_env = Environment(loader=FileSystemLoader(''))
        jinja_env.globals.update({
            'kms': KmsService(session),
            'jwt': jwt,
            'base64': base64,
            'time': time
        })

        self.template = jinja_env.get_template(templateFilename)

    def execute(self, params):
        configStr = self.template.render(params)

        config = yaml.load(configStr)

        for request in config['requests']:
            response = requests.get(**request)
            try:
                print json.dumps(response.json())
            except ValueError as error:
                print error.message

if __name__ == '__main__':
    import sys, os
    templateFilename = sys.argv[1]
    service = RestipyService(templateFilename)
    service.execute(os.environ)
