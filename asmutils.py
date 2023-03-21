# Helpful utilities when grading ASM
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
        mark = len(line) if ';' not in line else line.find(';')
        bits = line[:mark].split()
        if len(bits) > 2:
          data.append(bits)
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

# Get instructions from code section
def getIns(file):
  # Store data in a list
  data = []
  with open(file) as f:
    lines = f.readlines()
    # Only get code between .data and .code
    is_past_code = False
    for line in lines:
      line = line.casefold().replace(',', ' ')
      if not is_past_code and 'main proc' in line:
        is_past_code = True
        continue
      elif is_past_code and 'invoke' in line:
        is_past_code = False
        break
      elif is_past_code and line[0] != ';' and line[0] != '\n':
        mark = len(line) if ';' not in line else line.find(';')
        bits = line[:mark].split()
        if len(bits) > 0:
          data.append(bits)
    return data

# Get opcodes only 
def getOp(file):
  instructions = getIns(file)
  data = []
  for elem in instructions:
    data.append(elem[0])
  return set(data)
    
# Determine if 32 bit or 64 bit program
def is32(file):
  with open(file) as f:
    lines = f.readlines()
    for line in lines:
      if '.386' in line:
        print('32 BIT PROGRAM\n')
        return True
    print('WARNING: 64 BIT SYSTEM CODE DETECTED, ADAPT VS AS NECESSARY\n')
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

# Standardize linker
def standardize(file):
  os.system(f'sed -i "" "s/^main/_main/" "{file}"')
  os.system(f'sed -i "" "s/END main/END _main/" "{file}"')

# Copy file to clipboard and delete
def replace(file):
  os.system(f'cat "{file}" | pbcopy && rm "{file}"')
  print(f'Replaced {file} successfully')
