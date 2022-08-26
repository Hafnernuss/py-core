import os 
import json
import decouple
from decouple import undefined
from decouple import Csv
from py_core import pretty

Csv = Csv
_ignore_errors = False

class ConfigurationManager():
    parser = None
    config = {}
    path = None
    
    default_conf = {}
    default_conf_required = {}

    def __init__(self, path=None):
        self.path = path
        self.parser = decouple.AutoConfig(path)

    def read_param(self, key, default=undefined, suggestion=undefined, cast=str, help_text=None):
            if default is undefined and suggestion is undefined:
                pretty.error(f'cannot read key {key}: at least a default or suggestion is needed')
                exit(-1)

            self.default_conf[key] = {}
            self.default_conf[key]['value'] = default if default != undefined else suggestion
            self.default_conf[key]['help_text'] = help_text

            value = None
            try:
                value = self.parser(key, default=default, cast=cast)
            except Exception as e:
                if not _ignore_errors:
                    if suggestion is undefined:
                        pretty.error(e)
                    else:
                        pretty.error(f'{str(e)}, suggestion: {str(suggestion)}')
                    exit(-1)
                else:
                    self.default_conf_required[key] = {}
                    self.default_conf_required[key]['value'] = default if default != undefined else suggestion
                    self.default_conf_required[key]['help_text'] = help_text

            return value

    def dump_default_config(self, required_only=False):
        self._dump_config(self.default_conf_required if required_only else self.default_conf)
            
    def _dump_config(self, config):
        os.makedirs(self.path, exist_ok=True)
        target = os.path.join(self.path, '.env')
        with open(target, 'w') as config_file:
            for key, info in config.items():
                value = info['value']
                help_text = info['help_text']
                if help_text is not None:
                    help_text = help_text.replace('\n', '\n# ')
                    config_file.write(f'# {help_text}\n')
                config_file.write(f'{key}={value}')
                if help_text:
                    config_file.write('\n\n')
                else:
                    config_file.write('\n')

