def reverse(text):
  rvs = ""
  rangeTill = (1+len(text))*-1
  for x in range(-1,rangeTill , -1):
    rvs = rvs + text[x]
  print(rvs)