# Libraries
from utils.verifiers import testValue
import sys
sys.path.append("../utils")
from objects import Parser, Processor

# -- ObjectTests
testList1 = {
  "listTests": [
    "google.com",
    "www.google.com",
    "google.com/testing",
    "www.google.com/testing",
    "http://google.com",
    "https://google.com",
    "https://www.google.com",
    "https://testing.google.com",
    "https://google.com/",
    "http://google.com/page",
    "http://www.google.com/page",
    "http://testing.google.com/page",
    "http://google.com/page/",
    "http://google.com/page/page2",
    "http://google.com/page/page3",
    "/intl/es-419/policies/terms/"
  ],
  "results": "google.com"
}

testList2 = {
  "urls": [
    "https://google.com/",
    "https://aark.us/",
    "https://tryhackme.com/"
  ],
}

# -- Tests

# ---- Test 1 ----
for c, element in enumerate(testList1["listTests"]):
  result = testList1["results"]
  print (f"Test 1.{c+1} => ", end="")
  resultFunction = Parser.getDomainPrincipal(element, "http://google.com")
  status = testValue(resultFunction, result)
  if not status:
    break
print ("--- All tests passed ---")


# ---- Test 2 ----
for c, element in enumerate(testList2["urls"]):
  print (f"Test 2.{c+1} -> {element}")

  listURLS = Processor.getURLs(element)
  for e, URL in enumerate(listURLS):
    print (f"Test 2.{c+1}.{e+1} => ", end="")
    dominioOriginal = Parser.getDomainPrincipal(element)
    dominioEncontrado = Parser.getDomainPrincipal(URL)

    status = testValue(dominioOriginal, dominioEncontrado)
    if not status:
      break
print ("--- All tests passed ---")

