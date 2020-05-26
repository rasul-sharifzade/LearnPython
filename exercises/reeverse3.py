def reverse4(text):
  rvsList = []
  rvs = ""
  for x in text:
   rvsList.append(x)
  rvsList.reverse()
  for x in rvsList:
    rvs = rvs + x
  print(rvs)