def WikisGetLink(lookfor):
  import requests
  try:
    lines = lookfor.split()

    for index, line in enumerate(lines):
      lines[index] = line[0].upper() + line[1:]
          
    print("_".join(lines))

    lookfor = "_".join(lines)
    complete = "https://is.wikipedia.org/wiki/" + lookfor


    response = requests.get(complete)

    if "Þessi grein er ekki til." in str(response.text):
      complete = "Þessi grein er ekki til."

    print("_________")
  
    print(complete)

  except Exception:
    print("Villa kom upp")
