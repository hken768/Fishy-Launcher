from colorama import Fore, Style

hello = r"""
    _______      __         
   / ____(_)____/ /_  __  __
  / /_  / / ___/ __ \/ / / /
 / __/ / (__  ) / / / /_/ / 
/_/   /_/____/_/ /_/\__, /  
                   /____/   
"""

def print_title():
    print(Fore.BLUE + hello + Style.RESET_ALL)
