from bs4 import BeautifulSoup
import requests, json
import os
from utils.printers import console

class Parser:
  def __init__():
    pass

  def getDomainPrincipal(url:str, urlbase:str="") -> str:
    if url.startswith("http://") or url.startswith("https://"):
      url = url.split("://")[1]
      domain = ".".join(url.split("/")[0].split(".")[-2:])
      return domain

    elif url.startswith("/"):
      url = f"{urlbase}{url}"
      url = url.split("://")[1]
      domain = ".".join(url.split("/")[0].split(".")[-2:])
      return domain

    else:
      urlbase.startswith("http://") or urlbase.startswith("https://")
      urlbase = urlbase.split("://")[1]
      domain = ".".join(urlbase.split("/")[0].split(".")[-2:])
      return domain
      

  def setDirectories(domain:str, url:str) -> str:
    """Throw:
        Domain: google.com
        URL: /directory/directory ó https://google.com/directory/directory ó index.html
        
        Result: https://google.com/directory/directory"""

    schema = "https://"

    if url.startswith("/"):
      return f"{schema}{domain}{url}"
    elif url.startswith("https://") or url.startswith("http://"):
      return url
    else:
      return f"{schema}{domain}/{url}"
    
  def isRelated(domain:str, url:str) -> True:
    return domain in url
    
# -- Processor --
class Processor:
  def __init__():
    pass

  def getURLs(url:str) -> list:
    """Throw:
      URL: https://google.com/

      Result: ["https://google.com", "https://www.google.com", "https://testing.google.com", "https://google.com/others"]"""
    
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    links = []
    for link in soup.find_all("a"):
      urlFounded = link.get("href")
      if not urlFounded: continue
      dominio = Parser.getDomainPrincipal(urlFounded, url)
      link = Parser.setDirectories(dominio, urlFounded)

      if Parser.isRelated(dominio, url):
        links.append(link)

    return links
  
  def getTechs(html_string:str) -> list:
      
      # Get the route
      route = os.path.dirname(os.path.abspath(__file__))

      tech_dict = json.load(open(f"{route}/techs.json", "r"))
      found_technologies = []

      for tech_name, tech_info in tech_dict.items():
          # Verificar si el slug de la tecnología está presente en el HTML
          if tech_info["slug"].lower() in html_string.lower():
              found_technologies.append(tech_name)
      
      return found_technologies

class loop:
  def __init__(self, urlbase:str, limitLoops:int=5, verbose:int=2) -> dict:
    self.urlbase = urlbase
    self.limitLoops = limitLoops
    self.verbose = verbose
    self.loop:int = 0
    self.results = {
      "techs": {},
      "urls": []
    }

    listURLsBase = Processor.getURLs(urlbase)
    listURLsBase.append(urlbase)
    return loop.parseListURLs(self, listURLsBase)
  
  def parseListURLs(self, listURLs:list):
    if self.loop >= self.limitLoops or len(self.results["urls"]) >= 100:
      result = loop.finaliceLoop(self)
      return result

    console.success(f"Loop [{self.loop}] iniciado")
    self.loop += 1
    for URL in listURLs:
#      console.debug(json.dumps(self.results, indent=4))

      URLsInList = []

      for instance in self.results["urls"]:
        URLsInList.append(list(instance.keys())[0])

      if len(URLsInList) >= 100:
        break

      console.debug(f"Lista actual: {URLsInList} -> {len(URLsInList)}")

      if URL in URLsInList:
        continue

      try:
        html = requests.get(URL, timeout=5).text
      except Exception as Error:
        console.error(f"Se produjo un error: {Error}")
        continue
      techs = Processor.getTechs(html)

      # Saving to the URLs
      self.results["urls"].append({URL: techs})

      for tech in techs:
        # Process the techs
        if tech in self.results["techs"].keys():
            self.results["techs"][tech].append(URL)
        else:
            self.results["techs"][tech] = [URL]

    for URL in listURLs:
      listURLsAditional = Processor.getURLs(URL)
      console.debug(f"Lista encontrada: {listURLsAditional}")
      loop.parseListURLs(self, listURLsAditional)

  def finaliceLoop(self):
    return self.results