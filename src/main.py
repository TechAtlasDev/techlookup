# -- Import libraries --
from utils.objects import Processor
import json

# -- Banner --
print ("TechLookup")

# --

page = input("Pon una URL: ")
urls = Processor.getURLs(page)
print(json.dumps(urls, indent=4))