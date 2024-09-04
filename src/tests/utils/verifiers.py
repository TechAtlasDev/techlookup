from .extra import GREEN, RED, WHITE

# This function returns an bool data, and print the results
def testValue(value, target, verbose=True) -> bool:
  result:bool = value == target

  if verbose:
    
    if result:
      approved = f"{GREEN}✅ Approved{WHITE}"
      print (approved)
    else:

      diferencesTypes = GREEN if type(value) == type(target) else RED
      diferencesValues = GREEN if str(value) == str(target) else RED

      declined = f"{RED}❌ Declined\n {WHITE}- [INPUT] {diferencesValues}{value} {WHITE}-> {diferencesTypes}{type(value)}{WHITE}  {WHITE}\n - [TARGET] {diferencesValues}{target} {WHITE}-> {diferencesTypes}{type(target)}{WHITE} {WHITE}"
      print (declined)

  return result