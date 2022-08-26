from colorama import Style
from colorama import Fore

def error(message, end='\n'):
    _print(Fore.RED, str(message), end='\n')

def warn(message, end='\n'):
    _print(Fore.YELLOW, str(message), end='\n')

def success(message, end='\n'):
    _print(Fore.GREEN, str(message), end='\n')

def info(message, end='\n'):
    _print(Fore.BLUE, str(message), end='\n')




def _print(style, message, end='\n'):
    print(style + message + Style.RESET_ALL, end=end, flush=True)