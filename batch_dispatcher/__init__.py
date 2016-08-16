import json, yaml, boto3, os, requests, base64, time

from service import KmsService

from jinja2 import Environment, FileSystemLoader
from jose import jwt

def handler(event, context):
    session = boto3.session.Session()

    jinja_env = Environment(loader=FileSystemLoader(''))
    jinja_env.globals.update({
        'kms': KmsService(session),
        'jwt': jwt,
        'base64': base64,
        'time': time
    })

    event.update(os.environ)

    template = jinja_env.get_template('config.yml')
    template = template.render(event)

    config = yaml.load(template)

    for request in config['requests']:
        response = requests.get(**request)
        print json.dumps(response.json())


if __name__ == '__main__':
    handler({}, {})
