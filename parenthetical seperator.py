for x in data:
  if x == '(' or x == ')':
    test = not test
    print(group)
    group = ''
    continue
  elif test == True:
    group += x
    continue
  print(text, x)