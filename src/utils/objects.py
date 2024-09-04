from bs4 import BeautifulSoup
import requests

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