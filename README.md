# py-core 0.0.2
A set of handy utilities I commonly use in my python projects

## Config manager
This manager class relies heavily on the [decouple](https://pypi.org/project/python-decouple/) package, but it adds a few additions:

- Suggestions:\
  If the default is deliberatly unset, an error message is raised upvon retrieval of the value, with a suggestion for which value could be a good one.
- Help texts:\
  Each parameter can be provided with a help text 
- Config dumping: 
  Creates a a file containing all parameters, with defaults/suggestion and help texts, if provided.

### Usage

First, create a configuration object. A path where the config file is located, can be passed:
```py
from py_core.config import manager

config = manager.ConfigurationManager('config')
```

and for retrieving values:
```py
DEBUG = config.read_param(
    'DEBUG', 
    default=True, 
    cast=bool,
    suggestion=False, 
    help_text='Specifies if this system should run in debug mode'
)
```

The config can be dumped by invoking the `dump_config` argument:
```
dump_config path_to_config_file [-r] [-c]
```

The path must specify the python module that initially creates the manager. 
The `-r` argument specifies that only required variables (i.e. no default) should be dumped, 
and `-c` specifies the name of the manager variable (default is `config`)
   
