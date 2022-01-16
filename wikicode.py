def WikisGetLink(lookfor):
  import requests
  try:
    #Splits text
    lines = lookfor.split()
    
    #Capitalizes the starting letter of the words
    for index, line in enumerate(lines):
      lines[index] = line[0].upper() + line[1:]
          
    print("_".join(lines))
    
    #If a space was in it, it will change it to an underscore
    lookfor = "_".join(lines)
    #Looks for the page
    complete = "https://is.wikipedia.org/wiki/" + lookfor

    #Gets response
    response = requests.get(complete)
    
    #Checks if it doesn't exist
    if "Þessi grein er ekki til." in str(response.text):
      complete = "Þessi grein er ekki til."

    print("_________")
    
    #prints it out
    print(complete)

  except Exception:
    print("Villa kom upp")
