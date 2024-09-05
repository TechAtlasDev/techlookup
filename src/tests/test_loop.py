# Libraries
from utils.printers import console
import sys
sys.path.append("../utils")
from objects import loop

URL = "https://www.unsa.edu.pe/"
console.log("Iniciando el loop")

loop = loop(URL, 3)

console.success("Datos recibidos por el sistema")
print (loop.results)