
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'autor': 'Olga Yelisyeva',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'autor_email': 'yeliseeva.oa@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex47'],
    'scripts': [],
    'name': 'game from book'
}

setup(**config)
