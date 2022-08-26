
import importlib

import sys
import importlib.util
import click

from py_core import pretty
from py_core.config import manager

@click.command()
@click.argument('file')
@click.option( '-c', '--config', default='config', help='Name of the config variable')
@click.option( '-r', '--required_only', default=False, help='If true, only the default config is dumped')
def cli(file, config, required_only):
    pretty.info(f'Importing {file}')
    
    manager._ignore_errors = True
    spec = importlib.util.spec_from_file_location('module.name', file)
    module = importlib.util.module_from_spec(spec)
    sys.modules['module.name'] = module
    spec.loader.exec_module(module)

    pretty.info(f'Retrieving configuration')
    config = getattr(module, config)
    config.dump_default_config(required_only)