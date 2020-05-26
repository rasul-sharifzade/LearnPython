def reverse2(text):
  rvsList = []
  i = 0
  rvs = ""
  for x in text:
    i = i  -1;
    rvsList.insert(i, x)
  for x in rvsList:
    rvs = rvs + x
  print(rvs) 