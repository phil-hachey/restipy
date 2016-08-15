from setuptools import setup, find_packages
from pip.req import parse_requirements
import pip

# parse_requirements() returns generator of pip.req.InstallRequirement objects
install_reqs = parse_requirements(
    'requirements.txt', session=pip.download.PipSession())

# reqs is a list of requirement
reqs = [str(ir.req) for ir in install_reqs]

setup(
    name='hivemarket-batch',
    packages=find_packages(),
    install_requires=reqs,
    entry_points={
        'console_scripts': [
            'hivemarket-batch = hivemarket_batch:main'
        ]
    }
)
