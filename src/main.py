# -- Import libraries --
from utils.extra import *
import os, json
from utils.objects import loop
from utils.printers import console

# -- Banner --
os.system('cls' if os.name == 'nt' else 'clear') # clear the screen
print (BANNER)

# -- Input User
page:str = input(f"{YELLOW}Pon una web: {WHITE}")
verbose:int = int(input(f"{YELLOW}Verbosidad (0-3): {WHITE}"))
timeout:int = int(input(f"{YELLOW}Tiempo de espera (en segundos) [por defecto: 10]): {WHITE}"))
limitPages:int = int(input(f"{YELLOW}Límite de páginas por analizar [por defecto: 100]: {WHITE}"))

# -- Process the web
process:loop = loop(page, verbose=verbose, timeout=10 if not timeout else timeout, limitPages=limitPages if limitPages else 100)
console.success("Se logró obtener los datos de manera satisfactoria!.")

print (json.dumps(process, indent=4))