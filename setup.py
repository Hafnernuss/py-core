from setuptools import setup
from setuptools import find_packages

setup(
  name='py_core',
  packages=find_packages('.'),
  install_requires=[
    'click>=8.1.3',
    'python-decouple>=3.6'
    ],
  entry_points={
    'console_scripts' : [
      'dump_config = py_core.config.dump_config:cli',
    ]
  }
)