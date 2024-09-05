from .extra import *


class console:
  def __init__():
    pass

  def log(message:any, confirmation=False) -> None:
    MESSAGE = f"{BLUE}[{WHITE}INFO{BLUE}]{WHITE} {YELLOW}{message}{WHITE}"
    print(MESSAGE)
    if confirmation:
      input("Presiona para continuar...")

  def error(message:any, confirmation=True) -> None:
    MESSAGE = f"{RED}[{WHITE}ERROR{RED}]{WHITE} {YELLOW}{message}{WHITE}"
    print(MESSAGE)
    if confirmation:
      input("Presiona para continuar...")
  
  def success(message:any, confirmation=False) -> None:
    MESSAGE = f"{GREEN}[{WHITE}SUCCESS{GREEN}]{WHITE} {YELLOW}{message}{WHITE}"
    print(MESSAGE)
    if confirmation:
      input("Presiona para continuar...")

  def warning(message:any, confirmation=True) -> None:
    MESSAGE = f"{YELLOW}[{WHITE}WARNING{YELLOW}]{WHITE} {YELLOW}{message}{WHITE}"
    print(MESSAGE)
    if confirmation:
      input("Presiona para continuar...")
  
  def debug(message:any, confirmation=True) -> None:
    MESSAGE = f"{MAGENTA}[{WHITE}DEBUG{MAGENTA}]{WHITE} {YELLOW}{message}{WHITE}"
    print(MESSAGE)
    if confirmation:
      input("Presiona para continuar...")
