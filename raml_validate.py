"""Validator that implementation matches the RAML spec"""
import re

import urllib
import ramlfications

from best_conferences import app
from flask_script import Manager


RAML_FILE = "best_conferences.raml"


manager = Manager(app)


def sanitize_flask(resource):
    pattern = r'<(\w+):(\w+)>'
    replace = r'{\2}'

    return re.sub(pattern, replace, resource)


@manager.command
def validate():
    spec_resources = get_raml_resources()
    implemented = {sanitize_flask(rule.rule): rule.methods for rule in app.url_map.iter_rules()}
    missing = []
    for resource, methods in spec_resources.items():
        if resource not in implemented:
            missing.append(resource)
    if missing:
        print("Missing implemantation for endpoints: ")
        print "\n".join(missing)
    else:
        print("Implementation up to spec!")


def get_raml_resources():
    api = ramlfications.parse(RAML_FILE)
    resources = {}
    for resource in api.resources:
        if resource.path in resources:
            resources[resource.path].append(resource.method)
        else:
            resources[resource.path] = [resource.method]

    return resources


if __name__ == "__main__":
    manager.run()
