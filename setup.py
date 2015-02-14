from setuptools import setup
from bettertutors_rest_api import __version__

if __name__ == '__main__':
    setup(name='bettertutors_rest_api', version=__version__,
          author='Samuel Marks', license='TBA', py_modules=['bettertutors_rest_api'],
          test_suite='tests')
