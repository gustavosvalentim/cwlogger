import setuptools


with open('requirements.txt') as reqbuf:
    requirements = reqbuf.readlines()


setuptools.setup(
    name='cwlogger',
    version='0.0.1',
    author='Gustavo Valentim',
    packages=setuptools.find_packages(include=['cwlogger', 'cwlogger.*']),
    install_requires=requirements,
    python_requires='>=3.6'
)