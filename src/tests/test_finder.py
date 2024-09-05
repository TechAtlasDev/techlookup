# Libraries
from utils.verifiers import testValue
from utils.printers import console
import sys, json, requests
sys.path.append("../utils")
from objects import Parser, Processor

# 1st step: Get an URL
URL = "https://aark.us/"

# 2nd step: Obtain a list of links
listURLS:list = Processor.getURLs(URL)
console.log(f"URLs found: {json.dumps(listURLS, indent=4)}")

# 3nd step: Add the URL base to the link list
listURLS.insert(0, URL)
console.log(f"URLs found: {json.dumps(listURLS, indent=4)}")

# 4th step: Make an dict
dataURLs = {
    "urls": [],
    "techs": {}
}

# 5th step: Iterate the list of URLs and process
for url in listURLS:

    # 5.1st step: Verify if the URL is in the dict
    if url in dataURLs.keys():
        continue

    # 5.2nd step: Get techs from the URL
    else:
      html = requests.get(url).text
      techs = Processor.getTechs(html)

      # 5.3rd step: Add the URL and techs to the dict
      dataURLs["urls"].append({url: techs})
      # 5.4th step: Add the techs to the dict
      for tech in techs:
        if tech in dataURLs["techs"].keys():
            dataURLs["techs"][tech].append(url)
        else:
            dataURLs["techs"][tech] = [url]

# 6th step: Print the dict
console.success(f"Data processed: {json.dumps(dataURLs, indent=4)}")

# 2nd Test --
console.log("Step 1: Test if the processor detects the tech stack from the html")
URL = requests.get("https://aark.us")
html = URL.text

techs = Processor.getTechs(html)
console.log(f"Techs found: {json.dumps(techs, indent=4)}")
for c, tech in enumerate(techs):
   console.success(f"{c}) {tech}")