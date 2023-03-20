#Helpful utilities when grading ASM

import os

# Get variables from data section
def getVar(file):
  # Store data in a list
  data = []
  with open(file) as f:
    lines = f.readlines()
    # Only get code between .data and .code
    is_past_data = False
    for line in lines:
      line = line.casefold()
      if not is_past_data and '.data' in line:
        is_past_data = True
        continue
      elif is_past_data and '.code' in line:
        is_past_data = False
        break
      elif is_past_data and line[0] != ';' and line[0] != '\n':
        bits = line.replace(';', ' ').split()
        if len(bits) > 2:
          data.append(bits[:3])
    return data

# Get specific memory variable
def getMem(file):
  data = getVar(file)
  # Filter from data, we know memory will start as 0 or ?
  new_data = []
  for elem in data:
    if elem[2] == '0' or elem[2] == '?':
      new_data.append(elem)
  return new_data
    
      
# Determine if 32 bit or 64 bit program
def is32(file):
  with open(file) as f:
    lines = f.readlines()
    for line in lines:
      if '.386' in line:
        return True
    return False

# Determine if a certain command is used
def usesCommand(file, command):
  command = command.casefold()
  with open(file) as f:
    lines = f.readlines()
    # Only parse after flag checkpoint
    flag = False
    for line in lines:
      line = line.casefold()
      if not flag and '.code'.casefold() in line:
        flag = True
        continue
      elif flag:
       if command in line:
         return True
    return False
      
# Gets function names
def getFunction(file):
  # Store functions as string list
  names = []
  with open(file) as f:
    lines = f.readlines()
    for line in lines:
      if 'endp'.casefold() in line.casefold():
        names.append(line.split()[0])
    return names

# Assert functionality
def assertt(msg, expected, outcome):
  # Convert to string just in case
  expected = str(expected)
  outcome = ''.join(str(outcome))
  if expected.casefold() in outcome.casefold():
    print(f'{msg}: PASS')
  else:
    print(f'{msg}: FAIL')

# Assert functionality
def assertt(msg, test):
  if test: 
    print(f'{msg}: PASS')
  else:
    print(f'{msg}: FAIL')


# Standardize linker
def standardize(file):
  os.system(f'sed -i "" "s/^main/_main/" "{file}"')
  os.system(f'sed -i "" "s/END main/END _main/" "{file}"')

# Copy file to clipboard and delete
def replace(file):
  os.system(f'cat "{file}" | pbcopy && rm "{file}"')
  print(f'Copied {file}')
