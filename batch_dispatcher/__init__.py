import json, yaml, boto3, os, requests

from service import JwtService, KmsService, ResolverService

from jinja2 import Environment, FileSystemLoader

def handler(event, context):
    session = boto3.session.Session()

    jinja_env = Environment(loader=FileSystemLoader(''))
    jinja_env.globals.update({
        'kms': KmsService(session),
        'jwt': JwtService()
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
