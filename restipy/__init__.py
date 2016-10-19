import yaml, requests, importlib, inspect

from restipy.plugins import plugins
from pkg_resources import iter_entry_points
from jinja2 import Environment, FileSystemLoader

class RestipyService:
    def __init__(self, templateFilename):
        jinja_env = Environment(loader=FileSystemLoader(''))

        for entry_point in iter_entry_points(group='restipy.plugin', name=None):
            plugins[entry_point.name] = entry_point.load()

        jinja_env.globals.update(plugins)

        self.template = jinja_env.get_template(templateFilename)

    def execute(self, params):
        configStr = self.template.render(params)

        config = yaml.load(configStr)
        
        responses = []
        for request in config['requests']:
            responses.append(requests.get(**request))
        
        return responses

if __name__ == '__main__':
    import sys, os
    templateFilename = sys.argv[1]
    service = RestipyService(templateFilename)
    service.execute(os.environ)
